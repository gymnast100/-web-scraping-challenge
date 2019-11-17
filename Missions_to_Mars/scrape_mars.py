import requests
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs

# the  final scrape all function to run in the app.py file 
def scrape_info():
   
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    browser =  Browser("chrome", **executable_path, headless=False)
    news_title = scrape_title(browser)
    news_para =  scrape_para(browser)
    featured_img_url = scrape_featuredimage(browser)
    mars_weather = scrape_marsweather(browser)
    html_table_string =  scrape_htmltablestring()
    hemisphere_image_urls =  scrape_hemisphereimageurls(browser)
    

    mars_data = {
        "news_title": news_title ,
         "news_para": news_para,
         "featured_img_url":featured_img_url  ,
         "mars_weather" : mars_weather ,
         "html_table_string" : html_table_string ,
         "hemisphere_image_urls" : hemisphere_image_urls
    }
    return mars_data

#  function to scrape news title 
def scrape_title(browser):

    url_1 = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url_1)
    html_1= browser.html
    soup_1 = bs(html_1, "html.parser")
    news_title = news_title = soup_1.find("div" , class_="content_title").text
    return news_title

#  function to scrape news paagraph
def scrape_para(browser):

    url_1 ="https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url_1)
    html_1= browser.html
    soup_1 = bs(html_1, "html.parser")
    news_para = news_para = soup_1.find("div" , class_="rollover_description_inner").text
    return news_para

#  function to scrape featured image
def scrape_featuredimage(browser):

    url_2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url_2)
    html_2 = browser.html
    soup_2 = bs(html_2, 'html.parser')
    results = soup_2.find_all('a',class_="button fancybox" )

    for result in results:
        try:
            url = result['data-fancybox-href']
            featured_img_url=('https://www.jpl.nasa.gov'+ url )
        except :
            pass
    return featured_img_url

#  function to scrape twitter tweet
def scrape_marsweather(browser):

    url_3 = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url_3)
    html_3 = browser.html
    soup_3 = bs(html_3, 'html.parser')
    weather = soup_3.find('div', class_="js-tweet-text-container")
    weather_info = weather.p.text
    splitweather = weather_info.split('pic.twitter.com/')
    mars_weather = splitweather[0]
    return mars_weather

#  function to scrape facts table 
def scrape_htmltablestring():

    url_4 = "https://space-facts.com/mars/"
    tables = pd.read_html(url_4)
    df = tables[0]
    df.columns = ["description","value"]
    mars_table = df.set_index("description")
    html_table = mars_table.to_html()
    html_table_string = html_table.replace("\n","")
    html_table_string = html_table 
    return html_table_string

#  function to scrape mars hemisphere urls and image titles
def scrape_hemisphereimageurls(browser):

    cerberus_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    schiaparelli_url  ='https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    syrtis_url ='https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    valles_url='https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'

    hemisphere_image_urls=[]
    mars_hemispheres_urls  = [cerberus_url, schiaparelli_url, syrtis_url, valles_url]
    for hemisphere_url in mars_hemispheres_urls:
        browser.visit(hemisphere_url)
        html = browser.html
        hemisphere_soup = bs( html , 'lxml')

        # hemisphere =  requests.get(hemisphere_url)
        # hemisphere_soup = bs(hemisphere.text, "lxml")
        title = hemisphere_soup.find('h2', class_="title").text
        hem_results = hemisphere_soup.find_all('div', class_="wide-image-wrapper")
        for item in hem_results:
           
                if (item.li):
                    if(item.li.a):
                        url = (item.li.a)
                        img_url = (url.get("href"))
                        post = {"title":title , "img_url":img_url}
                        hemisphere_image_urls.append(post)
    
    
    
    return hemisphere_image_urls

 
