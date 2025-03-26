# File Name: wordcloudvis.py
# Student Name: Eirlys Vo
# email: vopq@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: Mar 26th, 2025
# Course #/Section: IS4010 - 001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Work with benchmark data and perform some data visualizations on it.
# Brief Description of what this module does: Work with more outside coding libraries and read CSV data files.
# Citations: https://www.geeksforgeeks.org/generating-word-cloud-python/ 
# Anything else that's relevant:

from wordcloud import WordCloud
import matplotlib.pyplot as plt

def create_word_cloud(text):
    """
    Create word cloud image from the given text
    @param text: string of text that needs to create word cloud
    @return: None
    """
    wordcloud = WordCloud(width = 800, height = 400, background_color = 'white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()