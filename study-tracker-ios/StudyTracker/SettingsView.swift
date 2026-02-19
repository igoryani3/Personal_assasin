import SwiftUI

struct SettingsView: View {
    @AppStorage("serverURL") private var serverURL: String = ""
    @State private var inputURL: String = ""
    @State private var showError = false
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        NavigationView {
            Form {
                Section {
                    TextField("https://your-vps.com", text: $inputURL)
                        .autocapitalization(.none)
                        .disableAutocorrection(true)
                        .keyboardType(.URL)
                        .font(.body.monospaced())

                    if showError {
                        Text("Введи корректный URL")
                            .font(.caption)
                            .foregroundColor(.red)
                    }
                } header: {
                    Text("Адрес сервера")
                } footer: {
                    Text("Текущий: \(serverURL)")
                        .font(.caption)
                        .foregroundColor(.secondary)
                }

                Section {
                    Button(role: .destructive) {
                        serverURL = ""
                        dismiss()
                    } label: {
                        Label("Сбросить настройки", systemImage: "trash")
                    }
                }
            }
            .navigationTitle("Настройки")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .navigationBarLeading) {
                    Button("Отмена") { dismiss() }
                }
                ToolbarItem(placement: .navigationBarTrailing) {
                    Button("Сохранить") { save() }
                        .fontWeight(.semibold)
                }
            }
            .onAppear { inputURL = serverURL }
        }
    }

    private func save() {
        let trimmed = inputURL.trimmingCharacters(in: .whitespacesAndNewlines)
        guard !trimmed.isEmpty,
              let url = URL(string: trimmed),
              (url.scheme == "http" || url.scheme == "https") else {
            showError = true
            return
        }
        serverURL = trimmed
        dismiss()
    }
}
