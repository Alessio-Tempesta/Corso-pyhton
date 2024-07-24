# Uno script per visitare Wikipedia, cerca "Python (programming language)" e stampare il primo paragrafo della pagina risultante.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

    # Configura e restituisce un'istanza del WebDriver di Chrome
def setup_driver():

    driver = webdriver.Chrome()
    return driver

    # Cerca una query su Wikipedia e restituisce il primo paragrafo della pagina risultante.
def ricerca_wikipedia(driver, query):
    # Visita la homepage di Wikipedia
    driver.get("https://www.wikipedia.org/")
    
    # Trova la barra di ricerca e inserisce la query
    search_box = driver.find_element(By.NAME, 'search')
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    
    # Attendi che la pagina dei risultati si carichi e che il primo paragrafo sia presente
    first_paragraph = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//p'))
    )
    return first_paragraph.text

# Esegui la funzione principale
driver = setup_driver()
query = "Python (programming language)"
first_paragraph = ricerca_wikipedia(driver, query)
if first_paragraph:
    print("Il primo paragrafo:", first_paragraph)
else:
    print("Non è stato possibile trovare il primo paragrafo.")
driver.quit()
