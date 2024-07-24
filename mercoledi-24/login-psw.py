# Visita https://practicetestautomation.com/practice-test-login/
# Effettua il login con username "student" e password "Password123"
# Verifica che il login sia avvenuto con successo


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time



def setup_driver():
    driver = webdriver.Chrome()
    return driver

#       Effettua il login sul sito con le credenziali fornite.
def login(driver, username, password):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    #  Trova i campi di input per username e password
    trova_username = driver.find_element(By.ID, 'username')
    trova_pass = driver.find_element(By.ID, 'password')
    
    #   Inserisci le credenziali nei campi di input
    trova_username.send_keys(username)
    trova_pass.send_keys(password)
    
    # Trova e clicca sul pulsante di login
    login_button = driver.find_element(By.ID, 'submit')
    login_button.click()

def verifica_login(driver):
    
    success_message = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Logged In Successfully')]"))
    )
    return success_message is not None
# 
driver = setup_driver()
username = 'student'
password = "Password123"
login(driver, username, password)

if verifica_login(driver):
    print("Login avvenuto con successo.")
else:
    print("Login fallito.")

driver.quit()