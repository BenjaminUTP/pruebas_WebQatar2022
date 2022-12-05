import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class TestInicioSesiones():
    def test_iniciarSesion_CamposVacios(self):
        self.driver = webdriver.Chrome('C://selenium-java-4.5.3/chromedriver.exe')
        # Hacemos la pestaña del navegador mas grande
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

        self.driver.get("http://localhost/login")
        self.driver.find_element(By.ID, "email").send_keys("")
        self.driver.find_element(By.ID, "password").send_keys("")

        self.driver.find_element(By.NAME, "iniciar").submit()


        self.driver.quit()


    def test_inicioSesion_ContraseñaIncorrecta(self):
        self.driver = webdriver.Chrome('C://selenium-java-4.5.3/chromedriver.exe')
        # Hacemos la pestaña del navegador mas grande
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

        self.driver.get("http://localhost/login")
        self.driver.find_element(By.ID, "email").send_keys("prueba6@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("password2")

        self.driver.find_element(By.NAME, "iniciar").submit()


        self.driver.quit()

    def test_inicioSesion_EmailErroneo(self):
        self.driver = webdriver.Chrome('C://selenium-java-4.5.3/chromedriver.exe')
        # Hacemos la pestaña del navegador mas grande
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

        self.driver.get("http://localhost/login")
        self.driver.find_element(By.ID, "email").send_keys("prueb6@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("password1")

        self.driver.find_element(By.NAME, "iniciar").submit()


        self.driver.quit()


    def test_inicioSesion_Valido(self):
        self.driver = webdriver.Chrome('C://selenium-java-4.5.3/chromedriver.exe')
        # Hacemos la pestaña del navegador mas grande
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

        self.driver.get("http://localhost/login")
        self.driver.find_element(By.ID, "email").send_keys("prueba6@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("password1")

        self.driver.find_element(By.NAME, "iniciar").submit()


        self.driver.quit()
