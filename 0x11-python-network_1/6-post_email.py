#!/usr/bin/python3
"""Sends POST request to a URL with a provided email.
Usage: For ./6-post_email.py <URL> <email>
  - Display the body of de response.
"""
import sys
import requests


if __name__ == "__main__":
    custom_url = sys.argv[1]
    custom_value = {"email": sys.argv[2]}

    rat = requests.post(custom_url, data=custom_value)
    print(rat.text)
