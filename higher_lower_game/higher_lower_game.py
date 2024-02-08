from art import logo, vs
from game_data import data
import random

def format_person(person):
  return "{}, {} from {}".format(person['name'], person['description'], person['country'])
  
def get_person_data():
  return random.choice(data)

def compare_followers(A_followers, B_followers, answer):
  if A_followers > B_followers:
    return answer == 'a'
  else:
    return answer == 'b'

def get_game_response(score):
  if score >= 0 and score < 5:
    print("What can we say... you‘re average!")
  elif score >= 5 and score < 9:
    print("Good going!")
  else:
    print("You are an awesome player!")


def game():
  continue_game = True
  score = 0

  person_A = get_person_data()
  person_B = get_person_data()

  while continue_game:
    person_A = person_B
    person_B = get_person_data()

    while person_A == person_B:
      person_B = get_person_data()
    print(logo)

    print(f'Compare A: {format_person(person_A)}')
    print(vs)
    print(f'Against B: {format_person(person_B)}')

    answer = input('Who has more followers? Select \'A\' or \'B\' ')

    if compare_followers(person_A['follower_count'], person_B['follower_count'], answer.lower()):
      score += 1
      print(f"You're Right! Your current score - {score}")
    else:
      print(f'You Lost! Your final score - {score}')
      get_game_response(score)
      continue_game = False

game()