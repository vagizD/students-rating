import logging

from selenium_project_lms_rating.locators.login_locators import LoginLocators
from selenium_project_lms_rating.login_info.login_info import LoginInfo

from selenium.webdriver.common.by import By

logger = logging.getLogger('app.script.login_page')


class LoginPage:
    def __init__(self, browser, actor):
        self.browser = browser
        self.actor = actor

    @property
    def username_gap(self):
        locator = LoginLocators.USERNAME
        return self.browser.find_element(By.CSS_SELECTOR, locator)

    @property
    def password_gap(self):
        locator = LoginLocators.PASSWORD
        return self.browser.find_element(By.CSS_SELECTOR, locator)

    @property
    def login_button(self):
        locator = LoginLocators.SIGN_IN_BUTTON
        return self.browser.find_element(By.CSS_SELECTOR, locator)

    def input_username(self):
        self.actor.send_keys_to_element(self.username_gap, LoginInfo.USERNAME_INFO).perform()

    def input_password(self):
        self.actor.send_keys_to_element(self.password_gap, LoginInfo.PASSWORD_INFO).perform()

    def click_login_button(self):
        self.actor.click(self.login_button).perform()

    def login(self):
        logger.info('Typing username in.')
        self.input_username()
        logger.info('Typing password in.')
        self.input_password()
        logger.info('Clicking login button.')
        self.click_login_button()
