from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait



class Browser:
    """Provide access to a singleton instance of a Selenium web driver.

    Methods:
    get_browser(cls)  class method that returns a singleton instance of a WebDriver
    """
    _browser = None


    @staticmethod
    def get_browser():
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        if Browser._browser is None:
            Browser._browser = webdriver.Chrome(options=options)
        return Browser._browser
Browser.get_browser()


def login(browser: webdriver, url: str, username: str, password: str) -> webdriver:
    """Login with specified username and password.
    Args:
        browser: browser object that is initialized.
        url: login url.
        username: user's username.
        password: user's password.
    Returns:
        browser object that is logged in.
    """
    browser.get(url)
    username_box = browser.find_element_by_xpath('//*[@id="id_login"]')
    username_box.send_keys(username)
    password_box = browser.find_element_by_xpath('//*[@id="id_password"]')
    password_box.send_keys(password)
    # click login button
    browser.find_element_by_xpath('/html/body/div/div[1]/div/div/div/div[2]/form/div[3]/button').click()
    return browser

