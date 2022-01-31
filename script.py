import logging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

from selenium_project_lms_rating.pages.sign_in_button_page import SignInButtonPage
from selenium_project_lms_rating.pages.login_page import LoginPage
from selenium_project_lms_rating.pages.LMS_home_page import LMSHomePage
from selenium_project_lms_rating.pages.rating_page import RatingPage

from selenium_project_lms_rating.errors.errors import ScriptError

from selenium_project_lms_rating.parsers.students import StudentsRatings


def execute_script():
    """
    Executes script with selenium and bs4.
    :return: list of StudentParser objects.
    """
    URL = ''
    PATH = ''
    service = Service(executable_path=PATH)
    chrome = webdriver.Chrome(service=service)
    actor = ActionChains(driver=chrome)


    logger = logging.getLogger('app.script')

    try:
        logger.info('Navigating to %(url)s' % {"url": URL})
        chrome.get(URL)

        sign_in_button_page = SignInButtonPage(chrome, actor)
        sign_in_button_page.click_sign_in_button()

        login_page = LoginPage(chrome, actor)
        login_page.login()

        LMS_home_page = LMSHomePage(chrome, actor)
        LMS_home_page.click_gradebook_button()

        rating_page = RatingPage(chrome, actor)
        rating_page.click_rating_button()

        students = StudentsRatings(chrome)
        logger.info('Shutting %(webdriver)s down.' % {"webdriver": chrome})
        chrome.close()
        logger.info("Returning list of students.")
        return students.students
    except ScriptError as e:
        print(e)
        chrome.close()
