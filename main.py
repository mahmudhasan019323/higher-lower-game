from art import logo, vs
from game_data import data
import random

def who_is_higher(a,b):
    if a['follower_count'] > b['follower_count']:
        return 'a'
    else:
        return 'b'

def higher_lower():
    print('\033c')
    print(logo)
    score = 0
    game_over = False
    subject_a = random.choice(data)
    subject_b = random.choice(data)
    while not game_over:
        print(score)
        print(f"Compare A: {subject_a['name']}, a {subject_a['description']}, from {subject_a['country']}")
        print(vs)
        print(f"Compare A: {subject_b['name']}, a {subject_b['description']}, from {subject_b['country']}")

higher_lower()