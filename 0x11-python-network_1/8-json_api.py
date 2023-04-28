#!/usr/bin/python3
"""Makes POST request to http://0.0.0.0:5000/search_user with a given letter.
Usage: For ./8-json_api.py <letter>
  - The letter is sent as the value of the variable `q`.
  - If null letter is provided, send `q=""`.
"""
import sys
import requests


if __name__ == "__main__":
    custom_letter = "" if len(sys.argv) == 1 else sys.argv[1]
    custom_payload = {"q": custom_letter}

    custom_r = requests.post("http://0.0.0.0:5000/search_user", data=custom_payload)
    try:
        custom_response = custom_r.json()
        if custom_response == {}:
            print("No results Found")
        else:
            print("[{}] {}".format(custom_response.get("id"), custom_response.get("name")))
    except ValueError:
        print("Not a valid JSON Object")
