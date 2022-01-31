import logging

import matplotlib.pyplot as plt
import seaborn as sns

logger = logging.getLogger('app.visualize')


def plot_average_grade(students):
    logger.info("Plotting average grade distribution.")
    fig, ax = plt.subplots(figsize=(15, 7))

    x = [student.average_grade for student in students]
    ax = sns.kdeplot(x=x, color='salmon', fill=True)

    ax.set(title="Average grade distribution.",
           ylabel="Probability density.",
           xlabel="Average grade.",
           xlim=(0,10))

    ax.grid(b=True, alpha=0.7, linestyle="--")
    plt.show()


def plot_minimal_grade(students):
    logger.info("Plotting minimal grade distribution.")
    fig, ax = plt.subplots(figsize=(15, 7))

    x = [student.minimal_grade for student in students]
    ax = sns.kdeplot(x=x, color="blue", fill=True)

    ax.set(title="Minimal grade distribution.",
           xlabel="Minimal grade.",
           ylabel="Probability density.",
           xlim=(0,10),
           ylim=(0,0.3))

    ax.grid(b=True, alpha=0.7, linestyle="--")
    plt.show()


def plot_cr_amount_norm(students):
    logger.info("Plotting credits amount after normalization distribution.")
    fig, ax = plt.subplots(figsize=(15, 7))

    x = [student.cr_amount_norm for student in students]
    ax = sns.kdeplot(x=x, color="green", fill=True)

    ax.set(title="Credits amount after normalization distribution.",
           xlabel="Credits after normalization.",
           ylabel="Probability density.",
           xlim=(0,300),
           ylim=(0,0.01))

    ax.grid(b=True, alpha=0.7, linestyle="--")

    plt.show()
