import requests

from bs4 import BeautifulSoup


def parse_url(url):
    list_of_tasks = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'html.parser')
    div = soup.find_all("div", {"class": "item-title"})
    for tag in div:
        a = tag.find_all("a")
        list_of_tasks.append(a[0].get_text())
    return list_of_tasks
