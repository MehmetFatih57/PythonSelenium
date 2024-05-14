from telnetlib import EC
from time import sleep
from utilitiessss import Constant as c


from openpyxl.reader.excel import load_workbook
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utilitiessss import Driver, ConfigReader
from pages import SaucePage
import openpyxl
import pytest



class TestSauce:
    def setup_method(self):
        self.driver = Driver.get_driver(True)
        self.driver.get(ConfigReader.read_config("url"))
        self.page = SaucePage.SaucePage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_invalid_login(self):
        # -Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required"
        # gösterilmelidir.
        self.page.login_button.click()
        message = self.driver.find_element(By.XPATH, "//h3[@data-test=\"error\"]")
        print(f"Hata Mesaji  {message.text}")
        sleep(2)
        assert message.text == c.error_user_name

        print("----------------------------------------------------------------------------------")

    def test_password_login(self):
        # -Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
        self.page.user_name.send_keys("standard_user")
        self.page.login_button.click()
        password_message = self.driver.find_element(By.XPATH, "//h3")
        print(f"Hata Mesaji  {password_message.text}")
        assert password_message.text == c.error_password
        self.page.user_name.clear()

        print("----------------------------------------------------------------------------------")

    def test_locked_login(self):
        # -Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry,
        # this user has been locked out." mesajı gösterilmelidir.
        self.page.user_name.send_keys("locked_out_user")
        self.page.password.send_keys("secret_sauce")
        self.page.login_button.click()
        locked_message = self.driver.find_element(By.XPATH, "//h3")
        print(f"Hata Mesaji  {locked_message.text}")
        assert locked_message.text == c.error_locked_user
        self.page.user_name.clear()


        print("----------------------------------------------------------------------------------")

    # -Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına
    # gönderilmelidir. Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.

    def test_valid_login(self):
        self.page.user_name.send_keys("standard_user")
        self.page.password.send_keys("secret_sauce")
        self.page.login_button.click()
        assert self.driver.current_url == c.url_inventory

        urunler = self.driver.find_elements(By.XPATH, "//div[@class='inventory_item_description']")
        sayac = len(urunler)
        for option in urunler:
            print(f"{sayac}. {option.text}")
        total_products = len(urunler)
        print(f"\nToplam Ürün Sayısı: {total_products}")
        assert total_products == 6

    def test(self):
        self.page.user_name.send_keys(ConfigReader.read_config("username1"))
        self.page.password.send_keys(ConfigReader.read_config("password"))
        self.page.login_button.click()

        self.driver.find_element(By.XPATH , "//button[@data-test='add-to-cart-sauce-labs-backpack']").click()
        add_to_cart_button = self.driver.find_element(By.XPATH,"//button[@data-test='add-to-cart-sauce-labs-backpack']")
        add_to_cart_button.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
        cart_badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert cart_badge.text == "1", "Sepette 1 ürün yok!"

