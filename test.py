from selenium import webdriver
from selenium.webdriver.common.by import By
import re
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class HomePage:

    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.about = (By.XPATH,"//div[@id='global_header']//div[contains(@class, 'content')]//div[contains(@class, 'supernav_container')]//a[@class='menuitem'][1]")[0]
        self.store = (By.XPATH,"//div[@id='global_header']//div[contains(@class, 'content')]//div[contains(@class, 'supernav_container')]//a[contains(@class,'supernav')][1]")[0]
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)


    def navigate_to_main_page(self):
        return self.driver.get('https://store.steampowered.com/')

    def do_click_about(self):
        about = self.driver.find_element(self.about)     
        return about.click()

    def get_playing_now(self):
        loc_playing_now = self.driver.find_elements(By.XPATH,"//div[(@class='online_stats')]//div[(@class='online_stat')][2]")
        playing_now = int("".join(re.findall(r"\d+", loc_playing_now[0].text)))
        return playing_now   
        
    def get_online_players(self):
        loc_online_players = self.driver.find_elements(By.XPATH,"//div[(@class='online_stats')]//div[(@class='online_stat')][1]")
        online_players = (int("".join(re.findall(r"\d+", loc_online_players[0].text))))
        return online_players    

    def do_click_store(self):   
        store = self.driver.find_element(self.store)     
        return store.click()
