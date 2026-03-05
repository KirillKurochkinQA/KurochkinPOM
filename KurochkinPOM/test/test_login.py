import time
from base.base_test import BaseTest

class TestLogin(BaseTest):

    def test_login(self):
        self.login_page.open()
        self.login_page.enter_login("team1aqa@gmail.com")
        self.login_page.enter_password("qwerty")
        self.login_page.click_submit_button()
        time.sleep(3)
        self.dashboard_page.click_invite_button()
        time.sleep(3)