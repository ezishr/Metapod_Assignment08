# main.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu

import string
from readingLevelPackage.readingLevel import Reading_Level
from utilitiesPackage.utilities import *
from utilitiesPackage.CSV_Utilities import *
from PDFPackage.PDFUtilities import *

from Metapodpackage.Pokemon import * # Import Metapodpackage to add image

from wordcloud import WordCloud # Import WordCloud and Matplotlib to create wordcloud visualization
import matplotlib.pyplot as plt

from SentenceLengthPackage.SentenceLength import * # Import SentenceLengthPackage to create sentence length visualization

if __name__ == "__main__":

    CSV_Processor = MMLU_CSV_Processor("dataPackage/MMLU/data/", ["management_test.csv"])
    questions = CSV_Processor.read_data()
    print(len(questions), "questions read")

 
    myPDF = PDFUtilities()
    myPDF.create_question_PDF("Management Test", "MMLU", questions)
   
    print("The first question:")
    print(questions[0])
    
    text = convert_dictionaries_to_string(questions, ["prompt", "possible answers"])
    print("\nText from dictionaries:", text[0:500])
    #print("\ntext from dictionaries:", text[0:500])

    #0. Append all the prompts into a big string - See utilities.convert_dictionaries_to_string()
    
    #1. Perform reading level analysis on the big string and print the results to the console.
    Reading_Level.compute_readability_indices("MMLU", text)

    #2. Process the big string to find the longest word

    #3. Process the big string to find the most prevalent word

    #4. Use the VS debugger: set a breakpoint somewhere to pause the project when a prompt containing the word "PEST" is read from the original CSV file

    #5. Perform some data visualization on the text. Research Data Vis libraries and apply one.

    # Create a word cloud
    wordcloud = WordCloud(
        width = 800,
        height = 400,
        background_color = 'white'
    ).generate(text)

    #6a. Write all the questions and possible answers (with unique identifier field for each question.
    #6b. Write the question identifier (see 6a, above) and the cohout the correct answer) to a text file. Use a CSV format and create arrect answer to another text file. Use a CSV format.
    questions_written = write_questions_to_text_files("MMLU", questions)
    print(questions_written, "questions written to the file.")
    
    """
    # This code is commented out
    #Reading_Level.test01()

    text = "This is a sentence that we can use to test the reading level computations. "
    reading_level_indices = Reading_Level.compute_readability_indices("Dummy Benchmark", text)
    for key in reading_level_indices.keys():
        print(key, ":", reading_level_indices[key])
            
    # A test with text at a higher reading level
    text = "Birds, employing a combination of aerodynamic principles and specialized anatomical adaptations, achieve flight through the generation of lift, which counteracts the force of gravity."
    reading_level_indices = Reading_Level.compute_readability_indices("Dummy Benchmark", text)
    for key in reading_level_indices.keys():
        print(key, ":", reading_level_indices[key])
    """

    # Add 3 visualizations to the same figure using matplotlib.pyplot
    fig, axes = plt.subplots(1, 3, figsize=(12, 5))

    axes[0].imshow(wordcloud, interpolation='bilinear')
    axes[0].axis("off")
    axes[0].set_title("Word Cloud")
    
    add_image(axes[1])
    axes[1].set_title("Metapod Image")

    sentence_length_graph(questions, axes[2])
    axes[2].set_title("Sentence Length Distribution")

    plt.tight_layout()
    plt.show()
