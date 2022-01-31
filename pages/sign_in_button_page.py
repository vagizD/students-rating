import logging

from selenium_project_lms_rating.locators.sign_in_button_locators import SignInButtonLocators

from selenium.webdriver.common.by import By

logger = logging.getLogger('app.script.sign_in_button_page')


class SignInButtonPage:
    def __init__(self, browser, actor):
        self.browser = browser
        self.actor = actor

    @property
    def sign_in_button(self):
        locator = SignInButtonLocators.SIGN_IN_BUTTON
        return self.browser.find_element(By.CSS_SELECTOR, locator)

    def click_sign_in_button(self):
        logger.info('Clicking on sign in button.')
        self.actor.click(self.sign_in_button).perform()
