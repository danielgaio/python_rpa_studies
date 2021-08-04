from selenium import webdriver
from selenium.webdriver.common.keys import Keys

pesquisa = input('Digite a pesquisa: ')

driver = webdriver.Chrome('chromedriver_linux64/chromedriver')

driver.get('https://www.google.com')

campo = driver.find_element_by_xpath("//input[@aria-label='Pesquisar']")
campo.send_keys(pesquisa)
campo.send_keys(Keys.ENTER)

resultados = driver.find_element_by_xpath("//div[@id='result-stats']").text
print(resultados)

numero_resultados = int(
  resultados.split('Aproximadamente ')[1]
  .split(' resultados')[0]
  .replace('.', ''))
  
maximo_paginas = numero_resultados/10
print('Número de páginas: {}'.format(maximo_paginas))
