import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
class TestRegistroCuenta():


    def test_registrar_Apellido(self):
        self.driver = webdriver.Chrome('C://selenium-java-4.5.3/chromedriver.exe')
        # Hacemos la pestaña del navegador mas grande
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

        # Comienza la prueba
        self.driver.get("http://localhost/registrar")
        self.driver.find_element(By.ID, "first_name").send_keys("flujonormal1")
        self.driver.find_element(By.ID, "last_name").send_keys("flujonormal")
        self.driver.find_element(By.ID, "email").send_keys("prueba2@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("password1")
        self.driver.find_element(By.ID, "repeat_password").send_keys("password1")
        self.driver.find_element(By.NAME, "create").submit()
        self.driver.quit()

    def test_registrar_ApellidoNulo(self):
        self.driver = webdriver.Chrome('C://selenium-java-4.5.3/chromedriver.exe')
        # Hacemos la pestaña del navegador mas grande
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

        # Comienza la prueba
        self.driver.get("http://localhost/registrar")
        self.driver.find_element(By.ID, "first_name").send_keys("flujonormal1")
        self.driver.find_element(By.ID, "last_name").send_keys("")
        self.driver.find_element(By.ID, "email").send_keys("prueba3@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("password1")
        self.driver.find_element(By.ID, "repeat_password").send_keys("password1")
        self.driver.find_element(By.NAME, "create").submit()
        self.driver.quit()

    def test_registrar_Email(self):
        self.driver = webdriver.Chrome('C://selenium-java-4.5.3/chromedriver.exe')
        # Hacemos la pestaña del navegador mas grande
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

        # Comienza la prueba
        self.driver.get("http://localhost/registrar")
        self.driver.find_element(By.ID, "first_name").send_keys("flujonormal1")
        self.driver.find_element(By.ID, "last_name").send_keys("flujonormal")
        self.driver.find_element(By.ID, "email").send_keys("prueba4@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("password1")
        self.driver.find_element(By.ID, "repeat_password").send_keys("password1")
        self.driver.find_element(By.NAME, "create").submit()
        self.driver.quit()

    def test_registrar_EmailDuplicado(self):
        self.driver = webdriver.Chrome('C://selenium-java-4.5.3/chromedriver.exe')
        # Hacemos la pestaña del navegador mas grande
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

        # Comienza la prueba
        self.driver.get("http://localhost/registrar")
        self.driver.find_element(By.ID, "first_name").send_keys("flujonormal1")
        self.driver.find_element(By.ID, "last_name").send_keys("flujonormal")
        self.driver.find_element(By.ID, "email").send_keys("correo@correo.com")
        self.driver.find_element(By.ID, "password").send_keys("password1")
        self.driver.find_element(By.ID, "repeat_password").send_keys("password1")
        self.driver.find_element(By.NAME, "create").submit()
        self.driver.quit()

    def test_registrar_EmailFormatoInvalido(self):
        self.driver = webdriver.Chrome('C://selenium-java-4.5.3/chromedriver.exe')
        # Hacemos la pestaña del navegador mas grande
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

        # Comienza la prueba
        self.driver.get("http://localhost/registrar")
        self.driver.find_element(By.ID, "first_name").send_keys("flujonormal1")
        self.driver.find_element(By.ID, "last_name").send_keys("flujonormal")
        self.driver.find_element(By.ID, "email").send_keys("invalido")
        self.driver.find_element(By.ID, "password").send_keys("password1")
        self.driver.find_element(By.ID, "repeat_password").send_keys("password1")
        self.driver.find_element(By.NAME, "create").submit()
        self.driver.quit()

    def test_registrar_EmailNulo(self):
        self.driver = webdriver.Chrome('C://selenium-java-4.5.3/chromedriver.exe')
        # Hacemos la pestaña del navegador mas grande
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

        # Comienza la prueba
        self.driver.get("http://localhost/registrar")
        self.driver.find_element(By.ID, "first_name").send_keys("flujonormal1")
        self.driver.find_element(By.ID, "last_name").send_keys("flujonormal")
        self.driver.find_element(By.ID, "email").send_keys("")
        self.driver.find_element(By.ID, "password").send_keys("password1")
        self.driver.find_element(By.ID, "repeat_password").send_keys("password1")
        self.driver.find_element(By.NAME, "create").submit()
        self.driver.quit()

    def test_registrar_Nombre(self):
        self.driver = webdriver.Chrome('C://selenium-java-4.5.3/chromedriver.exe')
        # Hacemos la pestaña del navegador mas grande
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

        # Comienza la prueba
        self.driver.get("http://localhost/registrar")
        self.driver.find_element(By.ID, "first_name").send_keys("flujonormal")
        self.driver.find_element(By.ID, "last_name").send_keys("flujonormal")
        self.driver.find_element(By.ID, "email").send_keys("pruebaflujonormal@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("password1")
        self.driver.find_element(By.ID, "repeat_password").send_keys("password1")
        self.driver.find_element(By.NAME, "create").submit()
        self.driver.quit()

    def test_registrar_NombreNulo(self):
        self.driver = webdriver.Chrome('C://selenium-java-4.5.3/chromedriver.exe')
        # Hacemos la pestaña del navegador mas grande
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

        # Comienza la prueba
        self.driver.get("http://localhost/registrar")
        self.driver.find_element(By.ID, "first_name").send_keys("")
        self.driver.find_element(By.ID, "last_name").send_keys("flujonormal")
        self.driver.find_element(By.ID, "email").send_keys("prueba1@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("password1")
        self.driver.find_element(By.ID, "repeat_password").send_keys("password1")
        self.driver.find_element(By.NAME, "create").submit()
        self.driver.quit()

    def test_registrar_PasswordNulo(self):
        self.driver = webdriver.Chrome('C://selenium-java-4.5.3/chromedriver.exe')
        # Hacemos la pestaña del navegador mas grande
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

        # Comienza la prueba
        self.driver.get("http://localhost/registrar")
        self.driver.find_element(By.ID, "first_name").send_keys("flujonormal1")
        self.driver.find_element(By.ID, "last_name").send_keys("flujonormal")
        self.driver.find_element(By.ID, "email").send_keys("prueba7@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("")
        self.driver.find_element(By.ID, "repeat_password").send_keys("password1")
        self.driver.find_element(By.NAME, "create").submit()
        self.driver.quit()

    def test_registrar_PasswordInvalido(self):
        self.driver = webdriver.Chrome('C://selenium-java-4.5.3/chromedriver.exe')
        # Hacemos la pestaña del navegador mas grande
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

        # Comienza la prueba
        self.driver.get("http://localhost/registrar")
        self.driver.find_element(By.ID, "first_name").send_keys("flujonormal1")
        self.driver.find_element(By.ID, "last_name").send_keys("flujonormal")
        self.driver.find_element(By.ID, "email").send_keys("prueba7@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("pass")
        self.driver.find_element(By.ID, "repeat_password").send_keys("pass")
        self.driver.find_element(By.NAME, "create").submit()
        self.driver.quit()

    def test_registrar_PasswordValido(self):
        self.driver = webdriver.Chrome('C://selenium-java-4.5.3/chromedriver.exe')
        # Hacemos la pestaña del navegador mas grande
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

        # Comienza la prueba
        self.driver.get("http://localhost/registrar")
        self.driver.find_element(By.ID, "first_name").send_keys("flujonormal1")
        self.driver.find_element(By.ID, "last_name").send_keys("flujonormal")
        self.driver.find_element(By.ID, "email").send_keys("prueba6@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("password1")
        self.driver.find_element(By.ID, "repeat_password").send_keys("password1")
        self.driver.find_element(By.NAME, "create").submit()
        self.driver.quit()

    def test_registrar_RepetirPasswordNulo(self):
        self.driver = webdriver.Chrome('C://selenium-java-4.5.3/chromedriver.exe')
        # Hacemos la pestaña del navegador mas grande
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

        # Comienza la prueba
        self.driver.get("http://localhost/registrar")
        self.driver.find_element(By.ID, "first_name").send_keys("flujonormal1")
        self.driver.find_element(By.ID, "last_name").send_keys("flujonormal")
        self.driver.find_element(By.ID, "email").send_keys("prueba11@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("password1")
        self.driver.find_element(By.ID, "repeat_password").send_keys("")
        self.driver.find_element(By.NAME, "create").submit()
        self.driver.quit()

    def test_registrar_RepetirPasswordValido(self):
        self.driver = webdriver.Chrome('C://selenium-java-4.5.3/chromedriver.exe')
        # Hacemos la pestaña del navegador mas grande
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

        # Comienza la prueba
        self.driver.get("http://localhost/registrar")
        self.driver.find_element(By.ID, "first_name").send_keys("flujonormal1")
        self.driver.find_element(By.ID, "last_name").send_keys("flujonormal")
        self.driver.find_element(By.ID, "email").send_keys("prueba9@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("password1")
        self.driver.find_element(By.ID, "repeat_password").send_keys("password1")
        self.driver.find_element(By.NAME, "create").submit()
        self.driver.quit()

    def test_registrar_RepetirPasswordInvalido(self):
        self.driver = webdriver.Chrome('C://selenium-java-4.5.3/chromedriver.exe')
        # Hacemos la pestaña del navegador mas grande
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

        # Comienza la prueba
        self.driver.get("http://localhost/registrar")
        self.driver.find_element(By.ID, "first_name").send_keys("flujonormal1")
        self.driver.find_element(By.ID, "last_name").send_keys("flujonormal")
        self.driver.find_element(By.ID, "email").send_keys("prueba10@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("password1")
        self.driver.find_element(By.ID, "repeat_password").send_keys("pass")
        self.driver.find_element(By.NAME, "create").submit()
        self.driver.quit()