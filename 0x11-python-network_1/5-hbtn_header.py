#!/usr/bin/python3
"""Displays de X-Request-Id header variable of a request to a certain URL.
Usage: For ./5-hbtn_header.py <URL>
"""
import sys
import requests


if __name__ == "__main__":
    custom_url = sys.argv[1]

    rat = requests.get(custom_url)
    print(rat.headers.get("X-Request-Id"))
