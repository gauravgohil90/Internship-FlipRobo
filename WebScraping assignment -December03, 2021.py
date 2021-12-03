#!/usr/bin/env python
# coding: utf-8

# Display all header tags in Wikipedia.org

# In[ ]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[ ]:


from bs4 import BeautifulSoup
import requests


# In[ ]:


page = requests.get('https://en.wikipedia.org/wiki/Main_Page')
page


# In[ ]:


wikisoup= BeautifulSoup(page.content)
wikisoup


# In[ ]:


headers= wikisoup.find(id="mp-portals")
headers


# In[ ]:


headers.text


# In[ ]:


headers.text.replace('\n',' ')


# # IMDB Top rated 100 movies

# In[ ]:


imdbpage = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')
imdbpage


# In[ ]:


imdbsoup= BeautifulSoup(imdbpage.content)
imdbsoup


# In[ ]:


titles =[]

for i in imdbsoup.find_all('td', class_="titleColumn"):
    titles.append(i.text.replace('\n',''))

titles


# In[ ]:


release=imdbsoup.find_all('span', class_='secondaryInfo')
release


# In[ ]:


release_year=[]
for i in release:
    release_year.append(i.text)
release_year


# In[ ]:


ratings=imdbsoup.find_all(class_='ratingColumn imdbRating')
ratings


# In[ ]:


avgratings=[]
for i in ratings:
    avgratings.append(i.text.replace('\n',''))
avgratings


# In[ ]:


print(len(titles),len(release_year),len(avgratings))


# In[ ]:


import pandas as pd
imbd=pd.DataFrame({})
imbd['movie_titles']=titles
imbd['release_year']=release_year
imbd['avgratings']=avgratings


# In[ ]:


imbd.head(100)


# # Imdb top rated 100 Indian Movies

# In[ ]:


imdbinpage = requests.get('https://www.imdb.com/india/top-rated-indian-movies/')
imdbinpage


# In[ ]:


imdbinsoup= BeautifulSoup(imdbinpage.content)
imdbinsoup


# In[ ]:


indiatitles =[]

for i in imdbinsoup.find_all('td', class_="titleColumn"):
    indiatitles.append(i.text.replace('\n',''))

indiatitles


# In[ ]:


indrelease=imdbinsoup.find_all('span', class_='secondaryInfo')
indrelease


# In[ ]:


indratings=imdbinsoup.find_all(class_='ratingColumn imdbRating')
indratings


# In[ ]:


avgindratings=[]
for i in indratings:
    avgindratings.append(i.text.replace('\n',''))
avgindratings


# In[ ]:


print(len(indiatitles),len(indrelease),len(avgindratings))


# In[ ]:


import pandas as pd
imbdin=pd.DataFrame({})
imbdin['movie_titles']=indiatitle
imbdin['release_year']=indrelease
imbdin['avgratings']=avgindratings


# In[ ]:


imbd.head(100)


# # Top 10 ODI Teams

# In[106]:


oditeams = requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
oditeams


# In[107]:


oditeamsoup= BeautifulSoup(oditeams.content)
oditeamsoup


# In[110]:


oditeamtitles =[]

for i in oditeamsoup.find_all('span', class_="u-hide-phablet"):
    oditeamtitles.append(i.text.replace('\n',''))

oditeamtitles


# In[116]:


oditeammatch =[]

for i in oditeamsoup.find_all('td', class_="table-body__cell u-center-text"):
    oditeammatch.append(i.text.split('|')[0])

oditeammatch


# In[117]:


oditeamrating =[]

for i in oditeamsoup.find_all('td', class_="table-body__cell u-text-right rating"):
    oditeamrating.append(i.text.split('|')[0])

oditeamrating


# In[118]:


print(len(oditeamtitles),len(oditeammatch),len(oditeamrating))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




