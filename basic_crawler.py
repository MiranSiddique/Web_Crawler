from bs4 import BeautifulSoup
from collections import deque
from urllib.parse import urljoin
from utils import extract_content

import requests

class URLQueue:
    def __init__(self):
        self.queue = deque()

    def put(self, item):
        self.queue.append(item)

    def get(self):
        return self.queue.popleft()

    def is_empty(self):
        return len(self.queue) == 0

def crawl_web(start_url, max_pages, search_pattern):
    visited = set()
    to_visit = URLQueue()
    to_visit.put(start_url)
    pages_crawled = 0
    crawled_data = {}
    links_graph = {}

    while not to_visit.is_empty() and pages_crawled < max_pages:
        url = to_visit.get()
        if url in visited:
            continue

        try:
            response = requests.get(url)
            if response.status_code != 200:
                print(f"Failed to fetch {url}: Status code {response.status_code}")
                continue

            soup = BeautifulSoup(response.content, 'html.parser')
            visited.add(url)
            pages_crawled += 1
            print(f"Crawled: {url}")

            # Extract content and find matches
            match_indices = extract_content(url, search_pattern)
            print(f"Matches found in {url}: {match_indices}")

            # Store matches, links, and page title
            page_title = soup.title.string if soup.title else "No Title"
            crawled_data[url] = {
                "title": page_title,
                "match_indices": match_indices,
                "links": []
            }

            # Collect all links on the page and convert to absolute URLs
            for link in soup.find_all('a', href=True):
                full_url = urljoin(url, link['href'])
                if full_url not in visited:
                    to_visit.put(full_url)
                    crawled_data[url]["links"].append(full_url)  # Save links
                    print(f"Queuing link: {full_url}")

            # Update the links graph
            links_graph[url] = crawled_data[url]["links"]

        except Exception as e:
            print(f"Failed to crawl {url}: {e}")

    return crawled_data, links_graph