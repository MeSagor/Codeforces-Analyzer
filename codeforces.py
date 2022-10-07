import math
import sys

import requests


def get_data(url):
    global response
    try:
        response = requests.get(url)
    except:
        print('May be network issue!!!')
        exit(0)
    if response.status_code != 200:
        print('Something went wrong!!!')
        exit(0)

    data = response.json()

    ratings = []
    for element in data['result']:
        try:
            if element['verdict'] == 'OK':
                ratings.append(element['problem']['rating'])
        except:
            continue

    rating_occurrence = {rate: ratings.count(rate) for rate in ratings}
    rating_occurrence = dict(sorted(rating_occurrence.items()))
    x = [item for item in rating_occurrence]
    y = [rating_occurrence[idx] for idx in rating_occurrence]
    return x, y


def print_in_console(x, y):
    total_problem_solved = 0
    for ix in range(len(y)):
        total_problem_solved += y[ix]
    print(f'͟R͟a͟t͟i͟n͟g͟|͟ ͟C͟o͟u͟n͟t͟|')
    for i in range(len(x)):
        stick = math.ceil((y[i] * 100) / total_problem_solved) * '#'
        space_rate = (6 - (math.floor(math.log10(x[i])) + 1)) * ' '
        space_count = (5 - (math.floor(math.log10(y[i])) + 1)) * ' '
        print(f'{x[i]}{space_rate}| {y[i]}{space_count}|{stick}')
    print(f'Total | {total_problem_solved}')


if len(sys.argv) != 2:
    print('Pass a valid codeforces Handle as an argument')
    exit(0)

username = sys.argv[1]
URL = f'https://codeforces.com/api/user.status?handle={username}'

[rating, count] = get_data(URL)
print(f'Hey {username}')
print_in_console(rating, count)
