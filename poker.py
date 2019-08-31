#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pprint import pprint

class PokerHand:
    def __init__(self, hand):
        temp = hand.split(' ')
        self.hand = temp.copy()
        # print("self.hand: ", self.hand)


    def compare_with(self, opponent):
        # Your code here

        player1 = get_score(evaluate_hand(hand.hand))
        player2 = get_score(evaluate_hand(opponent.hand))
        if player1 == player2:

            print("TIE")
            return 0
        elif player1 > player2:
            print("WIN")
            return 1
        else:
            print("LOSS")
            return 2


def numeric_ranks(cards):
    """
    Represent the card ranks numerically, with 'T(en)' as 10, 'J(ack)' as 11, Q(ueen) as 12, K(ing) as 13 and A(ce) as 14.
    ex.
    numeric_ranks(['AS', '3S', '4S', '7C', 'QD'])
    :return:
    ['14S', '3S', '4S', '7C', '12D']
    """
    suits = get_suits(cards)
    face_numbers = {'T': 10, 'J': 11, 'Q':12, 'K': 13, 'A': 14}
    for index, card in enumerate(cards):
        rank = card[0:-1]
        if '0' <= rank <= '9':
            rank = int(rank)
        else:
            cards[index] = str(face_numbers[rank]) + suits[index]
    return cards

def get_score(hand):
    if hand == 'Royal flush':
        score = 10
        return  score
    elif hand == 'Straight flush':
        score = 9
        return score
    elif hand == 'Straight':
        score = 8
        return score
    elif hand == 'Flush':
        score = 7
        return score
    elif hand == 'Four of a kind':
        score = 6
        return score
    elif hand == 'Full house':
        score = 5
        return score
    elif hand == 'Three of a kind':
        score = 4
        return score
    elif hand == 'Two pair':
        score = 3
        return score
    elif hand == 'One pair':
        score = 2
        return score
    elif hand == 'High card':
        score = 1
        return score






def get_ranks(cards):
    """
    Returns a list of integers containing thge rank of each card in cards
    ex.
    get_ranks(['2S', '3C', '5C', '4H', '7S'])
    :return:
    [2,3,5,4,7]
    """

    cards = numeric_ranks(cards)
    return [int(card[0:-1]) for card in cards]


def get_suits(cards):
    """
    Returns a list of styrtings containng the suit of each card in cards.
    ex.
    get_suits(['2S', '3C', '5C', '4H', '7S'])
    :return:
    ['S', 'C', 'C', 'H', 'S']
    """
    return [card[-1] for card in cards]

def all_equal(lst):
    """
    Returns True if all elements of lst are the same, False otherwise
    ex.
    all_equal(['S,'S','S']) returns True
    """
    return len(set(lst)) == 1

def show_cards(cards):
    """ Prints the rank and suit for each card in cards. """
    cards = sort_cards(cards)
    all_suits = ['C', 'D', 'H', 'S']
    symbols = dict(zip(all_suits, ['\u2667', '\u2662', '\u2661', '\u2664']))
    faces = {14: 'A', 11: 'J', 12: 'Q', 13: 'K', 10: 'T'}
    card_symbols = []
    for card in cards:
        rank = card[0:-1]
        if int(rank) in faces:
            card_symbols.append(faces[int(rank)] + symbols[card[-1]])
        else:
            card_symbols.append(rank + symbols[card[-1]])
    for symbol in card_symbols:
        print(symbol + ' ')
    print('')
    return card_symbols

def isconsecutive(lst):
    """
    Returns True if all numbers in lst can be ordered consecutively, and False otherwise
    """
    return len(set(lst)) == len(lst) and max(lst) - min(lst) == len(lst) - 1

def sort_cards(cards):
    """
    Sorts cards by their rank.
    If rank is a string (e.g., 'A' for Ace), then the rank is changed to a number.
    Cards of the same rank are not sorted by suit.
    ex.
    sort_cards(['AS','3S','4S','5S','JC'])
    returns
    ['3S','4S','5S','11C','14S']
    """
    cards = numeric_ranks(cards)
    rank_list = get_ranks(cards)
    # Keep track of the sorting permutation
    new_order = sorted((e, i) for i, e in enumerate(rank_list))
    unsorted_cards = list(cards)
    for index, (a, b) in enumerate(new_order):
        cards[index] = unsorted_cards[b]
    return cards

def evaluate_hand(hand):
    """
    Returns a string containing the name of the hand in poker.
    Input hand must be a list of 5 strings.
    ex.
    evaluate_hand(['2S','3C','5C','4D','6D'])
    returns 'Straight'
    """
    hand = numeric_ranks(hand)
    ranks = get_ranks(hand)
    suits = get_suits(hand)
    if len(set(hand)) < len(hand) or max(ranks) > 14 or min(ranks) < 1:
        # There is a duplicate
        return 'Invalid hand'
    if isconsecutive(ranks):
        # The hand is a type of straight
        if all_equal(suits):
            # Hand is a flush
            if max(ranks) == 14:
                # Highest card is an ace
                return 'Royal flush'
            return 'Straight flush'
        return 'Straight'
    if all_equal(suits):
        return 'Flush'
    total = sum([ranks.count(x) for x in ranks])
    hand_names = {
        17: 'Four of a kind',
        13: 'Full house',
        11: 'Three of a kind',
        9: 'Two pair',
        7: 'One pair',
        5: 'High card'
    }
    return hand_names[total]


hand = PokerHand("TD 9S QS QH TH")
opponent = PokerHand("5D 5S QC 9H QH")
print(hand.compare_with(opponent))


