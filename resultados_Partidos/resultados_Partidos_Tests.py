import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
class TestResultadosPartidos():

    def test_resultados_Fecha21(self):
        self.driver = webdriver.Chrome('C://selenium-java-4.5.3/chromedriver.exe')
        # Hacemos la pestaña del navegador mas grande
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

        self.driver.get("http://localhost/resultados")
        self.driver.find_element(By.ID, "play_date").send_keys("11212022")
        self.driver.find_element(By.ID, "buscar").submit()
        self.driver.quit()

    def test_resultados_Fecha22(self):
        self.driver = webdriver.Chrome('C://selenium-java-4.5.3/chromedriver.exe')
        # Hacemos la pestaña del navegador mas grande
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

        self.driver.get("http://localhost/resultados")
        self.driver.find_element(By.ID, "play_date").send_keys("11222022")
        self.driver.find_element(By.ID, "buscar").submit()
        self.driver.quit()

    def test_resultados_Fecha30(self):
        self.driver = webdriver.Chrome('C://selenium-java-4.5.3/chromedriver.exe')
        # Hacemos la pestaña del navegador mas grande
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

        self.driver.get("http://localhost/resultados")
        self.driver.find_element(By.ID, "play_date").send_keys("11302022")
        self.driver.find_element(By.ID, "buscar").submit()
        self.driver.quit()

    def test_resultados_Fecha01(self):
        self.driver = webdriver.Chrome('C://selenium-java-4.5.3/chromedriver.exe')
        # Hacemos la pestaña del navegador mas grande
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

        self.driver.get("http://localhost/resultados")
        self.driver.find_element(By.ID, "play_date").send_keys("12012022")
        self.driver.find_element(By.ID, "buscar").submit()
        self.driver.quit()

    def test_resultados_Fecha02(self):
        self.driver = webdriver.Chrome('C://selenium-java-4.5.3/chromedriver.exe')
        # Hacemos la pestaña del navegador mas grande
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

        self.driver.get("http://localhost/resultados")
        self.driver.find_element(By.ID, "play_date").send_keys("12022022")
        self.driver.find_element(By.ID, "buscar").submit()
        self.driver.quit()