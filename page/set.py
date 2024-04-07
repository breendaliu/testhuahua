from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Set(BasePage):

    # 进入修改用户资料页
    def set_profil(self):
        self.steps("../data/set.yaml", "set_profil")
        element = self.find(By.CLASS_NAME, "android.widget.TextView")
        return element.text

    # 进入账号与安全页面
    def set_accout_safe(self):
        self.steps("../data/set.yaml", "set_accout_safe")
        element = self.find(By.ID, "com.kejian.huahua:id/tv_switch_account")
        return element.text

    # 进入隐私设置页
    def set_privacy(self):
        self.steps("../data/set.yaml", "set_privacy")
        element = self.find(By.ID, "com.kejian.huahua:id/tv_friend_setting")
        return element.text

    def set_message(self):
        self.steps("../data/set.yaml", "set_message")
        element = self.find(By.ID, "miui:id/action_bar_title")
        return element.text

    def set_address(self):
        self.steps("../data/set.yaml", "set_address")
        element = self.find(By.ID, "com.kejian.huahua:id/tv_title")
        return element.text

    # 点击切换账号按钮
    def set_switch_account(self):
        self.steps("../data/set.yaml", "set_switch_account")
        element = self.find(By.ID, "com.kejian.huahua:id/btn_manage")
        return element.text

    # 点击清除缓存按钮
    def set_Clean(self):
        self.steps("../data/set.yaml", "set_Clean")
        element = self.find(By.ID, "com.kejian.huahua:id/btn_cancel")
        return element.text

    # 取消清除缓存
    def set_clean_cancel(self):
        self.steps("../data/set.yaml", "set_Clean")
        self.steps("../data/set.yaml", "set_clean_cancel")
        element = self.find(By.ID, "com.kejian.huahua:id/tv_profile_setting")
        return element.text

    # 确定清除缓存
    def set_clean_confirm(self):
        self.steps("../data/set.yaml", "set_Clean")
        self.steps("../data/set.yaml", "set_clean_confirm")
        element = self.find(By.ID, "com.kejian.huahua:id/tv_clean")
        return element.text
