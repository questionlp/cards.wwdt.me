# Copyright (c) 2026 Linh Pham
# cards.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Common Dictionaries."""

from typing import TypedDict


class CardSuit(TypedDict):
    """Card Suit."""

    name: str
    symbol: str


class CardName(TypedDict):
    """Card Name."""

    name: str
    display: str | int


class CardColor(TypedDict):
    """Card Color."""

    name: str
    symbol: str


CARD_SUITS: dict[str, CardSuit] = {
    "clubs": CardSuit({"name": "Clubs", "symbol": "♣️"}),
    "diamonds": CardSuit({"name": "Diamonds", "symbol": "♦️"}),
    "hearts": CardSuit({"name": "Hearts", "symbol": "♥️"}),
    "spades": CardSuit({"name": "Spades", "symbol": "♠️"}),
    "jokers": CardSuit({"name": "Jokers", "symbol": "🃏"}),
    "card_backs": CardSuit({"name": "Card Backs", "symbol": "🎴"}),
}

CARD_NAMES: dict[str, CardName] = {
    "1": CardName({"name": "Ace", "display": "A"}),
    "2": CardName({"name": "Two", "display": 2}),
    "3": CardName({"name": "Three", "display": 3}),
    "4": CardName({"name": "Four", "display": 4}),
    "5": CardName({"name": "Five", "display": 5}),
    "6": CardName({"name": "Six", "display": 6}),
    "7": CardName({"name": "Seven", "display": 7}),
    "8": CardName({"name": "Eight", "display": 8}),
    "9": CardName({"name": "Nine", "display": 9}),
    "10": CardName({"name": "Ten", "display": 10}),
    "J": CardName({"name": "Jack", "display": "J"}),
    "Q": CardName({"name": "Queen", "display": "Q"}),
    "K": CardName({"name": "King", "display": "K"}),
}

CARD_COLORS: dict[str, CardColor] = {
    "red": CardColor({"name": "Red", "symbol": "🟥"}),
    "black": CardColor({"name": "Black", "symbol": "⬛"}),
}
