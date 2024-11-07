import requests
import re
import json

def extract_content(url, search_pattern):
    try:
        response = requests.get(url)
        content = response.text
        matches = [match.start() for match in re.finditer(search_pattern, content)]
        return matches
    except Exception as e:
        print(f"Error extracting from {url}: {e}")
        return []

def save_data(crawled_data, pagerank_scores):
    # Save the crawled data to a JSON file
    with open('data/crawled_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(crawled_data, json_file, ensure_ascii=False, indent=4)

    # Save the PageRank scores to a separate JSON file
    with open('data/pagerank_scores.json', 'w', encoding='utf-8') as json_file:
        json.dump(pagerank_scores, json_file, ensure_ascii=False, indent=4)

    print("Crawling completed. Data saved in data/crawled_data.json and data/pagerank_scores.json.")
