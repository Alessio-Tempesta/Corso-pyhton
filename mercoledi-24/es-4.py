# Visita https://demoqa.com/dynamic-properties
# Attendi che il bottone "Visible After 5 Seconds" appaia
# Cliccalo e verifica che l'azione sia stata eseguita con successo


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def setup_driver():
    driver = webdriver.Chrome()
    return driver

def dynamic_form(driver):
    
    # Naviga verso il sito
    driver.get("https://demoqa.com/dynamic-properties")
    
    # Attendi che il bottone "Visible After 5 Seconds" diventi visibile
    button = driver.find_element(By.ID, "visibleAfter")
    print("Attendo che il bottone diventi visibile...")
    time.sleep(6)  # Attendi 6 secondi
    
    button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "visibleAfter"))
    )
    
    # Verifica se il bottone è visibile e cliccalo
    if button.is_displayed():
        print("Il bottone è visibile. Clicco sul bottone.")
        button.click()
        print("Bottone cliccato con successo.")
    else:
        print("Il bottone non è visibile.")
    
    # Chiudi il browser
    driver.quit()

# Esegui la funzione
driver = setup_driver()
dynamic_form(driver)
