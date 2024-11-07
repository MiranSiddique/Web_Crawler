from basic_crawler import crawl_web
from page_rank import calculate_pagerank
from utils import save_data
import os

def main():
    # Ensure the "data" directory exists
    if not os.path.exists("data"):
        os.makedirs("data")

    START_URL = "https://en.wikipedia.org/wiki/India"  # Initial URL
    MAX_PAGES = 20  # Maximum number of pages to crawl
    SEARCH_PATTERN = "Hindi"  # Pattern to search for

    crawled_data, links_graph = crawl_web(START_URL, MAX_PAGES, SEARCH_PATTERN)
    pagerank_scores = calculate_pagerank(links_graph)

    # Print the top 5 pages by PageRank score
    top_pages = sorted(pagerank_scores.items(), key=lambda x: x[1], reverse=True)[:5]
    print("Top 5 pages by PageRank:")
    for url, score in top_pages:
        if url in crawled_data and 'title' in crawled_data[url]:
            print(f"{crawled_data[url]['title']}: {score:.4f}")
        else:
            print(f"{url}: {score:.4f}")

    # Print the URLs where the search pattern was found
    print("\nURLs containing the search pattern:")
    for url, page_data in crawled_data.items():
        if page_data["match_indices"]:
            print(f"{url} - {len(page_data['match_indices'])} matches")

    # Save the crawled data and PageRank scores to JSON files
    save_data(crawled_data, pagerank_scores)

if __name__ == "__main__":
    main()

