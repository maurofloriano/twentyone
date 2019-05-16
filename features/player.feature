Feature: the player of a twentyone game


Scenario: player inital cards
    Given a player
    When the round starts
    Then the player start game with two cards

Scenario: Player has 2 cards and ask another, getting 3
    Given a player
    When the round starts
    And player get a new card 
    Then the player has 3 cards