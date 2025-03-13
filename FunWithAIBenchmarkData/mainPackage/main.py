# main.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu

import string
from readingLevelPackage.readingLevel import Reading_Level
from utilitiesPackage.utilities import *
from utilitiesPackage.CSV_Utilities import *
from PDFPackage.PDFUtilities import *

if __name__ == "__main__":

    CSV_Processor = MMLU_CSV_Processor("dataPackage/MMLU/data/", ["management_test.csv"])
    questions = CSV_Processor.read_data()
    print(len(questions), "questions read")

 
    myPDF = PDFUtilities()
    myPDF.create_question_PDF("Management Test", "MMLU", questions)
   
    print("The first question:")
    print(questions[0])
    
    text = convert_dictionaries_to_string(questions, ["prompt", "possible answers"])
    #print("\ntext from dictionaries:", text[0:500])

    #0. Append all the prompts into a big string - See utilities.convert_dictionaries_to_string()
    
    prompt_text = ""
    for i in range(0, len(questions)):
        prompt_text += " " + questions[i]["prompt"]

    print('\n\nprompt_text:', prompt_text)
    
    #1. Perform reading level analysis on the big string and print the results to the console.
    Reading_Level.compute_readability_indices("MMLU", text)

    #2. Process the big string to find the longest word
    import re
    list_words = re.findall(r'\b\w+\b', prompt_text)
    max_len = 0
    longest_word = ""
    for word in list_words:
        if len(word) > max_len:
            max_len = len(word)
            longest_word = word
    print('\nlongest word:', longest_word, 'length:', max_len)


    #3. Process the big string to find the most prevalent word
    

    #4. Use the VS debugger: set a breakpoint somewhere to pause the project when a prompt containing the word "PEST" is read from the original CSV file
    

    #5. Perform some data visualization on the text. Research Data Vis libraries and apply one.
     

    #6a. Write all the questions and possible answers (without the correct answer) to a text file. Use a CSV format and create a unique identifier field for each question.
    #6b. Write the question identifier (see 6a, above) and the correct answer to another text file. Use a CSV format.
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
