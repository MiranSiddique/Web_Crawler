# Web Crawler

This is a Python-based web crawler designed to extract and analyze content from a set of web pages.

## Features

- **Web Crawling**: Starts from a given URL and follows links on pages, visiting and extracting data from a specified number of pages.
- **Content Extraction**: Searches for a given pattern within the HTML content of each page and records the character indices where matches are found.
- **Link Graph Creation**: Builds a graph-like structure of the visited pages and the links between them.
- **PageRank Calculation**: Uses the NetworkX library to compute the PageRank scores for the visited pages, helping identify the most important or influential pages.
- **Data Storage**: Saves the crawled data and computed PageRank scores to JSON files for further analysis or use.

## Project Structure

The project is organized into the following files:

- `main.py`: The entry point of the application, orchestrating the overall program flow.
- `basic_crawler.py`: Contains the `crawl_web()` function, handling web crawling and data collection.
- `page_rank.py`: Contains the `calculate_pagerank()` function, handling the PageRank computation.
- `utils.py`: Contains utility functions used across the project, such as `extract_content()` and `save_data()`.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/username/web-crawler.git

2. **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python -m venv .venv
    .venv\Scripts\activate  # On Windows
    source .venv/bin/activate  # On macOS/Linux

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt

## Usage
1. **Open the main.py file and set the following variables:**

- START_URL: The initial URL to start crawling from.
- MAX_PAGES: The maximum number of pages to crawl.
- SEARCH_PATTERN: The pattern to search for within the page content.

2. **Run the application:**

3. **The crawled data and PageRank scores will be saved in the data directory as crawled_data.json and pagerank_scores.json, respectively.**

