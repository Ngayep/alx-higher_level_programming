#!/usr/bin/python3

""" script that takes in a URL and an email,
sends a POST request to the passed URL
with the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""

import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))
