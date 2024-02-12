from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO

search = input("Enter Search Criteria : ")
param = {"q": search}
r = requests.get("http://www.bing.com/images/search", params=param)

soup = BeautifulSoup(r.text, "html.parser")
links = soup.findAll("a", {"class": "iusc"})
i = 0
for item in links:
    #print(item)
    imageItems = item.findAll("img", {"data-src" : True})
    for imgItem in imageItems:
        #print(imgItem)
        i = i + 1
        #print(imgItem['data-src'])
        image_obj = requests.get(imgItem['data-src'])
        title = imgItem['data-src'].split("/")[-1]
        print(title)
        img = Image.open(BytesIO(image_obj.content))
        img.save("./Images/" + "MyImage" + str(i) + ".jpeg", img.format)
        
        
    #print(imageItem['alt'])
    #print(imageItem.attr["alt"])
    print("\n");