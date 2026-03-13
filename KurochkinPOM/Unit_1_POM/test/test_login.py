import time
import allure
from Unit_1_POM.base.base_test import BaseTest
from Unit_1_POM.data.credentials import Credentials

@allure.epic("User")
@allure.feature("Login")
@allure.description("Login page")
class TestLogin(BaseTest):

    @allure.story("Login in our account")
    def test_login(self):
        self.login_page.open()
        self.login_page.enter_login(Credentials.LOGIN)
        self.login_page.enter_password(Credentials.PASSWORD)
        self.login_page.click_submit_button()
        time.sleep(3)
        self.dashboard_page.click_invite_button()
        time.sleep(3)