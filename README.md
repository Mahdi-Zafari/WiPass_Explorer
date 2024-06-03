# WiPass Explorer

WiPass Explorer is a graphical tool for managing Wi-Fi profiles and their passwords on your system. This application, built using `PySide6`, enables you to view saved Wi-Fi profiles, copy their passwords to the clipboard, and save the information to a file.

## Version

WiPass Explorer v1.0

## Features

- Display saved Wi-Fi profiles
- Show passwords for Wi-Fi profiles
- Copy passwords to the clipboard with a double-click
- Save profile and password information to a text file

## Prerequisites

- Python 3.x
- `PySide6`

## Installation

To install the required dependencies, use the following command:

```sh
pip install PySide6
```

## Usage
- Download or Clone the Project: Obtain the project code by either downloading it directly or cloning the repository.

- Icon File Placement: Place an icon file named icon.png in the project directory. Alternatively, you can specify your desired icon path directly in the code.

- Run the Application: Execute the WiPass_Explorer.py file using the following command in your terminal:
sh
Copy code

```pip
python WiPass_Explorer.py
```

## How to Use
- Click the "Show Wi-Fi Profiles" button to display the saved Wi-Fi profiles along with their passwords.
- Double-click on any cell within the password column to copy the password to the clipboard.
- Utilize the "Save to File" button to store the profile and password information in a text file.

## Security
- Please exercise caution while using this tool as it reveals Wi-Fi passwords. Ensure that you have the necessary administrative privileges before running the application.

## Contributing
Contributions are welcome! Feel free to submit pull requests and report issues.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

# WiPass Explorer CLI

WiPass Explorer CLI is a command-line interface (CLI) tool that provides similar functionality to the graphical WiPass Explorer but in a text-based format.

### Usage

To use WiPass Explorer CLI, follow these steps:

1. Open your terminal or command prompt.
2. Navigate to the directory where WiPass_Explorer_CLI.py is located.
3. Run the script using Python:

```
python WiPass_Explorer_CLI.py
```

## Features
Display saved Wi-Fi profiles
Show passwords for Wi-Fi profiles
Save profile and password information to a text file
Command Line Options
WiPass Explorer CLI supports the following command-line options:

-h, --help: Display help information about the CLI tool.
-p, --profile <profile_name>: Specify a specific Wi-Fi profile to retrieve information for.
-s, --save <file_path>: Save the profile and password information to a specified text file.
Examples
Here are some examples of how to use WiPass Explorer CLI:

Display all saved Wi-Fi profiles:
```
python WiPass_Explorer_CLI.py
```

Display information for a specific Wi-Fi profile named "MyWiFi":
```
python WiPass_Explorer_CLI.py -p MyWiFi
```

Save Wi-Fi profile information to a text file named "wifi_profiles.txt":
```
python WiPass_Explorer_CLI.py -s wifi_profiles.txt
``

Display help information:
```
python WiPass_Explorer_CLI.py -h
```

## Security
- WiPass Explorer CLI operates in a similar manner to the graphical version, revealing Wi-Fi passwords. As such, it should be used with - caution and with appropriate administrative privileges.

Feel free to add this section to your README.md file and customize it as needed!