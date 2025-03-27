# File Name : Pokemon.py
# Student Name: Annapoorna Nair
# email:  nairap@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   March 27, 2025
# Course #/Section:   IS4010 Section 001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Add an image and make a data visualization

# We have made the code show us the card of a metapod!
# Citations: There was this article from DZone.com 'How to Display and Convert Images in Python' that I used to ref the image code
# and I asked chatgpt for some formatting help with figuring out sizing

def add_image():
    """
    Helps place in an image of a Metapod
    @returns: a picture of a metapod pokemon card at 200px by 200px
    """
    from PIL import Image
    filename = "Metapod.png"
    image = Image.open('caterpillarPackage/metapod.png')
    image = image.resize((200, 200))
    image.show()
