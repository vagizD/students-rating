import logging

from selenium_project_lms_rating.locators.LMS_home_page_locators import LMSHomePageLocators

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

logger = logging.getLogger('app.script.LMS_home_page')


class LMSHomePage:
    def __init__(self, browser, actor):
        self.browser = browser
        self.actor = actor

    @property
    def gradebook_button(self):
        locator = LMSHomePageLocators.GRADEBOOK_BUTTON
        return self.browser.find_element(By.CSS_SELECTOR, locator)

    def click_gradebook_button(self):
        WebDriverWait(self.browser, 10).until(
            expected_conditions.visibility_of_element_located(
                (By.CSS_SELECTOR, LMSHomePageLocators.GRADEBOOK_BUTTON)
            )
        )
        logger.info('Clicking on gradebook button.')
        self.actor.click(self.gradebook_button).perform()
