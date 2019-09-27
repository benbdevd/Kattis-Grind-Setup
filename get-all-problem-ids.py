from bs4 import BeautifulSoup
import requests
import threading

def get_ids(page_num):
     global all_ids
     url = "https://open.kattis.com/problems?page=" + str(page_num)
     page_html = requests.get(url)
     soup = BeautifulSoup(page_html.text, 'html.parser')
     for link in soup.findAll('a', href=True):
          if "/problems/" in link['href'] and link['href'].count("/") == 2:
               all_ids.append(link['href'].split("/")[2])
     
     
all_ids = []
all_threads = []
for i in range(25):
     print("Starting page: ", i)
     t = threading.Thread(target=get_ids, args=(i,))
     t.start()
     all_threads.append(t)
     
for thread in all_threads:
     thread.join()

print("All pages read.")
all_ids.sort()
with open('allProblemIDs.txt', 'w') as f:
    for item in all_ids:
        f.write("%s\n" % item)
