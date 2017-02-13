import urllib.request
import urllib.parse
import json

p = ''
with open('dict.txt', 'r') as file:
    k = file.read()
    p = json.loads(k)

input()
