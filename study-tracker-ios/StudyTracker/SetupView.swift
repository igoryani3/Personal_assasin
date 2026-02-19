import SwiftUI

struct SetupView: View {
    @AppStorage("serverURL") private var serverURL: String = ""
    @State private var inputURL: String = "https://"
    @State private var showError = false

    var body: some View {
        VStack(spacing: 32) {
            Spacer()

            VStack(spacing: 12) {
                Image(systemName: "graduationcap.fill")
                    .font(.system(size: 64))
                    .foregroundColor(.purple)

                Text("StudyTracker")
                    .font(.largeTitle.bold())

                Text("Введи адрес сервера, на котором\nзапущено приложение")
                    .font(.subheadline)
                    .foregroundColor(.secondary)
                    .multilineTextAlignment(.center)
            }

            VStack(alignment: .leading, spacing: 8) {
                Text("URL СЕРВЕРА")
                    .font(.caption.bold())
                    .foregroundColor(.secondary)
                    .tracking(1)

                TextField("https://your-vps.com", text: $inputURL)
                    .textFieldStyle(.roundedBorder)
                    .autocapitalization(.none)
                    .disableAutocorrection(true)
                    .keyboardType(.URL)
                    .font(.body.monospaced())

                if showError {
                    Text("Введи корректный URL (http:// или https://)")
                        .font(.caption)
                        .foregroundColor(.red)
                }
            }
            .padding(.horizontal, 32)

            Button(action: connect) {
                HStack {
                    Text("Подключиться")
                        .fontWeight(.semibold)
                    Image(systemName: "arrow.right")
                }
                .frame(maxWidth: .infinity)
                .padding()
                .background(Color.purple)
                .foregroundColor(.white)
                .cornerRadius(12)
            }
            .padding(.horizontal, 32)

            Spacer()
        }
        .background(Color(.systemBackground))
    }

    private func connect() {
        let trimmed = inputURL.trimmingCharacters(in: .whitespacesAndNewlines)
        guard !trimmed.isEmpty,
              let url = URL(string: trimmed),
              (url.scheme == "http" || url.scheme == "https") else {
            showError = true
            return
        }
        showError = false
        serverURL = trimmed
    }
}
