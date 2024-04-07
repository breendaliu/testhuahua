

from page.base_page import BasePage
from page.idle import Idle
from page.recycle import Recycle
from page.set import Set
from page.home import Home
from page.login_pwsd import LoginPwsd
from page.mine import Mine


class Main(BasePage):

    def goto_test_login_password(self):
        self.steps("../data/login_pswd.yaml", "login_pswd")
        return LoginPwsd(self._driver)
    # 点击底部tab回收
    def goto_recycle(self):
        self.steps("../data/recycle.yaml", "goto_recycle")
        return Recycle(self._driver)

    # 点击底部tab二手
    def goto_idle(self):
        self.steps("../data/idle.yaml", "goto_idle")
        return Idle(self._driver)

    # 点击底部tab首页
    def goto_home(self):
        self.goto_recycle()
        self.steps("../data/home.yaml", "goto_home")
        return Home(self._driver)

    # 点击底部tab我的
    def goto_mine(self):
        self.steps("../data/mine.yaml", "goto_mine")
        return Mine(self._driver)

    # 点击我的->设置
    def goto_set(self):
        self.goto_mine()
        self.steps("../data/mine.yaml", "goto_set")
        return Set(self._driver)





