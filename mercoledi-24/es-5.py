# Visita https://news.ycombinator.com/
# Estrai i titoli, i link e i punteggi dei primi 3 articoli
# Salva questi dati in un file CSV

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd

def setup_driver():
    driver = webdriver.Chrome()
    return driver


# Visita la pagina di Hacker News
driver.get('https://news.ycombinator.com/')

# Trova gli articoli nella pagina
articles = driver.find_elements(By.CSS_SELECTOR, '.athing')

data = []
for article in articles[:3]:
    title_element = article.find_element(By.CSS_SELECTOR, '.storylink')
    title = title_element.text
    link = title_element.get_attribute('href')
    
    # Trova il punteggio dell'articolo
    score_element = article.find_element(By.XPATH, 'following-sibling::tr//span[@class="score"]')
    score = score_element.text if score_element else '0 points'
    
    data.append({
        'Title': title,
        'Link': link,
        'Score': score
    })

# Crea un DataFrame e salva i dati in un file CSV
df = pd.DataFrame(data)
df.to_csv('hacker_news_top_articles_selenium.csv', index=False)
print('Dati salvati in hacker_news_top_articles_selenium.csv')

# Chiudi il browser
driver.quit()
