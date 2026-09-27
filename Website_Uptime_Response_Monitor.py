import requests
import time


SITES_TO_CHECK = [
    "https://www.google.com",
    "https://www.github.com",
    "https://httpbin.org/status/404", 
    "https://invalid-url-that-doesnt-exist.org" 
]

def check_site(url):
    try:
        
        start_time = time.time()
        
         
        response = requests.get(url, timeout=5)
        
         
        latency = round(time.time() - start_time, 2)
        status_code = response.status_code
        
         
        if 200 <= status_code < 300:
            print(f"[ONLINE]  {url} | Status: {status_code} | Latency: {latency}s")
        else:
            print(f"[WARNING] {url} | Status: {status_code} | Latency: {latency}s")

    except requests.exceptions.RequestException:
         
        print(f"[OFFLINE] {url} | Unable to connect!")

print("--- Starting Website Uptime Check ---")
for site in SITES_TO_CHECK:
    check_site(site)