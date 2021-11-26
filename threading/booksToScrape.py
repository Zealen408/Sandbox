from bs4 import BeautifulSoup
import requests
import queue, threading
import time


productUrl = queue.Queue()
lock = threading.Lock()

def getProductLinks():
    mainURL = 'https://books.toscrape.com/catalogue/'
    url = f'{mainURL}/page-1.html' # start url
    while url:
        response = requests.get(url)
        print(response.status_code)
        soup = BeautifulSoup(response.content, 'lxml')
        try:
            follow = soup.find('li', class_='next')
            nextLink = f'{mainURL}{follow.find("a")["href"]}'
            url = nextLink
            print(url)
        except:
            url = None
        finally:
            products = soup.find_all('article', class_='product_pod')
            with lock:
                for product in products:
                    productUrl.put(f"{mainURL}{product.find('a')['href']}")

def getData():
    while not productUrl.empty():
        url = productUrl.get()
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')
        title = soup.find('li', class_='active')
        category = title.find_previous_sibling().find('a').get_text()
        new_line = [category, title.get_text(), url]
        with lock:
            with open('data.txt', 'a') as f:
                f.write(f'{new_line}')
                f.write('\n')


        

if __name__ == "__main__":
    
    thread_list = []
    start = time.time()

    catalogueThread = threading.Thread(target=getProductLinks, daemon=True)
    catalogueThread.start()
    
    time.sleep(1.5) #Needs a moment to seed the product links queue

    for t in range(10):
        t = threading.Thread(target=getData)
        thread_list.append(t)
        t.start()

    for thread in thread_list:
        thread.join()


    end = time.time()
    print(f"time: {end - start}")
