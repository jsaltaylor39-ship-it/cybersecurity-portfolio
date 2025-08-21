#!/usr/bin/env python3
"""
LogParser.py
Author: Jessica Taylor
Date: 08/21/2025

Description:
A simple Python script to parse and analyze log files.
Extracts timestamps, log levels, and messages, and summarizes the results.
"""

import re
import argparse
from collections import Counter

def parse_log(file_path):
    """
    Parses a log file and extracts timestamp, log level, and message.
    """
    log_pattern = re.compile(r'^\[(.*?)\]\s+\[(.*?)\]\s+(.*)$')
    parsed_logs = []

    with open(file_path, 'r') as f:
        for line in f:
            match = log_pattern.match(line.strip())
            if match:
                timestamp, level, message = match.groups()
                parsed_logs.append({
                    'timestamp': timestamp,
                    'level': level,
                    'message': message
                })
    return parsed_logs

def summarize_logs(parsed_logs):
    """
    Prints a summary of log levels and counts.
    """
    levels = [log['level'] for log in parsed_logs]
    count = Counter(levels)
    print("\n=== Log Level Summary ===")
    for level, num in count.items():
        print(f"{level}: {num}")
    print(f"Total entries: {len(pars


