from behave import when
from twentyone import *

@when('the round starts')
def step_round_starts(context):
    context.human.new_round()

@when('{person} get a new card')
def step_get_new_card(context, person):
    context.human.get_card()

@when('the dealer sums the cards')
def step_dealers_sum_card(context):
    context.human_total = context.human.get_hand_total()

@when('the dealer determines a play')
def step_impl(context):
    context.human_play = context.human.determine_play(context.total)