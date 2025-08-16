import asyncio
from selenium import webdriver
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
    
    def stop_browser(self):
        if self.driver:
            try:
                self.driver.quit()
            except Exception:
                pass
            self.driver = None
