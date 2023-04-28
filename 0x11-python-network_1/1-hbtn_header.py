#!/usr/bin/python3
"""Displays de header variable of a request to a given custom URL.
Usage: for ./1-hbtn_header.py
"""
import sys
import urllib.request


if __name__ == "__main__":
    custom_url = sys.argv[1]

    request = urllib.request.Request(custom_url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
