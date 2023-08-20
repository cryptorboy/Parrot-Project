import webbrowser

popular_websites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "wikipedia": "https://www.wikipedia.org",
        "amazon": "https://www.amazon.com",
    }
search_engines = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "bing": "https://www.bing.com",
    }


def open_url(url):
        webbrowser.open(url)
        chrome_path = r"open -a /Applications/Google\ Chrome.app %s"
        webbrowser.get(chrome_path).open(url)   


def search(search_query, search_engine):
    try:
        open_url(f"{search_engines[search_engine]}/search?q={search_query}")
    except IndexError:
        open_url(f"https://www.google.com/search?q={search_query}")

if __name__ == "__main__":
     website = "goa"
