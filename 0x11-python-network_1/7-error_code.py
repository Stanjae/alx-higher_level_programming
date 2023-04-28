#!/usr/bin/python3
"""Send request 2 a given URL & display de response content.
Usage: For ./7-error_code.py <URL>
  - Handles HTTP errors.
"""
import sys
import requests


if __name__ == "__main__":
    custom_url = sys.argv[1]

    custom_response = requests.get(custom_url)
    if custom_response.status_code >= 400:
        print("Error code: {}".format(custom_response.status_code))
    else:
        print(custom_response.text)
