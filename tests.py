#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from poker import PokerHand
from poker import show_cards
class TestCase(unittest.TestCase):

    def test_royal_flush_wins(self):
        hand = PokerHand("TD JD QD KD AD")
        opponent = PokerHand("5D 5S 5C 5H AH")
        self.assertEqual(hand.compare_with(opponent), 1)

    def test_straight_flush_wins(self):
        hand = PokerHand("3S 4S 5S 6S 7S")
        opponent = PokerHand("5D 5S 5C 5H AH")
        self.assertEqual(hand.compare_with(opponent), 1)

    def test_higher_four_of_a_kind_wins(self):
        hand = PokerHand("3H JS JC JH JD")
        opponent = PokerHand("2H JS JC JH JD")
        self.assertEqual(hand.compare_with(opponent), 1)

    def test_higher_full_house_wins(self):
        hand = PokerHand("3C 3H QS QH QD")
        opponent = PokerHand("2C 2H QS QH QD")
        self.assertEqual(hand.compare_with(opponent), 1)

    def test_higher_flush_wins(self):
        hand = PokerHand("3D 6D 9D QD AD")
        opponent = PokerHand("3S 6S 9S QS KS")
        self.assertEqual(hand.compare_with(opponent), 1)

    def test_higher_straight_wins(self):
        hand = PokerHand("3D 4S 5S 6H 7H")
        opponent = PokerHand("2C 3C 4C 5H 6C")
        self.assertEqual(hand.compare_with(opponent), 1)

    def test_higher_three_of_a_kind_wins(self):
        hand = PokerHand("2C 4H QS QH QD")
        opponent = PokerHand("3C 4H QS QH QD")
        self.assertEqual(hand.compare_with(opponent), 1)

    def test_higher_two_pair_wins(self):
        hand = PokerHand("TD 9S QS QH TH")
        opponent = PokerHand("5D 5S QC 9H QH")
        self.assertEqual(hand.compare_with(opponent), 1)

    def test_higher_pair_wins(self):
        hand = PokerHand("TD TS QS KH AH")
        opponent = PokerHand("9D 9S QS KH AH")
        self.assertEqual(hand.compare_with(opponent), 1)

    def test_higher_card_wins(self):
        hand = PokerHand("4C 7D 9C JH KS")
        opponent = PokerHand("4C 7D 9C JH QS")
        self.assertEqual(hand.compare_with(opponent), 1)


if __name__ == '__main__':
    unittest.main()
