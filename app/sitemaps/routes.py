# Copyright (c) 2026 Linh Pham
# cards.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Sitemap Routes."""

from flask import Blueprint, Response, current_app, render_template

blueprint = Blueprint("sitemaps", __name__)


@blueprint.route("/sitemap.xml")
def primary() -> Response | None:
    """View: Primary Sitemap XML."""
    sitemap = render_template("sitemaps/sitemap.xml")

    return Response(sitemap, mimetype="text/xml")
