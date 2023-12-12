# League of Legends Champions' Characteristics with spaCy and Network Diagram with NetworkX in Python
## Abstract
League of Legends is a multiplayer online battle arena meticulously crafted by Riot Games, proving players with a vast pool of champions to choose from. Each champion is designed with intricate backstories that makes up a complex narrative backdrop and a complete universe of its own. These materials can be an exciting source of data for natural language processing and network analysis, which are the aim of this project.
## Overview
Instead of relying on the summaries of the Fandom website, the analysis utilises the official sources, which are presented in https://universe.leagueoflegends.com/en_US/champions/. The process of scraping the website was performed by LOLWebScraping script, and the result was combined into a CSV file, 'lolstory.csv'. This text file is analysed to derive each champion's dominant features from their stories and to visualise the relationship network between them.
## Library Requirements
* LOLWebScraping
  + Selenium
  + BeautifulSoup4
* LOLCharactersAnalysis
  + pandas
  + spaCy
  + scikit-learn
  + NetworkX
  + Matplotlib

## Caution
Champion "Milio" has different HTML structure, so the Python script can't scrape its stories. To avoid any errors while running the notebook, remove champion "Milio" completely, or copy the story manually from official websites to the CSV file. If the script can't scrape other stories, please provide longer waiting time.
