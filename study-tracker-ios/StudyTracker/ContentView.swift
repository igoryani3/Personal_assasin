import SwiftUI

struct ContentView: View {
    @AppStorage("serverURL") private var serverURL: String = ""
    @State private var showSettings = false
    @State private var reloadTrigger = UUID()

    var body: some View {
        if serverURL.isEmpty {
            SetupView()
        } else {
            NavigationView {
                WebView(url: URL(string: serverURL)!, reloadTrigger: reloadTrigger)
                    .ignoresSafeArea(edges: .bottom)
                    .navigationTitle("StudyTracker")
                    .navigationBarTitleDisplayMode(.inline)
                    .toolbar {
                        ToolbarItem(placement: .navigationBarTrailing) {
                            Button(action: { showSettings = true }) {
                                Image(systemName: "gear")
                                    .foregroundColor(.primary)
                            }
                        }
                        ToolbarItem(placement: .navigationBarLeading) {
                            Button(action: { reloadTrigger = UUID() }) {
                                Image(systemName: "arrow.clockwise")
                                    .foregroundColor(.primary)
                            }
                        }
                    }
            }
            .navigationViewStyle(.stack)
            .sheet(isPresented: $showSettings) {
                SettingsView()
            }
        }
    }
}
