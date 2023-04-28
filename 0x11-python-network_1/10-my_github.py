#!/usr/bin/python3
"""Use the GitHub API 2 display a GitHub ID based on given credentials.
Usage: for ./10-my_github.py <GitHub username> <GitHub password>
  - Uses Basic Authentication 2 access the ID.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    rat = requests.get("https://api.github.com/user", auth=auth)
    print(rat.json().get("id"))
