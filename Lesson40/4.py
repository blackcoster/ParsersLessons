from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome('chromedriver',options=options)

driver.get('https://www.kinopoisk.ru/media/article/4007668/')
print(driver.title)

contents = driver.find_elements(By.CLASS_NAME,'stk-reset')
contents_text = [content.text for content in contents]
print(contents_text)

images = driver.find_elements(By.CLASS_NAME,'stk-image')
images_url  = [im.get_attribute('src') for im in images]
print(images_url)

film_page_url = driver.find_element(By.CLASS_NAME,'film-object-card-film-poster__image-wrap')
print(film_page_url.get_attribute('href'))
film_page_url.click()

film_page = driver.find_elements(By.CLASS_NAME,'styles_rowDark__ucbcz')
film_info = [info.text for info in film_page]
for row in film_info:
    print(row.replace('\n',' - '))
