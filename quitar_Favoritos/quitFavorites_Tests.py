import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class TestquitarFavoritos():
    def test_quitFavorite_1Qatar(self):
        self.driver = webdriver.Chrome('C://selenium-java-4.5.3/chromedriver.exe')
        #Hacemos la pestaña del navegador mas grande
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

        self.driver.get("http://localhost/login")
        self.driver.find_element(By.ID, "email").send_keys("prueba6@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("password1")
        self.driver.find_element(By.NAME, "iniciar").submit()

        self.driver.get("http://localhost/favoritos")
        self.driver.get("http://localhost/api/delete-favoritos?id=40")
        self.driver.get("http://localhost/favoritos")
        self.driver.quit()

    def test_quitFavorite_2Ecuador(self):
        self.driver = webdriver.Chrome('C://selenium-java-4.5.3/chromedriver.exe')
        #Hacemos la pestaña del navegador mas grande
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

        self.driver.get("http://localhost/login")
        self.driver.find_element(By.ID, "email").send_keys("prueba6@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("password1")
        self.driver.find_element(By.NAME, "iniciar").submit()

        self.driver.get("http://localhost/favoritos")
        self.driver.get("http://localhost/api/delete-favoritos?id=32")
        self.driver.get("http://localhost/favoritos")
        self.driver.quit()

    def test_quitFavorite_25Brasil(self):
        self.driver = webdriver.Chrome('C://selenium-java-4.5.3/chromedriver.exe')
        #Hacemos la pestaña del navegador mas grande
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

        self.driver.get("http://localhost/login")
        self.driver.find_element(By.ID, "email").send_keys("prueba6@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("password1")
        self.driver.find_element(By.NAME, "iniciar").submit()

        self.driver.get("http://localhost/favoritos")
        self.driver.get("http://localhost/api/delete-favoritos?id=33")
        self.driver.get("http://localhost/favoritos")
        self.driver.quit()

    def test_quitFavorite_31Uruguay(self):
        self.driver = webdriver.Chrome('C://selenium-java-4.5.3/chromedriver.exe')
        #Hacemos la pestaña del navegador mas grande
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

        self.driver.get("http://localhost/login")
        self.driver.find_element(By.ID, "email").send_keys("prueba6@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("password1")
        self.driver.find_element(By.NAME, "iniciar").submit()

        self.driver.get("http://localhost/favoritos")
        self.driver.get("http://localhost/api/delete-favoritos?id=34")
        self.driver.get("http://localhost/favoritos")
        self.driver.quit()

    def test_quitFavorite_32CoreaSur(self):
        self.driver = webdriver.Chrome('C://selenium-java-4.5.3/chromedriver.exe')
        #Hacemos la pestaña del navegador mas grande
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

        self.driver.get("http://localhost/login")
        self.driver.find_element(By.ID, "email").send_keys("prueba6@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("password1")
        self.driver.find_element(By.NAME, "iniciar").submit()

        self.driver.get("http://localhost/favoritos")
        self.driver.get("http://localhost/api/delete-favoritos?id=35")
        self.driver.get("http://localhost/favoritos")
        self.driver.quit()