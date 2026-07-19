# Copyright (c) 2026 Linh Pham
# cards.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Core Web Application."""

import platform

from flask import Flask

from app import utilities
from app.cards import CardPack, card_pack_index, load_card_packs
from app.dicts import CARD_COLORS, CARD_NAMES, CARD_SUITS
from app.errors import handlers
from app.main.redirects import blueprint as redirects_bp
from app.main.routes import blueprint as main_bp
from app.settings import AppSettings, load_settings
from app.sitemaps.routes import blueprint as sitemaps_bp
from app.version import APP_VERSION


def create_app() -> Flask:
    """Create Flask application."""
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    # Override base Jinja options
    app.jinja_options = Flask.jinja_options.copy()
    app.jinja_options.update({"trim_blocks": True, "lstrip_blocks": True})
    app.create_jinja_environment()

    # Register error handlers
    app.register_error_handler(404, handlers.not_found)
    app.register_error_handler(500, handlers.handle_exception)

    # Load application settings
    _settings: AppSettings | None = load_settings()
    _card_packs: list[CardPack] | None = load_card_packs()
    _card_pack_index: dict[int, int] = card_pack_index(_card_packs)
    _available_card_packs: set[int] = {cs.card_pack for cs in _card_packs}

    # Add card sets to application config
    app.config["card_packs"] = _card_packs
    app.config["card_pack_index"] = _card_pack_index
    app.config["available_card_packs"] = _available_card_packs

    # Set up Jinja globals
    app.jinja_env.globals["app_version"] = APP_VERSION
    app.jinja_env.globals["settings"] = _settings
    app.jinja_env.globals["rendered_at"] = utilities.generate_date_time_stamp
    app.jinja_env.globals["node_name"] = (
        platform.node().split(".")[0] if platform.node() else None
    )

    app.jinja_env.globals["card_colors"] = CARD_COLORS
    app.jinja_env.globals["card_names"] = CARD_NAMES
    app.jinja_env.globals["card_suits"] = CARD_SUITS
    app.jinja_env.globals["available_card_packs"] = _available_card_packs

    # Register application blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(redirects_bp)
    app.register_blueprint(sitemaps_bp)

    return app
