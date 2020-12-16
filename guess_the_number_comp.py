import random
"""
The computer guesses a number in a given range, the user must guess it.
"""


def computer():
    question = random.randint(1, 100)
    return question


def main(question):
    print('The computer guessed a number from 1 To 100. Guess it!')
    print(question)
    res = 0
    while True:
        res += 1
        answer = int(input('Enter a number: '))
        if answer == question:
            print(f'Success! You guessed the number {question} on the {res} attempts!')
            break
        elif answer <= 0:
            print('Enter a number greater than 0!')
        elif answer >= 100:
            print('Enter a number less than 100!')
        else:
            if answer > question:
                print('Wrong! The hidden number is smaller.')
            else:
                print('Wrong! The hidden number is larger.')
        

if __name__ == '__main__':
    x = computer()
    main(question=x)