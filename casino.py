from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import pandas as pd

navegador = webdriver.Chrome(executable_path='chromedriver.exe')

navegador.get("https://blaze.com/pt/games/crash")


#ultimas rodadas
last_play = navegador.find_element(By.XPATH,
    '//*[@id="crash-recent"]/div[2]/div[2]/span[1]/text()[1]') 
print(last_play)

#xml = html.fromstring(h)

#table =  xml.xpath("//table[@class='casino-table dark-header crash-entries']")[0]

#for row in table.xpath(".//tr"):
     # get the text from all the td's from each row
    #print([td.text for td in row.xpath(".//td[@class='dddefault']")])

#jogadores e apostas


#excel