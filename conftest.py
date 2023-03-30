import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    driver_service = Service(ChromeDriverManager().install())            #create service
    driver = webdriver.Chrome(service=driver_service)          #create driver
    driver.maximize_window()
    #driver.set_window_size(480,640)

    yield driver        # return driver (instead return) so
    driver.quit()       #we are need quit from driver