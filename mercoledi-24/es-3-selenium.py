# Visita https://www.w3schools.com/html/html_tables.asp
# Estrai i dati dalla prima tabella sulla pagina e stampali in formato leggibile

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def setup_driver():
    driver = webdriver.Chrome()
    return driver

def estrai_tabella_dati(driver):
    
    driver.get("https://www.w3schools.com/html/html_tables.asp")         #visita la pagina con la tabella
    tabella = driver.find_element(By.XPATH, '//table[@id="customers"]')   # trova la prima tabella nella pagina
    # trova tutte le righe della tabella 
    righe = tabella.find_elements(By.TAG_NAME, 'tr')
    
    # iteriamo tutte le righe
    for riga in righe:
        celle = riga.find_elements(By.TAG_NAME, 'td')
        # estrazione testo di ongi cella 
        celle_testo = [cella.text for cella in celle]
        # se ci sono celle nella riga, stampa i dati
        if celle_testo:
            print(f"{', '.join(celle_testo)}")
            

driver = setup_driver()
estrai_tabella_dati(driver)
driver.quit()