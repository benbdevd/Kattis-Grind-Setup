from bs4 import BeautifulSoup
import os
import requests
import threading

OUTPUT_FILE = 'allProblemIDs.txt'

def get_ids(page_num):
     global all_ids
     url = "https://open.kattis.com/problems?page=" + str(page_num)
     page_html = requests.get(url)
     soup = BeautifulSoup(page_html.text, 'html.parser')
     for link in soup.findAll('a', href=True):
          if "/problems/" in link['href'] and link['href'].count("/") == 2:
               all_ids.append(link['href'].split("/")[2])


if not os.path.exists(OUTPUT_FILE):
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
     with open(OUTPUT_FILE, 'w') as f:
          for item in all_ids:
               f.write("%s\n" % item)

with open(OUTPUT_FILE) as problem_list:
     for problem_id in problem_list:
          if os.name is 'nt':
               os.system('new-problem.bat ' + problem_id)
          else:
               os.system('./newprob.sh ' + problem_id)
