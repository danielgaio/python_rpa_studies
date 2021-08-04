import time
import openpyxl
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print('Iniciando robô ...')

# Criar arquivo de texto para guardar os resultados
arquivo = open('Resultado.txt', 'w')

dominios = []
# lendo do excel
xlsx_file = Path('dominios.xlsx')
# Escolher uma aba de planilha dentro do arquivo
wb_obj = openpyxl.load_workbook(xlsx_file)

# Read the active sheet:
sheet = wb_obj.active

for linha in range(1, 8):
  print(sheet['A'+str(linha)].value)
  dominios.append(sheet['A'+str(linha)].value)

# time.sleep(10)

# Abrir navegador e o site desejado
driver = webdriver.Chrome(executable_path='chromedriver_linux64/chromedriver')
driver.get('https://registro.br/')

# Realizar pesquisa

for dominio in dominios:
  # Pegar caixa de pesquisa e limpar
  pesquisa = driver.find_element_by_id('is-avail-field')
  pesquisa.clear()

  pesquisa.send_keys(dominio)
  # clica enter
  pesquisa.send_keys(Keys.RETURN)
  time.sleep(2)

  resultados = driver.find_elements_by_tag_name("strong")

  texto = 'Dominio {} {}\n'.format(dominio, resultados[4].text)
  print(texto)
  arquivo.write(texto)

arquivo.close()
driver.close()
print('Fim')