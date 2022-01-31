import logging

import numpy as np

from scipy import stats


logger = logging.getLogger('app.retrieve')


def retrieve_average_grade(students):
    logger.info('Retrieving average grade stats.')
    array = np.array([student.average_grade for student in students])
    std = np.std(array)
    median = np.median(array)
    mean = np.mean(array)
    mode = stats.mode(array)[0][0]
    print("Average grade stats.")
    print(f"Mean: {mean:.3f}, mode: {mode:.3f}, standard deviation: {std:.3f}, median: {median:.3f}.")


def retrieve_minimal_grade(students):
    logger.info('Retrieving minimal grade stats.')
    array = np.array([student.minimal_grade for student in students])
    std = np.std(array)
    median = np.median(array)
    mean = np.mean(array)
    mode = stats.mode(array)[0][0]
    print("Minimal grade stats.")
    print(f"Mean: {mean:.3f}, mode: {mode:.3f}, standard deviation: {std:.3f}, median: {median:.3f}.")


def retrieve_cr_amount_norm(students):
    logger.info('Retrieving credits after normalization stats.')
    array = np.array([student.cr_amount_norm for student in students])
    std = np.std(array)
    median = np.median(array)
    mean = np.mean(array)
    mode = stats.mode(array)[0][0]
    print("Credits after normalization stats.")
    print(f"Mean: {mean:.3f}, mode: {mode:.3f}, standard deviation: {std:.3f}, median: {median:.3f}.")
