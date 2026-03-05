from base.base_page import BasePage

class LoginPage(BasePage):

    _PAGE_URL = "https://www.freeconferencecall.com/ru/ru/login"
    _LOGIN_FIELD = "//input[@id='login_email']"
    _PASSWORD_FIELD = "//input[@id='password']"
    _SUBMIT_BUTTON = "//button[@id='loginformsubmit']"

    def enter_login(self, login):
        self.driver.find_element(*self._LOGIN_FIELD).send_keys(login)

    def enter_password(self, password):
        self.driver.find_element(*self._PASSWORD_FIELD).send_keys(password)

    def click_submit_button(self):
        self.driver.find_element(*self._SUBMIT_BUTTON).click()