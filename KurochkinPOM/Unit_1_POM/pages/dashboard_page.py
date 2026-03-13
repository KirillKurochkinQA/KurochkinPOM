import allure
from Unit_1_POM.base.base_page import BasePage

class DashboardPage(BasePage):

    _PAGE_URL = "https://www.freeconferencecall.com/profile/account-info-login"
    _INVITE_BUTTON = "//button[@title='Пригласить']"

    @allure.step("Click invite button")
    def click_invite_button(self):
        self.driver.find_element(*self._INVITE_BUTTON).click()