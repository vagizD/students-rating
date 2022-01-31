import logging

from bs4 import BeautifulSoup

from unidecode import unidecode

from selenium_project_lms_rating.locators.students_locators import StudentsLocators
from selenium_project_lms_rating.errors.errors import ParsingError

logger = logging.getLogger('app.script.students')


class StudentsRatings:
    """
    Takes WebDriver instance as a parent.
    """

    def __init__(self, browser):
        self.browser = browser
        logger.info('Using bs4 instead of Selenium.')
        self.soup = BeautifulSoup(self.browser.page_source, 'html.parser')

    @property
    def students(self):
        students_table = self.soup.find(id=StudentsLocators.STUDENTS_TABLE_ID)
        students_info = students_table.find_all(StudentsLocators.STUDENTS)
        logger.info('Creating list of students of length: {length}.'.format(length=len(students_info)))
        try:
            return [StudentParser(student_info) for student_info in students_info[:-1]]
        except Exception:
            raise ParsingError("Problem in retrieving info from rating page.")
        except ParsingError as e:
            print(e)
            logger.info('Got an error.')


class StudentParser:
    """
    Takes StudentRatings object as a parent.

    Student info with attributes: rating, name, learn program, course, academic group, CR amount,
    CR amount norm, Normalization factor, Credits summary, Percentile, Average grade, Minimal grade,
    Learn group position.
    """
    def __init__(self, info):
        self.info = info
        logger.debug('Creating attributes for student.')
        self.attributes = [unidecode(str(e.string))for e in self.info.find_all(StudentsLocators.INFO)]

    def __repr__(self):
        logger.debug('Running __repr__ of StudentParser.')
        return f"Rating: {self.rating}, name: {self.name}, credits: {self.cr_amount_norm}"

    @property
    def rating(self) -> int:
        return int(self.attributes[0])

    @property
    def name(self) -> str:
        return self.attributes[1]

    @property
    def learn_program(self) -> str:
        return self.attributes[2]

    @property
    def course(self) -> int:
        return int(self.attributes[3])

    @property
    def academic_group(self) -> str:
        return self.attributes[4]

    @property
    def cr_amount(self) -> int:
        return int(round(float(self.attributes[5])))

    @property
    def cr_amount_norm(self) -> int:
        return int(round(float(self.attributes[6])))

    @property
    def normalization_factor(self) -> float:
        return float(self.attributes[7])

    @property
    def credits_summary(self) -> int:
        return int(self.attributes[8])

    @property
    def percentile(self) -> float:
        return float(self.attributes[9])

    @property
    def average_grade(self) -> float:
        return float(self.attributes[10])

    @property
    def minimal_grade(self) -> int:
        return int(self.attributes[11])

    @property
    def learn_group_position(self) -> str:
        return self.attributes[12]
