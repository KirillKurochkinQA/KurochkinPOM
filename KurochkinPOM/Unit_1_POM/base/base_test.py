from Unit_1_POM.pages.login_page import LoginPage
from Unit_1_POM.pages.dashboard_page import DashboardPage
from Unit_1_POM.utiles.generators import Generators
from Unit_1_POM.data.credentials import Credentials

class BaseTest:

    def setup_method(self):
        self.data = Credentials()
        self.generators = Generators()
        self.login_page = LoginPage(self.driver)
        self.dashboard_page = DashboardPage(self.driver)