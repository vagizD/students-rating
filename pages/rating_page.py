import logging

from selenium_project_lms_rating.locators.rating_locators import RatingLocators

from selenium.webdriver.common.by import By

logger = logging.getLogger('app.script.rating_page')


class RatingPage:
    def __init__(self, browser, actor):
        self.browser = browser
        self.actor = actor

    @property
    def rating_button(self):
        locator = RatingLocators.RATING_BUTTON
        return self.browser.find_element(By.CSS_SELECTOR, locator)

    def click_rating_button(self):
        logger.info('Clicking on rating button.')
        self.actor.click(self.rating_button).perform()
