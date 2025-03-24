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
    
    ## Starting
    prompt_text = " ".join(q['prompt'].lower() for q in questions)
    ## Ending
    
    #1. Perform reading level analysis on the big string and print the results to the console.
    
    ## Starting
    Reading_Level.compute_readability_indices("MMLU", text)
    ## Ending

    #2. Process the big string to find the longest word

    ## Starting
    import re
    list_words = re.findall(r'\b\w+\b', prompt_text)
    max_len = 0
    longest_word = ""
    for word in list_words:
        if len(word) > max_len:
            max_len = len(word)
            longest_word = word
    print('\nLongest word:', longest_word, '\nLength:', max_len)
    ## Ending

    #3. Process the big string to find the most prevalent word
    
    ## Starting
    dic_words = {}
    for word in list_words:
        if word not in dic_words:
            dic_words[word] = 1
        else:
            dic_words[word] += 1
    print('\nMost prevalent word:', max(dic_words, key=dic_words.get), '\nNumber of occurrences:', dic_words[max(dic_words, key=dic_words.get)])
    ## Ending

    #4. Use the VS debugger: set a breakpoint somewhere to pause the project when a prompt containing the word "PEST" is read from the original CSV file
    
    ## Starting
    ## Ending

    #5. Perform some data visualization on the text. Research Data Vis libraries and apply one.
     
    ## Starting
    #### NOT DONE
    from wordcloud import WordCloud
    wordcloud = WordCloud.generate(prompt_text)
    import matplotlib.pyplot as plt
    plt.imshow(wordcloud, interpolation='bilinear')
    ## Ending

    #6a. Write all the questions and possible answers (wit unique identifier field for each question.
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
