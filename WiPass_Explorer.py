import subprocess
import re
import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget,
    QTableWidgetItem, QFileDialog, QMessageBox, QHeaderView
)
from PySide6.QtGui import QIcon, QGuiApplication

def get_wifi_profiles():
    profiles_output = subprocess.check_output('netsh wlan show profiles', shell=True).decode('utf-8')
    profiles = re.findall(r'All User Profile\s*:\s*(.*)', profiles_output)
    return profiles

def get_wifi_password(profile):
    try:
        profile_info_output = subprocess.check_output(f'netsh wlan show profile "{profile}" key=clear', shell=True).decode('utf-8')
        password = re.findall(r'Key Content\s*:\s*(.*)', profile_info_output)
        return password[0] if password else None
    except subprocess.CalledProcessError:
        return None

class WiPassExplorer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WiPass Explorer")
        self.setGeometry(300, 300, 600, 400)
        # self.setWindowIcon(QIcon("icon.png"))

        layout = QVBoxLayout()

        self.show_button = QPushButton("Show Wi-Fi Profiles")
        self.show_button.clicked.connect(self.show_profiles)
        layout.addWidget(self.show_button)

        self.save_button = QPushButton("Save to File")
        self.save_button.setEnabled(False)
        self.save_button.clicked.connect(self.save_to_file)
        layout.addWidget(self.save_button)

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(["Network Name", "Password"])
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget.cellDoubleClicked.connect(self.copy_password_to_clipboard)
        layout.addWidget(self.table_widget)

        self.setLayout(layout)

    def show_profiles(self):
        profiles = get_wifi_profiles()
        if not profiles:
            QMessageBox.information(self, "No Wi-Fi profiles", "No Wi-Fi profiles found.")
            return

        self.profiles_with_passwords = []
        self.table_widget.setRowCount(len(profiles))
        for row, profile in enumerate(profiles):
            password = get_wifi_password(profile)
            self.profiles_with_passwords.append((profile.strip(), password.strip() if password else "No password found"))
            self.table_widget.setItem(row, 0, QTableWidgetItem(profile.strip()))
            self.table_widget.setItem(row, 1, QTableWidgetItem(password.strip() if password else "No password found"))

        self.save_button.setEnabled(True)

    def save_to_file(self):
        file_path = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt)")[0]
        if file_path:
            with open(file_path, 'w') as file:
                for profile, password in self.profiles_with_passwords:
                    file.write(f"Network Name: {profile}\nPassword: {password}\n\n")
            QMessageBox.information(self, "Success", "Wi-Fi profiles saved successfully!")

    def copy_password_to_clipboard(self, row, column):
        if column == 1:
            password_item = self.table_widget.item(row, column)
            if password_item:
                password = password_item.text()
                clipboard = QGuiApplication.clipboard()
                clipboard.setText(password)
                QMessageBox.information(self, "Copied to Clipboard", f"Password copied to clipboard:\n{password}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WiPassExplorer()
    window.show()
    sys.exit(app.exec())
