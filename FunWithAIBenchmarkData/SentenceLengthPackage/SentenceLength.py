# File Name: Pokemon.py
# Student Name: Eirlys Vo
# email: vopq@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: March 27, 2025
# Course #/Section: IS4010 Section 001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Add an image of group name and make some data visualization. We have made the code show us the card of a metapod and 2 data visualizations on the prompts.
# Brief Description of what this module does: This module works with CSV data and outside Python libraries.
# Citations: Seaborn library - https://seaborn.pydata.org/generated/seaborn.histplot.html; Matplotlib library - https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html; I use ChatGPT for idea

import matplotlib.pyplot as plt
import seaborn as sns

def sentence_length_graph(questions, ax):
    """
    Create histogram of sentence lengths for prompts
    @param questions: list of dictionaries containing prompts
    @param ax: axis to plot on
    @return: None
    """
    sentence_lengths = [len(q['prompt']) for q in questions]
    sns.set(style="whitegrid")
    sns.histplot(sentence_lengths, bins=20, kde=True)
    plt.xlabel("Sentence Length (Words)")
    plt.ylabel("Frequency")
