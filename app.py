"""
Here user is able to:
    1. Save data to json / sql database.
    2. Visualize data by selecting the desired features.
    3. Retrieve information about students with most / least educational indicators.
"""

import logging
import timeit
import time

from script import execute_script
from selenium_project_lms_rating.app_tools.menu import Menu
from selenium_project_lms_rating.app_tools import save, visualize, retrieve

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s: line %(lineno)d] %(message)s',
    level=logging.INFO,
    filename='/Users/vagiz/PycharmProjects/pythonProject/selenium_project_lms_rating/logs/script_logs.txt',
    filemode='w'
)

logger = logging.getLogger('app')
logger.info("Starting application.")


students = []
script_execution = False


def _menu():
    global students
    global script_execution
    menu_choice = input(Menu.USER_MENU)
    if menu_choice in USER_MENU_OPTIONS:
        if menu_choice != "e":
            letter = input(USER_MENU_OPTIONS[menu_choice][0])
            if letter in USER_MENU_OPTIONS[menu_choice][1]:
                if letter != "p":
                    if not script_execution:
                        script_execution = True
                        logger.info("Starting script.")
                        print("Executing script...")
                        start = timeit.default_timer()
                        students = execute_script()
                        end = timeit.default_timer()
                        print(f"Runtime: {end - start:.3f} seconds.")
                        logging.info(f"Script runtime: {end - start:.3f} seconds.")
                        USER_MENU_OPTIONS[menu_choice][1][letter](students)
                    else:
                        USER_MENU_OPTIONS[menu_choice][1][letter](students)
        else:
            logger.info("Closing application.")
            USER_MENU_OPTIONS[menu_choice]()
    else:
        print("Invalid command.")
        time.sleep(1)
        _menu()
    _menu()


SAVE_MENU_OPTIONS = {
    "j": save.save_to_json,
    "d": save.save_to_database,
    "p": _menu
}

VISUALIZE_MENU_OPTIONS = {
    "a": visualize.plot_average_grade,
    "m": visualize.plot_minimal_grade,
    "c": visualize.plot_cr_amount_norm,
    "p": _menu
}

RETRIEVE_MENU_OPTIONS = {
    "a": retrieve.retrieve_average_grade,
    "m": retrieve.retrieve_minimal_grade,
    "c": retrieve.retrieve_cr_amount_norm,
    "p": _menu
}

USER_MENU_OPTIONS = {
    "s": [Menu.SAVE_MENU, SAVE_MENU_OPTIONS],
    "v": [Menu.VISUALIZE_MENU, VISUALIZE_MENU_OPTIONS],
    "r": [Menu.RETRIEVE_MENU, RETRIEVE_MENU_OPTIONS],
    "e": exit
}

_menu()
