# USB Monitor 🔌🛡️

A simple Python tool to monitor USB device insertions on Linux systems and detect known malicious USB devices.

## Features
- Detects USB insertion events in real-time
- Matches against a list of known malicious vendor/product IDs
- Logs alerts to the terminal

## Requirements
- Python 3.x
- Linux OS
- udev subsystem (used by pyudev)

## Installation

```bash
git clone https://github.com/yourusername/usb-monitor.git
cd usb-monitor
pip install -r requirements.txt
