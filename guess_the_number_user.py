import random

start_number = 0
end_number = 100

answer = 42
res = 0

while True:
    res += 1
    question = random.randint(start_number, end_number)
    print(f'{start_number} - {question} - {end_number}')
    if question < answer:
        start_number = question + 1
    elif question > answer:
        end_number = question - 1
    else:
        print(f'Компьютер угадал число {answer} с {res} попытки!')
        break