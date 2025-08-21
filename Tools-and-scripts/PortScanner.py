#!/usr/bin/env python3
"""
PortScanner.py
Author: Jessica Taylor
Date: 08/21/2025

Description:
A simple Python script to scan open TCP ports on a target host.
Useful for lab exercises, penetration testing practice, and network reconnaissance.
"""

import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

def scan_port(host, port):
    """
    Attempts to connect to a given host and port.
    Returns True if the port is open, False otherwise.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((host, port))
            if result == 0:
                return port, True
            else:
                return port, False
    except Exception:
        return port, False

def main():
    parser = argparse.ArgumentParser(description="Simple TCP port scanner")
    parser.add_argument("host", help="Target host IP or hostname")
    parser.add
