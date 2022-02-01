#scrape_mars.py REAL DEAL
#import splinter, BeautifulSoup and chrome driver
from splinter import Browser
from bs4 import BeautifulSoup as soup
#import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

#scrape all function
def scrape_all():
    #print("Scrape All was reached") this is a first step to make sure the app is running correctly

    # set up splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # the goal is to return a json that has all of the necessary data, so that it
    # can be loaded into MongoDB

    # get the info from the news page
    news_title, news_paragraph = scrape_news(browser)

    # build a dictionary using the information from the scrapes
    marsData = {
        "newsTitle": news_title,
        "newsParagraph": news_paragraph
    }

    # stop the webdriver
    browser.quit()

    # display output
    return marsData

# scrape the mars new page
def scrape_news(browser):
    # go to the Mars NASA news site
    # Visit the mars enws site
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Convert the browser html to a soup object
    html = browser.html
    news_soup = soup(html, 'html.parser')

    slide_elem = news_soup.select_one('div.list_text')
    # grabs the title
    news_title = slide_elem.find('div', class_ = 'content_title').get_text()
    # grabs the paragraph
    news_p = slide_elem.find('div', class_ = 'article_teaser_body').get_text()


# scrape the featured image page

# scrape the facts page and get table

# scrape the hemispheres pages


# set up as a flask app
if __name__ == "__main__":
    print(scrape_all()) 