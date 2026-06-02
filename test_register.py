from selenium.webdriver.common.by import By
import pytest

BASE = "https://www.automationexercise.com"

def test_TC001_valid_registration(driver):
    driver.get(BASE)
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    driver.find_element(By.NAME, "name").send_keys("Hafsa Test")
    driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("230942@students.au.edu.pk")
    driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()
    assert "Signup" in driver.page_source

def test_TC002_existing_email(driver):
    driver.get(BASE + "/login")
    driver.find_element(By.NAME, "name").send_keys("Hafsa Test")
    driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("230942@students.au.edu.pk")
    driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()
    assert "Email Address already exist" in driver.page_source

def test_TC003_empty_name(driver):
    driver.get(BASE + "/login")
    driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("230942@students.au.edu.pk")
    driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()
    assert "login" in driver.current_url

def test_TC004_empty_email(driver):
    driver.get(BASE + "/login")
    driver.find_element(By.NAME, "name").send_keys("Hafsa Test")
    driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()
    assert "login" in driver.current_url

def test_TC005_invalid_email(driver):
    driver.get(BASE + "/login")
    driver.find_element(By.NAME, "name").send_keys("Hafsa Test")
    driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("notanemail")
    driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()
    assert "login" in driver.current_url

def test_TC006_register_then_logout(driver):
    driver.get(BASE + "/login")
    driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys("230942@students.au.edu.pk")
    driver.find_element(By.XPATH, "//input[@data-qa='login-password']").send_keys("hafsa@9506")
    driver.find_element(By.XPATH, "//button[@data-qa='login-button']").click()
    driver.find_element(By.LINK_TEXT, "Logout").click()
    assert "login" in driver.current_url