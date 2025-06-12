#!/usr/bin/env python3
"""
System Info Fetcher
- Gets publicly available device name, OS, and timestamp.
- Requires user consent before running.
- Does NOT store, log, or transmit data.
"""

import platform
from datetime import datetime

def get_system_info():
    """Returns non-sensitive system information."""
    return {
        "Device Name": platform.node(),
        "OS": platform.system(),
        "OS Version": platform.release(),
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def main():
    print("\n" + "=" * 40)
    print("SYSTEM INFO FETCHER (PUBLIC DATA ONLY)")
    print("=" * 40)
    print("[!] This script collects:")
    print("    - Device name (e.g., 'MyPC')")
    print("    - OS (e.g., 'Windows', 'Linux')")
    print("    - OS version (e.g., '10.0.19041')")
    print("    - Current timestamp\n")

    # Explicit user consent
    consent = input("Continue? (yes/no): ").strip().lower()
    if consent != "yes":
        print("\n[!] Aborted by user.")
        return

    # Fetch and display info
    info = get_system_info()
    print("\n" + "-" * 40)
    print("COLLECTED DATA (NON-SENSITIVE):")
    print("-" * 40)
    for key, value in info.items():
        print(f"{key}: {value}")
    print("-" * 40 + "\n")

if __name__ == "__main__":
    main()
