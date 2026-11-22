from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger
import traceback
from time import sleep



WEBSITE = "https://docs.google.com/forms/d/e/1FAIpQLSdBb-1vu3vfokLHCGPj6YcYVSmOV1WRjsqpQM_C7ZuBv4LtcA/viewform?usp=dialog"


class GoogleForms:
    def __init__(self):
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--log-level=3")  # keep only FATAL
        options.add_experimental_option("excludeSwitches", ["enable-logging"])  # kills these metrics logs
        options.add_experimental_option("useAutomationExtension", False)
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10) # Page Load
        self.driver.get(WEBSITE)


    def wait_element(self, by: str, value: str):
        return self.wait.until(EC.visibility_of_element_located((by, value)))


    def fill_form(self, coin, price, country):
        """
        Input all the data here as strings
        """
        try:
            # Wait the page loads
            self.wait_element(By.CSS_SELECTOR, ".whsOnd.zHQkBf")

            #sleep(1)

            self.coin_field = self.driver.find_element(By.CSS_SELECTOR, ".whsOnd.zHQkBf")
            self.coin_field.send_keys(coin)

            self.price_field = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            self.price_field.send_keys(price)

            if country.lower() == 'brasil':
                self.driver.find_element(By.ID, 'i31').click()
            
            elif country.lower() == 'portugal':
                self.driver.find_element(By.ID, 'i34').click()

            elif country.lower() == 'franca':
                self.driver.find_element(By.ID, 'i37').click()
                

        except Exception as e:
            logger.error(f"fill_form error: {e}\n{traceback.format_exc()}")
                


    def submit_form(self):
        self.submit_btn = self.driver.find_element(By.XPATH, '//*[@class="NPEfkd RveJvd snByac" and contains(text(), "Enviar")]')
        self.submit_btn.click()

        self.wait_element(By.LINK_TEXT, 'Enviar outra resposta')
        self.submit_other = self.driver.find_element(By.LINK_TEXT, 'Enviar outra resposta')
        self.submit_other.click()