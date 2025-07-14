# main.py
import sys
import os
from scraper import scrape_comments_from_user_page
from persona import build_prompt, call_groq, clean_persona_output

def extract_username(url):
    return url.strip("/").split("/")[-2]  

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <reddit_comments_url>")
        return

    url = sys.argv[1]
    username = extract_username(url)

    print(f"[+] Scraping comments from {url}")
    comments = scrape_comments_from_user_page(url)

    print(f"[+] Generating prompt for {username}")
    prompt = build_prompt(username, comments)

    print(f"[+] Calling Groq LLM...")
    persona = call_groq(prompt)
    persona_clean = clean_persona_output(persona)


    os.makedirs("output", exist_ok=True)
    with open(f"output/{username}_persona.txt", "w") as f:
        f.write(persona)

    print(f"[✓] Persona saved to output/{username}_persona.txt")

if __name__ == "__main__":
    main()
