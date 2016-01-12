#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from pages.desktop.partners import Partners
from unittestzero import Assert


class TestPartners(object):

    @pytest.mark.nondestructive
    def test_overview_section_image(self, mozwebqa):
        partners_page = Partners(mozwebqa)
        partners_page.selenium.maximize_window()
        partners_page.go_to_page()
        Assert.true(partners_page.is_phone_overlay_visible)

    @pytest.mark.nondestructive
    def test_os_section(self, mozwebqa):
        partners_page = Partners(mozwebqa)
        partners_page.go_to_page()
        partners_page.click_os_menu()
        partners_page.click_operators_button()
