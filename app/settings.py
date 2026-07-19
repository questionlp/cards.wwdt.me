# Copyright (c) 2026 Linh Pham
# cards.wwdt.me is released under the terms of the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
#
# vim: set noai syntax=python ts=4 sw=4:
"""Application settings."""

import json
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class UmamiAnalytics:
    """Umami Analytics Settings."""

    enabled: bool
    url: str | None = field(default=None)
    data_website_id: str | None = field(default=None)
    data_domains: str | None = field(default=None)
    data_auto_track: bool | None = field(default=None)


@dataclass
class AppSettings:
    """Application Settings."""

    block_ai_scrapers: bool
    use_minified_css: bool
    default_active_suit: str | None = field(default="clubs")

    # Application and External URLs
    api_url: str | None = field(default=None)
    blog_url: str | None = field(default=None)
    graphs_url: str | None = field(default=None)
    reports_url: str | None = field(default=None)
    stats_url: str | None = field(default=None)
    site_url: str | None = field(default=None)
    repo_url: str | None = field(default=None)
    support_npr_url: str | None = field(default=None)
    github_sponsor_url: str | None = field(default=None)

    # Optional: Time Zone
    time_zone: str | None = field(default="UTC")

    # Optional: Social Media
    bluesky_user: str | None = field(default=None)
    bluesky_url: str | None = field(default=None)
    mastodon_user: str | None = field(default=None)
    mastodon_url: str | None = field(default=None)

    # Optional: Umami Analytics
    umami_analytics: UmamiAnalytics | None = field(default=None)


def load_settings(settings_file_path: str = "settings.json") -> AppSettings | None:
    """Read application settings."""
    _settings_file_path: Path = Path(settings_file_path)
    with _settings_file_path.open(mode="r", encoding="utf-8") as settings_file:
        _app_settings: dict[str, str | bool | dict | list] = json.load(settings_file)

    if not _app_settings:
        return None

    if "umami_analytics" in _app_settings:
        _umami = UmamiAnalytics(**_app_settings.get("umami_analytics"))
        _app_settings["umami_analytics"] = _umami

    app_settings = AppSettings(**_app_settings)
    return app_settings
