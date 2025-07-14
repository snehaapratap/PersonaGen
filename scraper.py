# scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_comments_from_user_page(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch page: {url}")

    soup = BeautifulSoup(response.text, 'html.parser')
    comment_blocks = soup.find_all("div", {"data-test-id": "comment"})

    comments = []
    for block in comment_blocks:
        body = block.get_text(separator="\n").strip()
        if body:
            comments.append(body)
    
    return comments[:50]  # Limit for LLM input
