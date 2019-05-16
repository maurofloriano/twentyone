from behave import given
from twentyone import *

@given('a dealer')
def step_dealer(context):
    context.human = Dealer()

@given('a player')
def step_player(context):
    context.human = Player()

@given('a hand {total:d}')
def step_hand(context, total):
    context.human = Dealer()
    context.total = total

@given('a {hand}')
def step_given_the_hand(context, hand):
    context.human = Dealer()
    context.human.hand = hand.split(',')


