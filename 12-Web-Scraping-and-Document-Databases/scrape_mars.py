{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup as bs\n",
    "import requests\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "# @NOTE: Replace the path with your actual path to the chromedriver\n",
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit https://mars.nasa.gov/news/\n",
    "url = \"https://mars.nasa.gov/news/\"\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Scrape page into Soup\n",
    "html = browser.html\n",
    "soup = bs(html, \"html.parser\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "# Get the News Titles\n",
    "titles = soup.find_all('div', class_='content_title')\n",
    "paragraphs = soup.find_all('div', class_='article_teaser_body')\n",
    "\n",
    "\n",
    "for title in titles:\n",
    "        print('Titles:', '-------------')\n",
    "        print(title.text)\n",
    "for paragraph in paragraphs:\n",
    "        print('Text:')\n",
    "        print(paragraph.text)\n",
    "\n",
    "browser.find_link_by_text('More').last.click()\n",
    "\n",
    " "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "url = \"https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars\"\n",
    "browser.visit(url)\n",
    "html = browser.html\n",
    "soup = bs(html, \"html.parser\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "path =\"https://www.jpl.nasa.gov\"\n",
    "#relative_image_path = soup.find_all('div', class_='image_and_description_container')\n",
    "relative_image_paths = [img['src'] for img in soup.find_all('img')]\n",
    "#print(relative_image_path)\n",
    "\n",
    "for relative_image_path in relative_image_paths:\n",
    "        \n",
    "        featured_image_url = path + relative_image_path\n",
    "        print(featured_image_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "url = \"https://twitter.com/marswxreport\"\n",
    "browser.visit(url)\n",
    "html = browser.html\n",
    "soup = bs(html, \"html.parser\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "text = soup.find_all('ol',  class_='stream-items js-navigable-stream')\n",
    "print(text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "url = \"https://space-facts.com/mars/\"\n",
    "browser.visit(url)\n",
    "html = browser.html\n",
    "soup = bs(html, \"html.parser\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "col1 = soup.find_all('td', class_='column-1')\n",
    "col2 = soup.find_all('td', class_='column-2')\n",
    "column1 = []\n",
    "column2 = []\n",
    "for col in col1:\n",
    "    column1.append(col.text)\n",
    "for col in col2:\n",
    "    column2.append(col.text)\n",
    "#print(col1)\n",
    "#print(col2)\n",
    "data = {'Facts': column1, 'Data' : column2}\n",
    "df = pd.DataFrame(data=data)\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "hemisphere_image_urls = []\n",
    "\n",
    "data = {\"title\": None, \"img_url\": None}\n",
    "data2 = {\"title\": None, \"img_url\": None}\n",
    "data3 = {\"title\": None, \"img_url\": None}\n",
    "data4 = {\"title\": None, \"img_url\": None}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "url = \"https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced\"\n",
    "browser.visit(url)\n",
    "html = browser.html\n",
    "soup = bs(html, \"html.parser\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg\n",
      "Cerberus Hemisphere Enhanced\n",
      "{'title': 'Cerberus Hemisphere Enhanced', 'img_url': 'https://astrogeology.usgs.gov/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg'}\n",
      "[{'title': 'Cerberus Hemisphere Enhanced', 'img_url': 'https://astrogeology.usgs.gov/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg'}]\n"
     ]
    }
   ],
   "source": [
    "hemisphere_1_urls = [x['src'] for x in soup.findAll('img', {'class': 'wide-image'})]\n",
    "print(hemisphere_1_urls[0])\n",
    "\n",
    "for strong_tag1 in soup.find_all('h2', class_='title'):\n",
    "    print (strong_tag1.text)\n",
    "    data['title'] = strong_tag1.text\n",
    "\n",
    "data[\"img_url\"] = \"https://astrogeology.usgs.gov\" + hemisphere_1_urls[0]\n",
    "print (data)\n",
    "hemisphere_image_urls.append(data)\n",
    "print (hemisphere_image_urls)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "url = \"https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced\"\n",
    "browser.visit(url)\n",
    "html = browser.html\n",
    "soup = bs(html, \"html.parser\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "/cache/images/3cdd1cbf5e0813bba925c9030d13b62e_schiaparelli_enhanced.tif_full.jpg\n",
      "Schiaparelli Hemisphere Enhanced\n",
      "{'title': 'Schiaparelli Hemisphere Enhanced', 'img_url': 'https://astrogeology.usgs.gov/cache/images/3cdd1cbf5e0813bba925c9030d13b62e_schiaparelli_enhanced.tif_full.jpg'}\n",
      "[{'title': 'Cerberus Hemisphere Enhanced', 'img_url': 'https://astrogeology.usgs.gov/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg'}, {'title': 'Schiaparelli Hemisphere Enhanced', 'img_url': 'https://astrogeology.usgs.gov/cache/images/3cdd1cbf5e0813bba925c9030d13b62e_schiaparelli_enhanced.tif_full.jpg'}]\n"
     ]
    }
   ],
   "source": [
    "hemisphere_2_urls = [x['src'] for x in soup.findAll('img', {'class': 'wide-image'})]\n",
    "print(hemisphere_2_urls[0])\n",
    "\n",
    "for strong_tag2 in soup.find_all('h2', class_='title'):\n",
    "    print (strong_tag2.text)\n",
    "    data2['title'] = strong_tag2.text\n",
    "\n",
    "data2[\"img_url\"] = \"https://astrogeology.usgs.gov\" + hemisphere_2_urls[0]\n",
    "print (data2)\n",
    "hemisphere_image_urls.append(data2)\n",
    "print (hemisphere_image_urls)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "url = \"https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced\"\n",
    "browser.visit(url)\n",
    "html = browser.html\n",
    "soup = bs(html, \"html.parser\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg\n",
      "Syrtis Major Hemisphere Enhanced\n",
      "{'title': 'Syrtis Major Hemisphere Enhanced', 'img_url': 'https://astrogeology.usgs.gov/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg'}\n",
      "[{'title': 'Cerberus Hemisphere Enhanced', 'img_url': 'https://astrogeology.usgs.gov/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg'}, {'title': 'Schiaparelli Hemisphere Enhanced', 'img_url': 'https://astrogeology.usgs.gov/cache/images/3cdd1cbf5e0813bba925c9030d13b62e_schiaparelli_enhanced.tif_full.jpg'}, {'title': 'Syrtis Major Hemisphere Enhanced', 'img_url': 'https://astrogeology.usgs.gov/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg'}]\n"
     ]
    }
   ],
   "source": [
    "hemisphere_3_urls = [x['src'] for x in soup.findAll('img', {'class': 'wide-image'})]\n",
    "print(hemisphere_3_urls[0])\n",
    "\n",
    "for strong_tag3 in soup.find_all('h2', class_='title'):\n",
    "    print (strong_tag3.text)\n",
    "    data3['title'] = strong_tag3.text\n",
    "\n",
    "data3[\"img_url\"] = \"https://astrogeology.usgs.gov\" + hemisphere_3_urls[0]\n",
    "print (data3)\n",
    "hemisphere_image_urls.append(data3)\n",
    "print (hemisphere_image_urls)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "url = \"https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced\"\n",
    "browser.visit(url)\n",
    "html = browser.html\n",
    "soup = bs(html, \"html.parser\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg\n",
      "Valles Marineris Hemisphere Enhanced\n",
      "{'title': None, 'img_url': 'https://astrogeology.usgs.gov/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg'}\n",
      "[{'title': 'Cerberus Hemisphere Enhanced', 'img_url': 'https://astrogeology.usgs.gov/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg'}, {'title': 'Schiaparelli Hemisphere Enhanced', 'img_url': 'https://astrogeology.usgs.gov/cache/images/3cdd1cbf5e0813bba925c9030d13b62e_schiaparelli_enhanced.tif_full.jpg'}, {'title': 'Valles Marineris Hemisphere Enhanced', 'img_url': 'https://astrogeology.usgs.gov/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg'}, {'title': None, 'img_url': 'https://astrogeology.usgs.gov/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg'}]\n"
     ]
    }
   ],
   "source": [
    "hemisphere_4_urls = [x['src'] for x in soup.findAll('img', {'class': 'wide-image'})]\n",
    "print(hemisphere_4_urls[0])\n",
    "\n",
    "for strong_tag4 in soup.find_all('h2', class_='title'):\n",
    "    print (strong_tag4.text)\n",
    "    data3['title'] = strong_tag4.text\n",
    "\n",
    "data4[\"img_url\"] = \"https://astrogeology.usgs.gov\" + hemisphere_4_urls[0]\n",
    "print (data4)\n",
    "hemisphere_image_urls.append(data4)\n",
    "print (hemisphere_image_urls)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
