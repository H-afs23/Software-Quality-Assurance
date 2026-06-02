from selenium.webdriver.common.by import By

BASE = "https://www.automationexercise.com"

def test_TC007_valid_login(driver):
    driver.get(BASE + "/login")
    driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys("230942@students.au.edu.pk")
    driver.find_element(By.XPATH, "//input[@data-qa='login-password']").send_keys("hafsa@9506")
    driver.find_element(By.XPATH, "//button[@data-qa='login-button']").click()
    assert "Logged in as" in driver.page_source

def test_TC008_wrong_password(driver):
    driver.get(BASE + "/login")
    driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys("hafsa_test123@gmail.com")
    driver.find_element(By.XPATH, "//input[@data-qa='login-password']").send_keys("wrongpass")
    driver.find_element(By.XPATH, "//button[@data-qa='login-button']").click()
    assert "Your email or password is incorrect" in driver.page_source

def test_TC009_wrong_email(driver):
    driver.get(BASE + "/login")
    driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys("fake@fake.com")
    driver.find_element(By.XPATH, "//input[@data-qa='login-password']").send_keys("anypassword")
    driver.find_element(By.XPATH, "//button[@data-qa='login-button']").click()
    assert "Your email or password is incorrect" in driver.page_source

def test_TC010_both_fields_empty(driver):
    driver.get(BASE + "/login")
    driver.find_element(By.XPATH, "//button[@data-qa='login-button']").click()
    assert "login" in driver.current_url

def test_TC011_logout_after_login(driver):
    driver.get(BASE + "/login")
    driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys("230942@students.au.edu.pk")
    driver.find_element(By.XPATH, "//input[@data-qa='login-password']").send_keys("hafsa@9506")
    driver.find_element(By.XPATH, "//button[@data-qa='login-button']").click()
    driver.find_element(By.LINK_TEXT, "Logout").click()
    assert "login" in driver.current_url

def test_TC012_login_page_loads(driver):
    driver.get(BASE + "/login")
    assert "Login" in driver.page_source
    assert "Signup" in driver.page_source