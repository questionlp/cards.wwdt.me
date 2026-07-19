# Copyright (c) 2026 Linh Pham
# wwdtm-playing-cards-gallery is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Testing Errors Module and Blueprint Views."""

from flask.testing import FlaskClient
from werkzeug.test import TestResponse


def test_not_found(client: FlaskClient) -> None:
    """Testing errors.not_found."""
    response: TestResponse = client.get("/bad-url")
    assert response.status_code == 404


def test_500(client: FlaskClient) -> None:
    """Testing main.tempest for 500 error."""
    response: TestResponse = client.post("/tempest", headers={"418": "I'm a teapot."})
    assert response.status_code == 500
