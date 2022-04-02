from ast import While
from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime


from time import sleep


import pandas as pd

navegador = webdriver.Chrome(executable_path='chromedriver.exe')

navegador.get("https://blaze.com/pt/games/crash")

while True:
    element = WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="crash-recent"]/div[2]/div[2]')))
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if element == element:
        last_play = navegador.find_element(By.XPATH,
            '//*[@id="crash-recent"]/div[2]/div[2]').text
    sleep(10)
    print(last_play[:5], current_time)

#ultimas rodadas
# while True: 
#     last_play = navegador.find_element(By.XPATH,
#         '//*[@id="crash-recent"]/div[2]/div[2]').text
#     now = datetime.now()
#     current_time = now.strftime("%H:%M:%S")
#     print(last_play[:5], current_time)
#     sleep(10)


#jogadores e apostas


#excel