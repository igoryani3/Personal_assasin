# Study Tracker iOS App

Unsigned iOS app for TrollStore (iOS 16+).
Wraps the Study Tracker web interface in a native WKWebView.

## 📦 Installation

1. Transfer `build/StudyTracker.ipa` to your iPhone (AirDrop, iCloud Drive, etc).
2. Open **TrollStore** on your iPhone.
3. Tap **+** -> **Install IPA File**.
4. Select `StudyTracker.ipa`.
5. Open the app and enter your VPS URL (e.g. `https://my-vps.com` or `http://192.168.1.X:3000`).

## 🛠 Rebuilding

If you change the Swift code:

```bash
# 1. Generate Xcode project (updates file references)
python3 generate_project.py

# 2. Build and package IPA
bash build_ipa.sh
```

## ⚙️ Configuration

- **URL**: stored in `UserDefaults`. To change, tap the ⚙️ gear icon in the app toolbar.
- **Networking**: `AllowsArbitraryLoads = true` enabled for HTTP support.
