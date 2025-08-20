import asyncio
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

class BrowserManager():
    def __init__(self):
        self.driver = None

    def start_browser(self, headless: bool = False):
        if self.driver is not None:
            try:
                self.driver.title  
                return self.driver
            except WebDriverException:
                self.driver.quit()
                self.driver = None

        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless=new")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        return self.driver

    async def open_url(self, url: str) -> str:
        if not self.driver:
            self.start_browser()
        await asyncio.to_thread(self.driver.get, url)
        return f"opened {url}"
    
    async def get_title(self) -> str:
        if not self.driver:
            self.start_browser()
        return await asyncio.to_thread(lambda: self.driver.title)
    
    async def click(self, ID: str) -> str:
        if not self.driver:
            self.start_browser()
        return await asyncio.to_thread(lambda: self.driver.find_element(By.ID, ID).click)
    
    async def send_keys(self, ID: str, value: str) ->str:
        if not self.driver:
            self.start_browser()
        def _send():
            text_field = self.driver.find_element(By.ID, ID)
            text_field.clear()
            text_field.send_keys(value)
        return await asyncio.to_thread(_send)
        
    
    def stop_browser(self):
        if self.driver:
            try:
                self.driver.quit()
            except Exception:
                pass
            self.driver = None
