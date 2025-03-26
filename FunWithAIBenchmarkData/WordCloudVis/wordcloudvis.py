# File Name: wordcloudvis.py
# Student Name: Eirlys Vo
# email: vopq@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: March 26th, 2025
# Course #/Section: IS 4010 - 001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Work with AI Benchmark Data and create data visualizations
# Brief Description of what this module does: This module works with CSV data and outside Python libraries.
# Citations: https://www.geeksforgeeks.org/generating-word-cloud-python/
# Anything else that's relevant: N/A

from wordcloud import WordCloud
import matplotlib.pyplot as plt

def create_wordcloud(text):
    """
    Create a word cloud from the given text.
    @param String text: The text to create the word cloud from.
    @return: None
    """

    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')  
    plt.title("IMDB Movie Reviews Word Cloud")
    plt.show()
