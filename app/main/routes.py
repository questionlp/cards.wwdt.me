# Copyright (c) 2026 Linh Pham
# wwdtm-playing-cards-gallery is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Main Routes."""

from pathlib import Path

from flask import Blueprint, Response, current_app, render_template, send_file, url_for

from app.utilities import redirect_url

blueprint = Blueprint("main", __name__)


@blueprint.route("/")
def index() -> str:
    """View: Main Page."""
    return render_template("pages/index.html")


@blueprint.route("/pack/<int:card_pack_number>")
def view_pack(card_pack_number: int) -> Response | str:
    """View: Card Pack."""
    if card_pack_number not in current_app.config["available_card_packs"]:
        return redirect_url(url_for("main.index"))

    _index = current_app.config["card_pack_index"][card_pack_number]
    return render_template(
        "pages/card_pack.html",
        pack_number=card_pack_number,
        card_set=current_app.config["card_packs"][_index],
    )


@blueprint.route("/about")
def about() -> str:
    """View: About Page."""
    return render_template("pages/about.html")


@blueprint.route("/robots.txt")
def robots_txt() -> Response:
    """View: robots.txt File."""
    robots_txt_path = Path(current_app.root_path) / "static" / "robots.txt"
    if not robots_txt_path.exists():
        response = render_template("robots.txt")
        return Response(response, mimetype="text/plain")

    return send_file(robots_txt_path, mimetype="text/plain")
