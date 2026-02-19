import SwiftUI
import WebKit

struct WebView: UIViewRepresentable {
    let url: URL
    let reloadTrigger: UUID

    func makeCoordinator() -> Coordinator {
        Coordinator()
    }

    func makeUIView(context: Context) -> WKWebView {
        let prefs = WKWebpagePreferences()
        prefs.allowsContentJavaScript = true

        let config = WKWebViewConfiguration()
        config.defaultWebpagePreferences = prefs
        config.allowsInlineMediaPlayback = true
        // Allow loading mixed content (http resources inside https pages etc.)
        config.preferences.setValue(true, forKey: "allowFileAccessFromFileURLs")

        let webView = WKWebView(frame: .zero, configuration: config)
        webView.allowsBackForwardNavigationGestures = true
        webView.navigationDelegate = context.coordinator
        webView.uiDelegate = context.coordinator
        webView.scrollView.contentInsetAdjustmentBehavior = .automatic
        if #available(iOS 16.4, *) {
            webView.isInspectable = true  // Safari DevTools inspection
        }

        // Custom user agent – mimic Safari so Next.js doesn't serve SSR-only
        webView.customUserAgent = "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"

        // Pull to refresh
        let refresh = UIRefreshControl()
        refresh.addTarget(context.coordinator, action: #selector(Coordinator.handleRefresh(_:)), for: .valueChanged)
        webView.scrollView.refreshControl = refresh

        context.coordinator.webView = webView
        let request = URLRequest(url: url, cachePolicy: .reloadIgnoringLocalCacheData, timeoutInterval: 15)
        webView.load(request)
        return webView
    }

    func updateUIView(_ webView: WKWebView, context: Context) {
        if context.coordinator.lastTrigger != reloadTrigger {
            context.coordinator.lastTrigger = reloadTrigger
            let request = URLRequest(url: url, cachePolicy: .reloadIgnoringLocalCacheData, timeoutInterval: 15)
            webView.load(request)
        }
    }

    class Coordinator: NSObject, WKNavigationDelegate, WKUIDelegate {
        weak var webView: WKWebView?
        var lastTrigger = UUID()

        @objc func handleRefresh(_ sender: UIRefreshControl) {
            webView?.reload()
            DispatchQueue.main.asyncAfter(deadline: .now() + 0.8) {
                sender.endRefreshing()
            }
        }

        // MARK: - Navigation
        func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
            webView.scrollView.refreshControl?.endRefreshing()
        }

        func webView(_ webView: WKWebView, didFail navigation: WKNavigation!, withError error: Error) {
            webView.scrollView.refreshControl?.endRefreshing()
            showError(in: webView, error: error)
        }

        func webView(_ webView: WKWebView, didFailProvisionalNavigation navigation: WKNavigation!, withError error: Error) {
            webView.scrollView.refreshControl?.endRefreshing()
            showError(in: webView, error: error)
        }

        private func showError(in webView: WKWebView, error: Error) {
            let nsError = error as NSError
            // URLErrorCancelled (-999) happens on user-initiated navigation, ignore it
            guard nsError.code != NSURLErrorCancelled else { return }
            let html = """
            <html><body style="font-family:-apple-system;padding:40px;background:#0d0d0d;color:#e8e8e8;text-align:center">
            <div style="font-size:48px;margin-bottom:16px">⚠️</div>
            <h2 style="color:#e05252">Не удалось загрузить</h2>
            <p style="color:#999;font-size:14px">\(nsError.localizedDescription)</p>
            <p style="color:#666;font-size:12px">Убедись, что сервер запущен и доступен по сети</p>
            <button onclick="location.reload()" style="margin-top:24px;background:#7c6ff7;color:#fff;border:none;padding:12px 24px;border-radius:8px;font-size:16px">Повторить</button>
            </body></html>
            """
            webView.loadHTMLString(html, baseURL: nil)
        }

        // MARK: - UI Delegate (JS alerts/confirms/prompts)
        func webView(_ webView: WKWebView, runJavaScriptAlertPanelWithMessage message: String, initiatedByFrame frame: WKFrameInfo, completionHandler: @escaping () -> Void) {
            guard let vc = topVC() else { completionHandler(); return }
            let alert = UIAlertController(title: nil, message: message, preferredStyle: .alert)
            alert.addAction(UIAlertAction(title: "OK", style: .default) { _ in completionHandler() })
            vc.present(alert, animated: true)
        }

        func webView(_ webView: WKWebView, runJavaScriptConfirmPanelWithMessage message: String, initiatedByFrame frame: WKFrameInfo, completionHandler: @escaping (Bool) -> Void) {
            guard let vc = topVC() else { completionHandler(false); return }
            let alert = UIAlertController(title: nil, message: message, preferredStyle: .alert)
            alert.addAction(UIAlertAction(title: "Отмена", style: .cancel) { _ in completionHandler(false) })
            alert.addAction(UIAlertAction(title: "OK", style: .default) { _ in completionHandler(true) })
            vc.present(alert, animated: true)
        }

        private func topVC() -> UIViewController? {
            UIApplication.shared.connectedScenes
                .compactMap { $0 as? UIWindowScene }
                .flatMap { $0.windows }
                .first { $0.isKeyWindow }?.rootViewController
        }
    }
}
