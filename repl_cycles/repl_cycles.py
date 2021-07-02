from bs4 import BeautifulSoup 
import requests,string
def get_cycles(name):
  url = "https://replit.com/@" + name
  req = requests.get(url)
  soup = BeautifulSoup(req.content,features="html5lib")
  results = soup.find("span",class_="jsx-1979011775")
  results = results.text
  results = results.replace("(","")
  results = results.replace(")","")
  return results

