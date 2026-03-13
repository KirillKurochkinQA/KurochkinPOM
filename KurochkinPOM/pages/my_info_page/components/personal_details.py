import time

from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
class PersonalDetailsComponent(BasePage):

    _FIRST_NAME_FIELD = "//input[@name='firstName']"
    _SUBMIT_BUTTON = "(//button[@type='submit'])[1]"

    def change_first_name(self, first_name):
        first_name_field = self.wait.until(EC.element_to_be_clickable(self._FIRST_NAME_FIELD))
        current_value = first_name_field.get_attribute("value")
        time.sleep(5)
        first_name_field.send_keys(Keys.CONTROL + "A")
        first_name_field.send_keys(Keys.BACKSPACE)
        first_name_field.send_keys(first_name)
        assert current_value != first_name_field.get_attribute("value"), "Name was not changed"

    def save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self._SUBMIT_BUTTON)).click()
