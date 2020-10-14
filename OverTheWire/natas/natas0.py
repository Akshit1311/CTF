#!/usr/bin/env python
import requests
import re

username = "natas0"
# username = input("Enter Username: ")
password = username
# password = input("Enter Password: ")


url = f"http://{username}.natas.labs.overthewire.org"

response = requests.get(url, auth=(username, password))
content = response.text

store = re.findall(
    f"<!--The password for natas1 is (.*) -->", content)[0]
print(store)

# print(content)
