# Copyright (c) 2026 Linh Pham
# wwdtm-playing-cards-gallery is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Testing Main Redirects Module and Blueprint Views."""

from flask.testing import FlaskClient
from werkzeug.test import TestResponse


def test_favicon(client: FlaskClient) -> None:
    """Testing main.redirects.favicon."""
    response: TestResponse = client.get("/favicon.ico")
    assert response.status_code == 301
    assert response.location


def test_pack_redirect(client: FlaskClient) -> None:
    """Testing main.redirect.pack_redirect."""
    response: TestResponse = client.get("/pack")
    assert response.status_code == 302
    assert response.location

    response: TestResponse = client.get("/packs")
    assert response.status_code == 302
    assert response.location


def test_tempest(client: FlaskClient) -> None:
    """Testing main.redirect.tempest."""
    response: TestResponse = client.get("/tempest")
    assert response.status_code == 302
    assert response.location

    response: TestResponse = client.head("/tempest")
    assert response.status_code == 302
    assert response.location
