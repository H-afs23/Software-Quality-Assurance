from selenium.webdriver.common.by import By

BASE = "https://www.automationexercise.com"

def test_TC013_search_valid_product(driver):
    driver.get(BASE + "/products")
    driver.find_element(By.ID, "search_product").send_keys("dress")
    driver.find_element(By.ID, "submit_search").click()
    assert "dress" in driver.page_source.lower()

def test_TC014_search_no_results(driver):
    driver.get(BASE + "/products")
    driver.find_element(By.ID, "search_product").send_keys("xyzabc999")
    driver.find_element(By.ID, "submit_search").click()
    assert "searched" in driver.page_source.lower()

def test_TC015_search_empty(driver):
    driver.get(BASE + "/products")
    driver.find_element(By.ID, "submit_search").click()
    assert "products" in driver.current_url

def test_TC016_product_detail_opens(driver):
    driver.get(BASE + "/products")
    driver.find_element(By.XPATH, "(//a[contains(@href,'product_details')])[1]").click()
    assert "product_details" in driver.current_url

def test_TC017_products_page_loads(driver):
    driver.get(BASE + "/products")
    assert "All Products" in driver.page_source

def test_TC018_case_insensitive_search(driver):
    driver.get(BASE + "/products")
    driver.find_element(By.ID, "search_product").send_keys("DRESS")
    driver.find_element(By.ID, "submit_search").click()
    assert "dress" in driver.page_source.lower()