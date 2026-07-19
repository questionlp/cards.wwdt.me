# Copyright (c) 2026 Linh Pham
# cards.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Testing Main Routes Module and Blueprint Views."""

import pytest
from flask.testing import FlaskClient
from werkzeug.test import TestResponse


def test_index(client: FlaskClient) -> None:
    """Testing main.index."""
    response: TestResponse = client.get("/")
    assert response.status_code == 200
    assert "Playing Cards Gallery" in response.text
    assert "Welcome!" in response.text


def test_about(client: FlaskClient) -> None:
    """Testing main.index."""
    response: TestResponse = client.get("/about")
    assert response.status_code == 200
    assert "Playing Cards Gallery" in response.text
    assert "About" in response.text
    assert "Scanning Process" in response.text


@pytest.mark.parametrize("card_pack_number", [1, 2])
def test_card_pack(client: FlaskClient, card_pack_number: int):
    """Testing main.card_pack."""
    response: TestResponse = client.get(f"/pack/{card_pack_number}")
    assert response.status_code == 200
    assert "Playing Cards Gallery" in response.text
    assert "Clubs" in response.text
    assert "Jokers" in response.text
    assert "Card Backs" in response.text


@pytest.mark.parametrize("card_pack_number", [1701, 65535])
def test_invalid_card_pack(client: FlaskClient, card_pack_number: int):
    """Testing main.card_pack."""
    response: TestResponse = client.get(f"/pack/{card_pack_number}")
    assert response.status_code == 302
    assert "Location" in response.headers


def test_robots_txt(client: FlaskClient) -> None:
    """Testing main.robots_txt."""
    response: TestResponse = client.get("/robots.txt")
    assert response.status_code == 200
    assert "Sitemap:" in response.text


def test_tempest_non_error(client: FlaskClient) -> None:
    """Testing main.tempest for non-500 error."""
    response: TestResponse = client.post("/tempest")
    assert response.status_code == 302

    response: TestResponse = client.post("/tempest", headers={"418": "I'm a pepper pot."})
    assert response.status_code == 302

    response: TestResponse = client.post("/tempest", headers={"419": "I'm a teapot."})
    assert response.status_code == 302
