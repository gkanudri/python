from bs4 import BeautifulSoup
import requests

search = input("Enter serach term")
params = {"q":search}
r = requests.get("http://www.bing.com/search", params=params)

#print(r.text)
soup = BeautifulSoup(r.text, "html.parser")

results = soup.find("ol", {"id":"b_results"})
links = results.findAll("li", {"class": "b_algo"})
for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]
    print(item_text)
    print(item_href)
#print(results)