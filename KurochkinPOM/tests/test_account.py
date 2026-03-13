import time

from base.base_test import BaseTest

class TestAccount(BaseTest):

    def test_change_name(self):
        self.login_page.open()
        self.login_page.login(
            login=self.credentials.LOGIN,
            password=self.credentials.PASSWORD
        )
        self.dashboard_page.is_opened()
        self.dashboard_page.go_to_info_page()
        self.my_info_page.is_opened()
        self.my_info_page.personal_details.change_first_name("AQA POWER")
        self.my_info_page.personal_details.save_changes()
        time.sleep(5)