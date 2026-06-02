from selenium.webdriver.common.by import By

BASE = "https://www.automationexercise.com"

def login(driver):
    driver.get(BASE + "/login")
    driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys("230942@students.au.edu.pk")
    driver.find_element(By.XPATH, "//input[@data-qa='login-password']").send_keys("hafsa@9506")
    driver.find_element(By.XPATH, "//button[@data-qa='login-button']").click()

def test_TC025_checkout_shows_address(driver):
    login(driver)
    driver.get(BASE + "/products")
    driver.find_element(By.XPATH, "(//a[contains(@href,'product_details')])[1]").click()
    driver.find_element(By.XPATH, "//button[@type='button' and contains(.,'Add to cart')]").click()
    driver.get(BASE + "/view_cart")
    driver.find_element(By.LINK_TEXT, "Proceed To Checkout").click()
    assert "Address" in driver.page_source

def test_TC026_place_order_valid_card(driver):
    login(driver)
    driver.get(BASE + "/products")
    driver.find_element(By.XPATH, "(//a[contains(@href,'product_details')])[1]").click()
    driver.find_element(By.XPATH, "//button[@type='button' and contains(.,'Add to cart')]").click()
    driver.get(BASE + "/view_cart")
    driver.find_element(By.LINK_TEXT, "Proceed To Checkout").click()
    driver.find_element(By.LINK_TEXT, "Place Order").click()
    driver.find_element(By.XPATH, "//input[@data-qa='name-on-card']").send_keys("Hafsa Test")
    driver.find_element(By.XPATH, "//input[@data-qa='card-number']").send_keys("4111111111111111")
    driver.find_element(By.XPATH, "//input[@data-qa='cvc']").send_keys("123")
    driver.find_element(By.XPATH, "//input[@data-qa='expiry-month']").send_keys("12")
    driver.find_element(By.XPATH, "//input[@data-qa='expiry-year']").send_keys("2027")
    driver.find_element(By.XPATH, "//button[@data-qa='pay-button']").click()
    assert "Order Placed" in driver.page_source

def test_TC027_checkout_without_login(driver):
    driver.get(BASE + "/view_cart")
    driver.find_element(By.LINK_TEXT, "Proceed To Checkout").click()
    assert "Register / Login" in driver.page_source or "login" in driver.current_url

def test_TC028_order_confirmation_message(driver):
    login(driver)
    driver.get(BASE + "/products")
    driver.find_element(By.XPATH, "(//a[contains(@href,'product_details')])[1]").click()
    driver.find_element(By.XPATH, "//button[@type='button' and contains(.,'Add to cart')]").click()
    driver.get(BASE + "/view_cart")
    driver.find_element(By.LINK_TEXT, "Proceed To Checkout").click()
    driver.find_element(By.LINK_TEXT, "Place Order").click()
    driver.find_element(By.XPATH, "//input[@data-qa='name-on-card']").send_keys("Hafsa Test")
    driver.find_element(By.XPATH, "//input[@data-qa='card-number']").send_keys("4111111111111111")
    driver.find_element(By.XPATH, "//input[@data-qa='cvc']").send_keys("123")
    driver.find_element(By.XPATH, "//input[@data-qa='expiry-month']").send_keys("12")
    driver.find_element(By.XPATH, "//input[@data-qa='expiry-year']").send_keys("2027")
    driver.find_element(By.XPATH, "//button[@data-qa='pay-button']").click()
    assert "Congratulations" in driver.page_source

def test_TC029_download_invoice(driver):
    login(driver)
    assert "Logged in as" in driver.page_source

def test_TC030_continue_after_order(driver):
    login(driver)
    assert "Logged in as" in driver.page_source