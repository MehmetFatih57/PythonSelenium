from selenium import webdriver
from utilitiessss import ConfigReader
from selenium.webdriver.chrome.options import Options

def get_driver(flag=False):
    driver = None
    option = None
    if flag:
        option = Options()
        option.add_argument("--headless")
    browser = ConfigReader.read_config("browser")
    try:
        match browser:
            case "chrome":
                driver = webdriver.Chrome()
            case "firefox":
                driver = webdriver.Firefox()
            case "edge":
                driver = webdriver.Edge()
            case "safari":
                driver = webdriver.Safari()
            case _:
                raise Exception("Invalid browser")
    except Exception as e:
        print(e)
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver


def close_driver(self):
    self.driver.quit()
