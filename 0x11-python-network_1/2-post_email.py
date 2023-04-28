#!/usr/bin/python3
"""Sends a POST request to a given URL with an email.
Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response to console.
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    custom_url = sys.argv[1]
    custom_value = {"email": sys.argv[2]}
    custom_data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(custom_url, custom_data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
