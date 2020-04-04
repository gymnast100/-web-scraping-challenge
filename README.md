# Mars_Mission ![pic](/Mars.png)


The goal of  this assignment was to  build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines were followed :

## Step 1 - Web Scraping

### Initial scraping  was completed using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.
•	Created a Jupyter Notebook file called mission_to_mars.ipynb and used this to complete all of your scraping and analysis       tasks. The following outlines were used to scrape.

### NASA Mars News

  ..* Scraped the NASA Mars News Site and collect the latest News Title and Paragraph Text.
  
  ![pic](/LatestNews.png)
  
  ..* JPL Mars Space Images - Featured Image
  ..* Visited the url for JPL Featured Space Image.
  ..* Used splinter to navigate the site and find the image url for the current Featured Mars Image 
   
   ![pic](/FeaturedImage.png)


### Mars Weather
 
 ![pic](/CurrentWeather.png)

•Visited the Mars Weather twitter account and scraped the latest Mars weather tweet from the page. 

### Mars Facts
 
 ![pic](/MarsFacts.png)
 
•Visited the Mars Facts webpage and used Pandas to scrape the table containing facts about the planet including           Diameter, Mass, etc.
•Used Pandas to convert the data to a HTML table string.

### Mars Hemispheres

 ![pic](/4Hemispheres.png)
 
•Visited the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres.
•Saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere    name. Used a Python dictionary to store the data using the keys img_url and title.
•Appended the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary   for each hemisphere.

## Step 2 - MongoDB and Flask Application
 
• Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the   URLs above.
• Used Pymongo for CRUD applications for the database. Existing documents are overwritten  each time the /scrape url is         visited and new data is obtained.

• Bootstrap was used to structure the HTML template 
 ![pic](/Page1.png)

