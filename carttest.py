import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import HtmlTestRunner  # Import HtmlTestRunner for HTML reports

class SauceDemoTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(5)

    def login(self):
        driver = self.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

    def add_to_cart_and_verify(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(1) .btn_inventory").click()
        time.sleep(2)
        driver.get("https://www.saucedemo.com/inventory.html")
        driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(2) .btn_inventory").click()
        time.sleep(2)

        # Verify cart total
        cart_total = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        self.assertEqual(cart_total, "2", "Cart item count mismatch")

        # Open cart and validate items
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(2)
        items_in_cart = driver.find_elements(By.CLASS_NAME, "cart_item")
        self.assertEqual(len(items_in_cart), 2, "Cart items count mismatch")

    def test_cart_functionality(self):
        self.login()
        self.add_to_cart_and_verify()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
