#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a given letter.

Usage: ./8-json_api.py <letter>
  - The letter is sent as the value of the variable `q`.
  - If no letter is provided, sends `q=""`.
"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    data = {"q": letter}
    response = requests.post(url, data=data)

    try:
        response_data = response.json()

        if response_data:
            print("[{}] {}".format(response_data["id"], response_data["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
