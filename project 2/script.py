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

url_pagina = driver.find_element_by_xpath(
  "//a[@aria-label='Page 2']"
).get_attribute('href')

pagina_atual = 0
start = 10
while pagina_atual < 10:
  if not pagina_atual == 0:
    url_pagina = url_pagina.replace('start=%s' % start, 'start=%s' % str(start+10))
    start += 10
  pagina_atual += 1
  driver.get(url_pagina)
  divs = driver.find_elements_by_xpath(
    "//div[@class='g']"
  )
  for div in divs:
    nome = div.find_element_by_tag_name('span')
    link = div.find_element_by_tag_name('a')
    resultado = '%s;%s' % (nome.text, link.get_attribute('href'))
    print(resultado)