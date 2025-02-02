import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Constants
BASE_URL = "https://xaltsocnportal.web.app"
EMAIL = "indulekhatest@gmail.com"
PASSWORD = "Testindu@123"

@pytest.fixture
def driver():
    """Fixture to initialize and teardown the WebDriver."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def wait_for_element(driver, xpath, clickable=False):
    """Wait for an element to be present or clickable."""
    wait = WebDriverWait(driver, 10)
    try:
        if clickable:
            return wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        else:
            return wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    except Exception as e:
        print(f"Error: Element with XPath {xpath} not found or not clickable. Details: {e}")
        raise

def sign_up(driver,cred_data):
    """Sign up a new user."""
    for email_id, password in cred_data:
        try:
            driver.get(BASE_URL)

            wait_for_element(driver, "//button")
            driver.find_element(By.TAG_NAME, "BUTTON").click()

            wait_for_element(driver, "/html/body/div/div/main/div[2]/div[1]/div/input")
            driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/div[1]/div/input").send_keys(email_id)
            driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/div[2]/div/input").send_keys(password)
            driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/div[3]/div/input").send_keys(password)

            wait_for_element(driver, "//button[text()='Sign Up']", clickable=True)
            driver.find_element(By.XPATH, "//button[text()='Sign Up']").click()

            time.sleep(3)
            print("✅ Sign-up successful.")

        except Exception as e:
            print(f"❌ Error during sign-up: {e}")
            raise

def sign_in(driver):
    """Sign in with existing credentials."""
    try:
        driver.get(BASE_URL)
        wait_for_element(driver, "//button")
        driver.find_element(By.TAG_NAME, "BUTTON").click()

        wait_for_element(driver, "/html/body/div/div/main/div[2]/button[2]")
        driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/button[2]").click()

        wait_for_element(driver, "/html/body/div/div/main/div[2]/div[1]/div/input")
        driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/div[1]/div/input").send_keys(EMAIL)
        driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/div[2]/div/input").send_keys(PASSWORD)
        driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/button[1]").click()

        print("✅ Sign-In successful.")
    except Exception as e:
        print(f"Error during sign-in: {e}")
        driver.quit()
        raise

def sign_out(driver):
    """Sign out from the application."""
    try:
        driver.get(BASE_URL)
        time.sleep(5)  # Wait for the page to load
        driver.find_element(By.XPATH, "/html/body/div/div/header/div/button").click()  # Find the sign-out button
        time.sleep(2)  # Wait for the sign-out process to complete
        print("✅ Sign-out successful.")
    except Exception as e:
        print(f"Error during sign-out: {e}")
        raise

def onboard_nodes(driver, nodes_data):
    """Submit requests to onboard multiple nodes to an existing blockchain."""
    try:
        wait_for_element(driver, "/html/body/div/div/main/div/div/div/button", clickable=True)
        driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/div/button").click()

        wait_for_element(driver, "/html/body/div/div/main/section[2]/div/div[1]/h2", clickable=True)
        driver.find_element(By.XPATH, "/html/body/div/div/main/section[2]/div/div[1]/h2").click()
        wait_for_element(driver, "/html/body/div/div/main/section[3]/div/div/div[1]/div[1]/div/input")

        for node_id, public_ip, wallet_address in nodes_data:
            try:
                driver.find_element(By.XPATH, "/html/body/div/div/main/section[3]/div/div/div[1]/div[1]/div/input").send_keys(node_id)
                driver.find_element(By.XPATH, "/html/body/div/div/main/section[3]/div/div/div[1]/div[2]/div/input").send_keys(public_ip)
                driver.find_element(By.XPATH, "/html/body/div/div/main/section[3]/div/div/div[1]/div[3]/button").click()
                print(f"✅ Added node {node_id} to the onboarding blockchain.")
            except Exception as e:
                print(f"Error adding node {node_id}: {e}")

        driver.find_element(By.XPATH, "/html/body/div/div/main/section[3]/div/div/div[1]/button").click()

        for node_id, public_ip, wallet_address in nodes_data:
            try:
                driver.find_element(By.XPATH, "/html/body/div/div/main/section[3]/div/div/div[1]/div[1]/div/input").send_keys(wallet_address)
                driver.find_element(By.XPATH, "/html/body/div/div/main/section[3]/div/div/div[1]/div[2]/button").click()
            except Exception as e:
                print(f"Error adding wallet address for node {node_id}: {e}")

        driver.find_element(By.XPATH, "/html/body/div/div/main/section[3]/div/div/div[1]/div[3]/button[2]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div/main/section[3]/div/div[2]/button[2]").click()
        time.sleep(3)
        print(f"✅ Successfully onboarded node to the blockchain.")
    except Exception as e:
        print(f"Error during node onboarding: {e}")
        raise


def create_private_blockchains(driver, blockchains_data):
    try:
        wait = WebDriverWait(driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/div/div/div/button")))
        button.click()

        wait_for_element(driver, "/html/body/div/div/main/section[2]/div/div[2]/h2", clickable=True)
        driver.find_element(By.XPATH, "/html/body/div/div/main/section[2]/div/div[2]/h2").click()
        time.sleep(2)

        wait_for_element(driver, "/html/body/div/div/main/section[3]/div/div/div[1]/div[1]/div/input")
        driver.find_element(By.XPATH,"/html/body/div/div/main/section[3]/div/div/div[1]/div[1]/div/input").send_keys("Network01")
        driver.find_element(By.XPATH,"/html/body/div/div/main/section[3]/div/div/div[1]/div[2]/div/input").send_keys("0x55Fa61d2fAa13aad8Fbd5b030372b4A159BbBdFB")
        wait_for_element(driver, "/html/body/div/div/main/section[3]/div/div/div[1]/button").click()
        for node_id, node_ip in blockchains_data:
            try:
                wait_for_element(driver, "/html/body/div/div/main/section[3]/div/div/div[1]/div[1]/div/input")
                driver.find_element(By.XPATH, "/html/body/div/div/main/section[3]/div/div/div[1]/div[1]/div/input").send_keys(node_id)
                driver.find_element(By.XPATH, "/html/body/div/div/main/section[3]/div/div/div[1]/div[2]/div/input").send_keys(node_ip)
                wait_for_element(driver, "/html/body/div/div/main/section[3]/div/div/div[1]/div[3]/button").click()
                print(f"✅ Added node {node_id} to the newly creating blockchain.")
            except Exception as e:
                print(f"Error adding node {node_id}: {e}")

        driver.find_element(By.XPATH, "/html/body/div/div/main/section[3]/div/div/div[1]/div[4]/button[2]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div/main/section[3]/div/div[2]/button[2]").click()
        time.sleep(3)
        print(f"✅ Successfully created a private blockchain.")
    except Exception as e:
        print(f"Error during blockchain creation: {e}")
        raise

@pytest.mark.parametrize("cred_data", [
    [
        ("indulekhatest04@gmail.com", "Testindu@1234")
    ]
])

def test_user_journey(driver, cred_data):
    """Test complete user journey: Sign-up → Onboard Nodes → Sign-out."""
    sign_up(driver,cred_data)  # First, sign up a new user
    sign_out(driver)  # Then, sign out

@pytest.mark.parametrize("nodes_data", [
    [
        ("NodeID-1234", "192.168.1.1", "0x88fa61d2faA13aad8Fbd5B030372B4A159BbbDFb"),
        ("NodeID-5678", "172.16.0.2", "0x22Fa61d2Faa13aAD8FbD5b030372B4a159BbbdFb"),
        ("NodeID-91011", "10.0.0.3", "0x33FA61D2FaA13AaD8FBd5B030372B4A159BBBdFb"),
        ("NodeID-1213", "192.168.2.4", "0x44Fa61d2fAa13AaD8fBD5B030372B4A159bbBdFb"),
        ("NodeID-1415", "10.1.1.5", "0x55Fa61d2fAa13aad8Fbd5b030372b4A159BbBdFB"),
        ("NodeID-1617", "172.16.5.6", "0x66Fa61D2fAA13Aad8fBD5B030372b4A159bbbdfb"),
    ]
])

def test_onboard_multiple_nodes(driver, nodes_data):
    """Test onboarding multiple nodes with different data in a single iteration."""
    sign_in(driver)  # Sign in before onboarding
    onboard_nodes(driver, nodes_data)  # Onboard multiple nodes in one go
    sign_out(driver)

@pytest.mark.parametrize("blockchains_data",[
        [
            ("NodeID-1234", "225.0.0.1"),
            ("NodeID-5678", "225.0.0.2"),
            ("NodeID-9101", "225.0.0.3"),
        ]
    ])
def test_create_private_blockchain(driver, blockchains_data):
    """Test creating multiple private blockchains in a single iteration."""
    sign_in(driver)  # Sign in before creating blockchains
    create_private_blockchains(driver, blockchains_data)  # Create multiple blockchains in one go
    sign_out(driver)
