# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as expected

from pages.desktop.base import Base


class Partners(Base):

    _url = '{base_url}/{locale}/firefox/partners'

    _firefox_os_header_locator = (By.CSS_SELECTOR, '#main-feature > h2')
    _welcome_section_locator = (By.CSS_SELECTOR, '#primary')
    _new_web_standards_header_locator = (By.CSS_SELECTOR, '#secondary div.section:nth-of-type(1) > h3:nth-of-type(1)')
    _freedom_platforms_header_locator = (By.CSS_SELECTOR, '#secondary div.section:nth-of-type(1) > h3:nth-of-type(2)')
    _customizations_for_oems_header_locator = (By.CSS_SELECTOR, '#secondary div.section:nth-of-type(2) > h3')
    _developer_opportunities_header_locator = (By.CSS_SELECTOR, '#secondary div.section:nth-of-type(3) > h3')
    _consumer_freedom_header_locator = (By.CSS_SELECTOR, '#secondary div.section:nth-of-type(4) > h3')
    _overview_menu_icon_locator = (By.CSS_SELECTOR, '#menu-overview > a')
    _os_menu_icon_locator = (By.CSS_SELECTOR, '#menu-os > a')
    _marketplace_menu_icon_locator = (By.CSS_SELECTOR, '#menu-marketplace > a')
    _android_menu_icon_locator = (By.CSS_SELECTOR, '#menu-android > a')
    _form_icon_locator = (By.CSS_SELECTOR, 'menu-form > a')
    _partner_pager_button_locator = (By.CSS_SELECTOR, '#mozilla-pager-page-2-tab')
    _partner_page_one_button_locator = (By.CSS_SELECTOR, '#mozilla-pager-page-1-tab')
    _partner_with_us_button_locator = (By.CSS_SELECTOR, '.partner-button > a')
    _phone_foxtail_image_locator = (By.CSS_SELECTOR, '.phone > #screen-overview > #foxtail')
    _phone_os_image_locator = (By.ID, 'screen-os')
    _os_overview_button_locator = (By.CSS_SELECTOR, '#os > .article-header > .tween > a.view-section:nth-of-type(1)')
    _operators_button_locator = (By.CSS_SELECTOR, '#os > .article-header > nav.tween > a.view-section[data-section=os-operators]:nth-of-type(2)')
    _phone_marketplace_image_locator = (By.ID, 'screen-marketplace')
    _phone_image_locator = (By.CSS_SELECTOR, '.phone-overlay')

    def click_partner_pager_button(self):
        return self.selenium.find_element(*self._partner_pager_button_locator).click()

    def click_overview_menu(self):
        return self.selenium.find_element(*self._overview_menu_icon_locator).click()

    def click_marketplace_menu(self):
        return self.selenium.find_element(*self._marketplace_menu_icon_locator).click()

    def click_os_menu(self):
        self.selenium.find_element(*self._os_menu_icon_locator).click()
        Wait(self.selenium, self.timeout).until(expected.visibility_of_element_located(self._phone_os_image_locator))

    def click_operators_button(self):
        Wait(self.selenium, self.timeout).until(expected.element_to_be_clickable(self._operators_button_locator))
        self.selenium.find_element(*self._operators_button_locator).click()
        element = Wait(self.selenium, self.timeout).until(
            expected.visibility_of_element_located((By.CSS_SELECTOR, '#os-operators-headline')))
        return element

    @property
    def is_marketplace_image_visible(self):
        return self.is_element_visible(*self._phone_marketplace_image_locator)

    @property
    def is_partner_with_us_button_visible(self):
        return self.is_element_visible(*self._partner_with_us_button_locator)

    @property
    def is_foxtail_image_visible(self):
        return self.is_element_visible(*self._phone_foxtail_image_locator)

    @property
    def is_phone_overlay_visible(self):
        return self.is_element_visible(*self._phone_image_locator)

    def click_partner_page_one_button(self):
        self.selenium.find_element(*self._partner_page_one_button_locator).click()
