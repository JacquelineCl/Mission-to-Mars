#!/usr/bin/env python
# coding: utf-8

# In[34]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[35]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[3]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[4]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[5]:


slide_elem.find('div', class_='content_title')


# In[6]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[7]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[8]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[9]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[10]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[11]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[12]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[13]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[14]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[15]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[36]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)


# In[37]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

#Start HERE, see hint in challenge for navigating to full image urls
# 3. Write code to retrieve the image urls and titles for each hemisphere.
html = browser.html
hemisphere_results = soup(html, 'html.parser')

for img_location_rel in hemisphere_results:
    #rel location fixed, full image found, how to get this to loop without errors? 
    img_location_rel = hemisphere_results.find('a', class_='itemLink product-item').get('href')
    img_location = f'{url}{img_location_rel}'
    browser.visit(img_location)
    html = browser.html
    result = soup(html, 'html.parser')
    img_src = result.find('img', class_='wide-image').get('src')
    img_url = f'{url}{img_src}'
    title = result.find('h2', class_='title').text

    hemispheres = {
          'img_url' : img_url,
          'title' : title
          }
       
    hemisphere_image_urls.append(hemispheres)
    browser.back()
hemispheres
# maybe add code in app.py to insert this dictionary to MongoDB as a documents e.g. collection.insert_one(post) refrencing # Define database and collection: db = client.nhl_db \n collection = db.articles  


# In[31]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[19]:


# 5. Quit the browser
browser.quit()


# In[20]:


# 6. For reference until the Hemispheres code for steps 2-4 can be fixed.  

hemisphere_image_urls = [{'img_url': 'https://marshemispheres.com/images/full.jpg',
  'title': 'Cerberus Hemisphere Enhanced'},
 {'img_url': 'https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg',
  'title': 'Schiaparelli Hemisphere Enhanced'},
 {'img_url': 'https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg',
  'title': 'Syrtis Major Hemisphere Enhanced'},
 {'img_url': 'https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg',
  'title': 'Valles Marineris Hemisphere Enhanced'}]

hemisphere_image_urls


# In[ ]:





# In[ ]:





# In[ ]:




