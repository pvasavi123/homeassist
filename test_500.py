import urllib.request
import urllib.error
import re

urls = ['http://127.0.0.1:8000/api/services/items/', 'http://127.0.0.1:8000/api/users/profile/']
for url in urls:
    try:
        req = urllib.request.Request(url)
        res = urllib.request.urlopen(req)
        print(f"Success: {url}")
    except urllib.error.HTTPError as e:
        html = e.read().decode('utf-8', errors='ignore')
        title = re.search(r'<title>(.*?)</title>', html, re.I | re.S)
        if title:
            print(f"Error {e.code} on {url}: {title.group(1).strip()}")
        exc = re.search(r'<div class="exception_value">(.*?)</div>', html, re.I | re.S)
        if exc:
            print(f"Exception: {exc.group(1).strip()}")
