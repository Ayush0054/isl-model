import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
import string

def display_image(image_path):
    ImageItself = Image.open(image_path)
    ImageNumpyFormat = np.asarray(ImageItself)
    plt.imshow(ImageNumpyFormat)
    plt.show()

def func(text_input):
    isl_gif = ['any questions', 'are you angry', 'are you busy', 'are you hungry', 'are you sick', 'be careful',
               'can we meet tomorrow', 'did you book tickets', 'did you finish homework', 'do you go to office',
               'do you have money', 'do you want something to drink', 'do you want tea or coffee', 'do you watch TV',
               'dont worry', 'flower is beautiful', 'good afternoon', 'good evening', 'good morning', 'good night',
               'good question', 'had your lunch', 'happy journey', 'hello what is your name',
               'how many people are there in your family', 'i am a clerk', 'i am bore doing nothing',
               'i am fine', 'i am sorry', 'i am thinking', 'i am tired', 'i dont understand anything',
               'i go to a theatre', 'i love to shop', 'i had to say something but I forgot', 'i have headache',
               'i like pink colour', 'i live in nagpur', 'lets go for lunch', 'my mother is a homemaker', 'my name is john',
               'nice to meet you', 'no smoking please', 'open the door', 'please call me later', 'please clean the room',
               'please give me your pen', 'please use dustbin dont throw garbage', 'please wait for sometime',
               'shall I help you', 'shall we go together tommorow', 'sign language interpreter', 'sit down',
               'stand up', 'take care', 'there was traffic jam', 'wait I am thinking', 'what are you doing',
               'what is the problem', 'what is todays date', 'what is your father do', 'what is your job',
               'what is your mobile number', 'what is your name', 'whats up', 'when is your interview', 'when we will go',
               'where do you stay', 'where is the bathroom', 'where is the police station', 'you are wrong', 'address',
               'agra', 'ahmedabad', 'all', 'april', 'assam', 'august', 'australia', 'badoda', 'banana', 'banaras', 'banglore',
               'bihar', 'bihar', 'bridge', 'cat', 'chandigarh', 'chennai', 'christmas', 'church', 'clinic', 'coconut',
               'crocodile', 'dasara', 'deaf', 'december', 'deer', 'delhi', 'dollar', 'duck', 'february', 'friday', 'fruits',
               'glass', 'grapes', 'gujarat', 'hello', 'hindu', 'hyderabad', 'india', 'january', 'jesus', 'job', 'july',
               'july', 'karnataka', 'kerala', 'krishna', 'litre', 'mango', 'may', 'mile', 'monday', 'mumbai', 'museum',
               'muslim', 'nagpur', 'october', 'orange', 'pakistan', 'pass', 'police station', 'post office', 'pune', 'punjab',
               'rajasthan', 'ram', 'restaurant', 'saturday', 'september', 'shop', 'sleep', 'southafrica', 'story', 'sunday',
               'tamil nadu', 'temperature', 'temple', 'thursday', 'toilet', 'tomato', 'town', 'tuesday', 'usa', 'village',
               'voice', 'wednesday', 'weight', 'please wait for sometime', 'what is your mobile number', 'what are you doing',
               'are you busy']

    arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    text_input = text_input.lower()
    for c in string.punctuation:
        text_input = text_input.replace(c, "")

    if text_input == 'goodbye' or text_input == 'good bye' or text_input == 'bye':
        print("Oops! Time To say good bye")
        return

    elif text_input in isl_gif:
        image_path = os.path.join('ISL_Gifs', f'{text_input}.gif')
        display_image(image_path)
    else:
        for i in range(len(text_input)):
            if text_input[i] in arr:
                ImageAddress = 'letters/' + text_input[i] + '.jpg'
                ImageItself = Image.open(ImageAddress)
                ImageNumpyFormat = np.asarray(ImageItself)
                plt.imshow(ImageNumpyFormat)
                plt.show()
                plt.pause(0.8)

while True:
    msg = "HEARING IMPAIRMENT ASSISTANT"
    choices = ["Enter Text", "All Done!"]
    reply = input(f"{msg}\nOptions: {choices}\nYour choice: ").lower()
    if reply == choices[0].lower():
        text_input = input("Enter the text: ")
        func(text_input)
    elif reply == choices[1].lower():
        break
