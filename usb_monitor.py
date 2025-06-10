import pyudev
import json
import time

def load_known_devices(file_path='known_devices.json'):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"[!] Error loading known devices: {e}")
        return []

def check_device(device, known_devices):
    vendor_id = device.get('ID_VENDOR_ID')
    product_id = device.get('ID_MODEL_ID')

    if not vendor_id or not product_id:
        return False

    for entry in known_devices:
        if entry['vendor_id'].lower() == vendor_id.lower() and entry['product_id'].lower() == product_id.lower():
            return True
    return False

def monitor_usb():
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by('usb')

    known_devices = load_known_devices()

    print("[*] USB Monitor is running... Press Ctrl+C to exit.")
    for device in monitor:
        if device.action == 'add':
            print(f"[+] USB Device Inserted: {device}")
            if check_device(device, known_devices):
                print("[!] ⚠️  ALERT: Known malicious USB device detected!")
            else:
                print("[*] USB device appears safe.")

if __name__ == "__main__":
    try:
        monitor_usb()
    except KeyboardInterrupt:
        print("\n[+] Exiting USB Monitor...")
