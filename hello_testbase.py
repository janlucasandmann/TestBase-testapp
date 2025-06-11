#!/usr/bin/env python3
"""
A simple Python script that prints a greeting from TestBase Agent
along with the current timestamp.
"""

from datetime import datetime

def main():
    """Main function that prints the greeting with timestamp."""
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    
    print("Hello from TestBase Agent!")
    print(f"Current timestamp: {formatted_time}")

if __name__ == "__main__":
    main()
