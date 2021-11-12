import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class unitest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe") #Ubicación del webdriver


       #Comienza la función que hará toda  la prueba
    def test_Pagina(self):
        driver = self.driver
        driver.get("http://grupolhogar-001-site1.etempurl.com/") #página donde se hará el test
        driver.maximize_window()
        time.sleep(5)

        #Seleccionar la sección del menu tablas
        Tablas = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/form/div[1]/input")
        Tablas.send_keys("josedejesus.zm@gmail.com")
        time.sleep(3)

        Tablas = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/form/div[2]/input")
        Tablas.send_keys("jshddj")
        time.sleep(3)

        Tablas = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/form/button")
        Tablas.click()
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()



























    # #Abrir el menu
        # AbrirMenu = driver.find_element_by_xpath("/html/body/div[2]")
        # AbrirMenu.click()
        # time.sleep(3)

        # #Seleccionar la sección del menu tablas
        # Tablas = driver.find_element_by_id("_tablas")
        # Tablas.click()
        # time.sleep(3)

        

        # #seleccionar tipos de documentos 
        # Tablas = driver.find_element_by_id("monedas")
        # Tablas.click()
        # time.sleep(9)

        # #agregar nuevo
        # Tablas = driver.find_element_by_name("_new")
        # Tablas.click()
        # time.sleep(3)


        # #codigo
        # Tablas = driver.find_element_by_xpath("/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/ui-numericbox/input")
        # Tablas.send_keys("5")
        # time.sleep(3)

        # #descripcion
        # Tablas = driver.find_element_by_xpath("/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/ui-textbox/input")
        # Tablas.send_keys("jshddj")
        # time.sleep(3)

        # #simbolo
        # Tablas = driver.find_element_by_xpath("/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/ui-textbox/input")
        # Tablas.send_keys("$")
        # time.sleep(3)

        # #simboloiso
        # Tablas = driver.find_element_by_xpath("/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[4]/ui-textbox/input")
        # Tablas.send_keys("$")
        # time.sleep(3)

        # #guardar
        # Tablas = driver.find_element_by_name("_save")
        # Tablas.click()
        # time.sleep(3)

        # #actualizar
        # Tablas = driver.find_element_by_name("_refresh")
        # Tablas.click()
        # time.sleep(3)
