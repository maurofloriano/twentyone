from behave import then
from twentyone import *


@then('the {person} start game with two cards')
def step_dealer_has_two_cards(context, person):
    assert (len(context.human.hand) == 2)

@then('the {person} has {number_cards:d} cards')
def step_dealer_has_x_cards(context, person, number_cards):
    assert (len(context.human.hand) == number_cards)

@then('the dealer chooses a play')
def step_dealer_choose_play(context):
    assert (context.human.make_play() in ['stand', 'hit'])

@then('the {total:d} is correct')
def step_total_hand(context, total):
    assert (context.human_total == total)

@then('the {play} is correct')
def step_play_correct(context, play):
    assert (context.human_play == play)
