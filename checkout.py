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
        # Add the first product
        driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(1) .btn_inventory").click()
        time.sleep(2)
        
        # Add the second product
        driver.get("https://www.saucedemo.com/inventory.html")  # Go back to inventory
        driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(2) .btn_inventory").click()
        time.sleep(2)

        # Verify the cart total
        cart_total = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        self.assertEqual(cart_total, "2", "Cart item count mismatch")

        # Open cart and validate items
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(2)
        items_in_cart = driver.find_elements(By.CLASS_NAME, "cart_item")
        self.assertEqual(len(items_in_cart), 2, "Cart items count mismatch")

    def proceed_to_checkout(self):
        driver = self.driver
        # Proceed to checkout
        driver.find_element(By.CLASS_NAME, "checkout_button").click()
        time.sleep(2)

    def empty_cart_checkout(self):
        driver = self.driver
        # Go to cart and remove all items
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(2)
        
        # Remove items from the cart
        remove_buttons = driver.find_elements(By.CLASS_NAME, "cart_button")
        for button in remove_buttons:
            button.click()
            time.sleep(1)
        
        # Proceed to checkout with an empty cart
        self.proceed_to_checkout()

        # Verify that the error message for empty cart is displayed
        error_message = driver.find_element(By.CSS_SELECTOR, ".error-message-container").text
        self.assertIn("Your cart is empty", error_message, "Empty Cart Error not displayed correctly.")

    def test_checkout_functionality(self):
        self.login()
        self.add_to_cart_and_verify()
        self.proceed_to_checkout()

    def test_empty_cart_checkout(self):
        self.login()
        self.empty_cart_checkout()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
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
        # Add the first product
        driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(1) .btn_inventory").click()
        time.sleep(2)
        
        # Add the second product
        driver.get("https://www.saucedemo.com/inventory.html")  # Go back to inventory
        driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(2) .btn_inventory").click()
        time.sleep(2)

        # Verify the cart total
        cart_total = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        self.assertEqual(cart_total, "2", "Cart item count mismatch")

        # Open cart and validate items
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(2)
        items_in_cart = driver.find_elements(By.CLASS_NAME, "cart_item")
        self.assertEqual(len(items_in_cart), 2, "Cart items count mismatch")

    def proceed_to_checkout(self):
        driver = self.driver
        # Proceed to checkout
        driver.find_element(By.CLASS_NAME, "checkout_button").click()
        time.sleep(2)

    def empty_cart_checkout(self):
        driver = self.driver
        # Go to cart and remove all items
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(2)
        
        # Remove items from the cart
        remove_buttons = driver.find_elements(By.CLASS_NAME, "cart_button")
        for button in remove_buttons:
            button.click()
            time.sleep(1)
        
        # Proceed to checkout with an empty cart
        self.proceed_to_checkout()

        # Verify that the error message for empty cart is displayed
        error_message = driver.find_element(By.CSS_SELECTOR, ".error-message-container").text
        self.assertIn("Your cart is empty", error_message, "Empty Cart Error not displayed correctly.")

    def test_checkout_functionality(self):
        self.login()
        self.add_to_cart_and_verify()
        self.proceed_to_checkout()

    def test_empty_cart_checkout(self):
        self.login()
        self.empty_cart_checkout()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
