# https://www.duquanben.com
# encoding = utf-8
import concurrent
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import os
import traceback

browser = webdriver.PhantomJS()
WAIT = WebDriverWait(browser, 10)
browser.set_window_size(1400, 900)

def search(book_name):
    try:
        print('开始访问读全本站....')
        browser.get("https://www.duquanben.com/")

        input = WAIT.until(EC.presence_of_element_located((By.NAME, "searchkey")))
        submit = WAIT.until(EC.element_to_be_clickable((By.ID, "searchbutton")))

        input.send_keys(book_name)
        submit.click()

        # 跳转到新的窗口
        print('跳转到新窗口')
        all_h = browser.window_handles
        browser.switch_to.window(all_h[1])

        target_book_a = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".listIndexUpdata > ul > a")))
        if(target_book_a):
            print(target_book_a)
            target_book_url = target_book_a.get_attribute('href').replace('xiazai', 'xiaoshuo')
            print(target_book_url)
            get_chapter_list(book_name, target_book_url)
        else:
            print('can find book')
    except TimeoutException:
            traceback.print_exc()
            search(book_name)

def get_chapter_list(book_name, target_book_url):
    if not os.path.exists(book_name):
        os.mkdir(book_name)

    browser.get(target_book_url)
    chapter_list = browser.find_elements(By.CSS_SELECTOR, ".mulu_list > li > a")

    print(f'total chapter: {len(chapter_list)}')
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as exector:
        for chapter in chapter_list:
            title = chapter.text
            chapter_url = chapter.get_attribute('href')
            
            exector.submit(get_chapter, book_name, title, chapter_url)
    print('done')

def get_chapter(book_name, title, chapter_url):

    filename = '%s/%s.txt' % (book_name, str(title))

    if not os.path.exists(filename):
        html = request_page(chapter_url)
        soup = BeautifulSoup(html.replace('&nbsp;', '').replace('<br />', 'br'), 'lxml')

        html_content = soup.find('div', id = 'htmlContent')
        del_div_list = html_content.find_all('div')
        for del_div in del_div_list:
            del_div.clear()

        content = html_content.get_text().strip().replace('br', "\n")

        try:
            with open(filename, 'wb') as f:
                print(f"写入{filename}...")
                f.write(content.encode('utf-8'))
        except:
            traceback.print_exc()
            print(f"写入{filename}异常")
            os.remove(filename)

def request_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            response.encoding = "gbk"
            return response.text
    except requests.RequestException:
        return None


if __name__ == '__main__':
    search('诛仙')