from src.tools.tools import web_search, scrape_url

results = web_search.invoke("what is the latest research on climate change mitigation?")

# results = scrape_url("https://techcrunch.com/category/artificial-intelligence/")

print(results)

