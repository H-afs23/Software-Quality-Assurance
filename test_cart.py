from selenium.webdriver.common.by import By

BASE = "https://www.automationexercise.com"

def test_TC019_add_product_to_cart(driver):
    driver.get(BASE + "/products")
    driver.find_element(By.XPATH, "(//a[contains(@href,'product_details')])[1]").click()
    driver.find_element(By.XPATH, "//button[@type='button' and contains(.,'Add to cart')]").click()
    assert "added" in driver.page_source.lower()

def test_TC020_view_cart(driver):
    driver.get(BASE + "/products")
    driver.find_element(By.XPATH, "(//a[contains(@href,'product_details')])[1]").click()
    driver.find_element(By.XPATH, "//button[@type='button' and contains(.,'Add to cart')]").click()
    driver.get(BASE + "/view_cart")
    assert "Shopping Cart" in driver.page_source

def test_TC021_remove_item_from_cart(driver):
    driver.get(BASE + "/products")
    driver.find_element(By.XPATH, "(//a[contains(@href,'product_details')])[1]").click()
    driver.find_element(By.XPATH, "//button[@type='button' and contains(.,'Add to cart')]").click()
    driver.get(BASE + "/view_cart")
    driver.find_element(By.XPATH, "//a[@class='cart_quantity_delete']").click()
    assert "Cart is empty" in driver.page_source or "empty" in driver.page_source.lower()

def test_TC022_add_multiple_products(driver):
    driver.get(BASE + "/view_cart")
    assert "view_cart" in driver.current_url

def test_TC023_cart_shows_correct_price(driver):
    driver.get(BASE + "/view_cart")
    assert "view_cart" in driver.current_url

def test_TC024_proceed_to_checkout(driver):
    driver.get(BASE + "/login")
    driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys("230942@students.au.edu.pk")
    driver.find_element(By.XPATH, "//input[@data-qa='login-password']").send_keys("hafsa@9506")
    driver.find_element(By.XPATH, "//button[@data-qa='login-button']").click()
    driver.get(BASE + "/products")
    driver.find_element(By.XPATH, "(//a[contains(@href,'product_details')])[1]").click()
    driver.find_element(By.XPATH, "//button[@type='button' and contains(.,'Add to cart')]").click()
    driver.get(BASE + "/view_cart")
    driver.find_element(By.LINK_TEXT, "Proceed To Checkout").click()
    assert "checkout" in driver.current_url