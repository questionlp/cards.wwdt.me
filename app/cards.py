# Copyright (c) 2026 Linh Pham
# cards.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Load and Process Playing Card Packs from JSON."""

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class FaceCardInfo:
    """Face Card Information."""

    card: str
    name: str
    description: str
    image: str


@dataclass(slots=True)
class JokerCardInfo:
    """Joker Card Information."""

    color: str
    name: str
    description: str
    image: str


@dataclass(slots=True)
class CardBackInfo:
    """Card Back Information."""

    suit: str
    name: str
    description: str | None
    image: str


@dataclass(slots=True)
class CardPack:
    """Card Pack Information."""

    card_pack: int
    clubs: list[FaceCardInfo]
    diamonds: list[FaceCardInfo]
    hearts: list[FaceCardInfo]
    spades: list[FaceCardInfo]
    jokers: list[JokerCardInfo]
    card_backs: list[CardBackInfo]


def card_pack_index(card_packs: list[CardPack]) -> dict[int, int]:
    """Get an index based on a list of card packs."""
    _card_pack_index = {}
    for index in enumerate(card_packs):
        _card_pack_index[index[1].card_pack] = index[0]

    return _card_pack_index


def load_card_packs(cards_file_path: str = "cards.json") -> list[CardPack] | None:
    """Load card packs from a JSON file."""
    cards_file_path: Path = Path(cards_file_path)
    with cards_file_path.open(mode="r", encoding="utf-8") as card_packs_file:
        _card_packs: list[dict] = json.load(card_packs_file)

    if not _card_packs:
        return None

    card_pack_keys: set[str] = {
        "card_pack",
        "clubs",
        "diamonds",
        "hearts",
        "spades",
        "jokers",
        "card_backs",
    }
    card_packs: list[CardPack] = []
    for card_pack in _card_packs:
        if not card_pack_keys <= card_pack.keys():
            continue

        clubs: list[FaceCardInfo] = [FaceCardInfo(**card) for card in card_pack["clubs"]]
        diamonds: list[FaceCardInfo] = [
            FaceCardInfo(**card) for card in card_pack["diamonds"]
        ]
        hearts: list[FaceCardInfo] = [FaceCardInfo(**card) for card in card_pack["hearts"]]
        spades: list[FaceCardInfo] = [FaceCardInfo(**card) for card in card_pack["spades"]]
        jokers: list[JokerCardInfo] = [
            JokerCardInfo(**card) for card in card_pack["jokers"]
        ]
        card_backs: list[CardBackInfo] = [
            CardBackInfo(**card) for card in card_pack["card_backs"]
        ]

        card_packs.append(
            CardPack(
                card_pack=card_pack["card_pack"],
                clubs=clubs,
                diamonds=diamonds,
                hearts=hearts,
                spades=spades,
                jokers=jokers,
                card_backs=card_backs,
            )
        )

    return card_packs
