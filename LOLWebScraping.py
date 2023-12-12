# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 08:24:28 2023

@author: Bui Son Trang
"""

#selenium for scraping dynamic websites and bs4 for formatting the websites' sources
from selenium import webdriver
from bs4 import BeautifulSoup

#The original websites roots
site = 'https://universe.leagueoflegends.com/en_AU/champions/'
bio_site = 'https://universe.leagueoflegends.com/en_AU/story/champion/'
story_site = 'https://universe.leagueoflegends.com/en_AU/story/champion-color-story/'

#Getting champions' names and parameters in the stories' links
driver = webdriver.Chrome()

driver.get(site)

driver.implicitly_wait(3)

page_source = driver.page_source

soup = BeautifulSoup(page_source, 'html.parser')

elements = soup.find_all(class_ = 'item_30l8')

links = []
for element in elements:
    link = element.find_all('a', href = True)
    links.extend(link)

champions_links = {}
for link in links:
    champions_links[link.find('h1').text] = link['href'].split('/')[-2]

#Getting the stories for each champion
champions_stories = {}
for key, value in champions_links.items():
    story = ''
    champ_bio_site = bio_site + value + '/'
    champ_story_site = story_site.replace('champion', value)
    
    driver.get(champ_bio_site)
    driver.implicitly_wait(1)
    bio_page_source = driver.page_source
    driver.get(champ_story_site)
    driver.implicitly_wait(1)
    story_page_source = driver.page_source
    
    bio_soup = BeautifulSoup(bio_page_source, 'html.parser')
    elements = bio_soup.find_all(class_ = 'p_1_sJ')
    for element in elements:
        story += element.text.strip().replace('\n', ' ').strip('"') + ' '

    story_soup = BeautifulSoup(story_page_source, 'html.parser')
    elements = story_soup.find_all(class_ = 'p_1_sJ')
    for element in elements:
        story += element.text.strip().replace('\n', ' ').strip('"') + ' '
    
    champions_stories[key] = story

#Quitting the driver
driver.quit()

#Saving to CSV file
with open('lolstory.csv', 'w') as file:
    for key, value in champions_stories.items():
        file.write(f'{key},{value}\n')
    
