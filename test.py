import requests
import time

base_url = 'https://d1zjsiun7w25x0.cloudfront.net'

paths = ['index.html', 'cat.html', 'dog.html', 'bird.html']

def test_cache_behavior(url, wait_time=15):
    for path in paths:
        full_url = f"{url}/{path}"

        initial_response = requests.get(full_url)
        etag = initial_response.headers.get('ETag')
        print(f"Initial request for {path}: {initial_response.status_code}")

        if etag:
            hit_response = requests.get(full_url, headers={'If-None-Match': etag})
            print(f"Cache hit test for {path}: {hit_response.status_code}")
        else:
            print(f"No ETag found for {path}")

        print(f"Waiting {wait_time} seconds for cache to expire, to simulate a cache miss...")
        time.sleep(wait_time)

        print(f"After waiting {wait_time} seconds, making another request to simulate a cache miss.")
        miss_response = requests.get(full_url)
        print(f"Cache miss test for {path}: {miss_response.status_code}")

if __name__ == "__main__":
    test_cache_behavior(base_url)
