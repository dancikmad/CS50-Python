answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
answer = answer.lower().strip()

accepted_answers = ["42", "forty two", "forty-two"]

def check_answer(a, b):
    """Initialize a function that takes a users
    input 'a' and check if the answer is in list 'b'.
    - If a is in b : print "Yes"
    - If a is not in b : print "No"
    """
    if a in b:
        print("Yes")
    else:
        print("No")

check_answer(answer, accepted_answers)