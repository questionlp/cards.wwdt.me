# Copyright (c) 2026 Linh Pham
# wwdtm-playing-cards-gallery is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Utility Functions."""

from datetime import datetime
from typing import Any

import pytz
from flask import Response, current_app


def generate_date_time_stamp(time_zone: str = "UTC") -> str:
    """Generate a current date/timestamp string."""
    _time_zone = pytz.timezone(time_zone)
    now = datetime.now(_time_zone)
    return now.strftime("%Y-%m-%d %H:%M:%S %Z")


def redirect_url(url: str, status_code: int = 302) -> Response:
    """Returns a redirect response for a given URL."""
    # Use a custom response class to force set response headers
    # and handle the redirect to prevent browsers from caching redirect
    response: Response = current_app.response_class(
        response=None, status=status_code, mimetype="text/plain"
    )

    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = 0
    response.headers["Location"] = url
    return response
