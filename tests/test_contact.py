#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from pages.desktop.contact import Contact, Spaces, Communities
from unittestzero import Assert


class TestContact:

    def check_bad_links(self, page, link_list):
        bad_links = []
        for link in link_list:
            url = page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: '
                     % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_spaces_links_are_correct(self, mozwebqa):
        spaces_page = Spaces(mozwebqa)
        spaces_page.go_to_page()
        self.check_bad_links(spaces_page, spaces_page.spaces_nav_links_list)

    @pytest.mark.nondestructive
    def test_start_on_spaces(self, mozwebqa):
        contact_page = Contact(mozwebqa)
        contact_page.go_to_page()
        Assert.equal('current', contact_page.spaces_tab.get_attribute('class'),
                     'Page does not start on spaces tab.')

    @pytest.mark.nondestructive
    def test_switching_tabs_list_display(self, mozwebqa):
        spaces_page = Spaces(mozwebqa)
        spaces_page.go_to_page()
        communities_page = spaces_page.click_communities_tab()
        spaces_page.wait_until_element_visible(communities_page.region_list)
        Assert.true(communities_page.region_list.is_displayed(),
                    'List of regions not displayed on communities tab.')
        spaces_page = communities_page.click_spaces_tab()
        spaces_page.wait_until_element_visible(spaces_page.spaces_list)
        Assert.true(spaces_page.spaces_list.is_displayed(),
                    'List of spaces not displayed on spaces tab.')

    @pytest.mark.nondestructive
    def test_region_links_are_correct(self, mozwebqa):
        communities_page = Communities(mozwebqa)
        communities_page.go_to_page()
        self.check_bad_links(communities_page, communities_page.region_nav_links_list)

