# Card Craft

#### Video Demo:  [click here](https://www.youtube.com/watch?v=qLLVoveeffQ)
#### Description:
Card Craft - Your One-Stop Shop for Personalized and Generic Cards.

Card Craft is a project developed as a part of the CS50 Introduction to Python Programme, aimed at providing users a convenient way to generate personalized or generic card for various occasions. Whether you want to express your gratitude with a thank-you card or a celebrate a birthday with a personalized touch, Card Craft has you covered.

This is the first version. In the future this project will be improved with some of suggestions:
* error handling refinement
* input validation enhancement
* enhancing user interface such as graphical user interface (GUI) library like Tkinter or PyQt.


## Features
**Personalized and Generic Cards:** Choose between personalized cards, where you can add your own message, or select from a variety of pre-designed generic cards.

**User-Friendly Interface:** The app features a simple and intuitive interface, making it easy for users to navigate and create cards.

**Cusomization Options:** Personalise your cards by entering your name as the sender and the recipient's name.

**File Operations and Context Managers:** The project demonstrates the ability of working with file operations and creating custom context managers to manipulate text templates that are read from .txt files and being generated in full cards.

**contextlib library:** Possibility of creating own context managers with the user of generator functions and the contextlib decorator **@contextmanager**.

## Technologies Used
* Python3
* File I/O operations
* Contextlib / @contextmanager - creating own context managers.
* Colorama library
* Testing: Unittest

## Installation
To use Cardify, simply clone this repository and install the required libraries using pip:
```bash
git clone https://github.com/your_username/project.git
cd project
python3 -m pip install -r requirements.txt
```


## Usage
```bash
python3 -m project.py
```


```bash
Welcome to Create Your Card - ASAP

Please choose one of the following options.
1 - Generate a generic card.
2 - Generate a personalized card.

If you wish to quit enter "quit" or "q":
```

## Example
```bash
Welcome to Create Your Card - ASAP

Please choose one of the following options.
1 - Generate a generic card.
2 - Generate a personalized card.

If you wish to quit enter "quit" or "q":
1
You have selected to create a generic card.
Enter your name: User1
Enter the name of the recipient: User2

We generate cards for the following occassions.

0. Thank You Card
1. Happy Birthday Card
2. Encourangement
3. Sympathy
4. Mother's/Father's Day

Please select a number for the occassion you want to send card:
2
```
```bash
The card has been generated!
Redirecting back to the menu ..
```
```.txt
## A file 'User1_generic.txt' has been created.
Dear User2

You're in my thoughts and prayers.
Hope you're doing well

... Good luck today! I know you'll do great!


Sincerely,

User1
```
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.


