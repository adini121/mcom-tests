#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests
from bs4 import BeautifulSoup
from unittestzero import Assert
from pages.desktop.notes import Notes


class TestNotes:

    @pytest.mark.nondestructive
    def test_that_notes_page_is_reachable(self, mozwebqa):
        notes_page = Notes(mozwebqa)
        notes_page.go_to_page()
        Assert.contains("Notes", notes_page.firefox_notes_header_text)


    def make_absolute(self, url, base_url):
        url = url.strip(" ")
        if url.startswith('http'):
            return url
        elif url.startswith('//'):
            return 'http:' + url

        return base_url + url
