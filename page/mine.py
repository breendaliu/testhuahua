from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Mine(BasePage):

    # 进入我的二维码页面
    def qrcode(self):
        self.steps("../data/mine.yaml", "qrcode")
        element = self.find(By.ID, "com.kejian.huahua:id/tv_title")
        return element.text

    # 绑定微信
    def qrcode_bind_wx(self):
        self.steps("../data/mine.yaml", "qrcode")
        # 如果绑定微信按钮存在，则点击绑定微信按钮
        try:
            self.steps("../data/mine.yaml", "qrcode_bind_wx")
            self._driver.implicitly_wait(20)
            element = self.find(By.ID, "com.kejian.huahua:id/btn_bind_wx")
        # 绑定微信按钮不存在，返回None
        except:
            self._driver.implicitly_wait(20)
            element = None
        return element

    # 返回上一页
    def qrcode_back(self):
        self.steps("../data/mine.yaml", "qrcode")
        self.steps("../data/mine.yaml", "qrcode_back")
        element = self.find(By.ID, "com.kejian.huahua:id/tv_mian_user")
        return element.text

    # 点击设置
    def set(self):
        self.steps("../data/mine.yaml", "goto_set")
        element = self.find(By.ID, "com.kejian.huahua:id/tv_profile_setting")
        return element.text

    def set_back(self):
        self.steps("../data/mine.yaml", "goto_set")
        self.steps("../data/mine.yaml", "set_back")
        element = self.find(By.ID, "com.kejian.huahua:id/tv_mian_user")
        return element.text

    # 点击主页
    def goto_mian_user(self):
        self.steps("../data/mine.yaml", "goto_mian_user")
        element = self.find(By.ID, "com.kejian.huahua:id/tv_tab")
        return element.text

    def mian_user_back(self):
        self.steps("../data/mine.yaml", "goto_mian_user")
        self.steps("../data/mine.yaml", "mian_user_back")
        element = self.find(By.ID, "com.kejian.huahua:id/tv_mian_user")
        return element.text

    # 点击获赞数
    def liked(self):
        self.steps("../data/mine.yaml", "liked")
        element = self.find(By.ID, "com.kejian.huahua:id/btn_know")
        return element.text

    # 点击获赞弹窗中的我知道了按钮
    def liked_know(self):
        self.liked()
        self.steps("../data/mine.yaml", "liked_know")
        element = self.find(By.ID, "com.kejian.huahua:id/tv_mian_user")
        return element.text

    # 点击关注数
    def focus(self):
        self.steps("../data/mine.yaml", "focus")
        element = self.find(By.ID, "com.kejian.huahua:id/tv_friends_myfollow")
        return element.text

    # 点击朋友页面的返回按钮
    def friends_back(self):
        self.steps("../data/mine.yaml", "focus")
        self.steps("../data/mine.yaml", "friends_back")
        element = self.find(By.ID, "com.kejian.huahua:id/tv_mian_user")
        return element.text

    # 点击粉丝数
    def fans(self):
        self.steps("../data/mine.yaml", "fans")
        element = self.find(By.ID, "com.kejian.huahua:id/tv_friends_myfollow")
        return element.text

    # 点击我的钱包
    def wallet(self):
        self.steps("../data/mine.yaml", "wallet")
        element = self.find(By.ID, "com.kejian.huahua:id/tv_title")
        return element.text

    # 点击我的钱包页面的返回按钮
    def wallet_back(self):
        self.steps("../data/mine.yaml", "wallet")
        self.steps("../data/mine.yaml", "wallet_back")
        element = self.find(By.ID, "com.kejian.huahua:id/tv_mian_user")
        return element.text

    # 点击福利中心
    def welfare(self):
        self.steps("../data/mine.yaml", "welfare")
        element = self.find(By.ID, "com.kejian.huahua:id/tab_welfare")
        return element.text

    # 点击福利中心页面的返回按钮
    def welfare_back(self):
        self.steps("../data/mine.yaml", "welfare")
        self.steps("../data/mine.yaml", "welfare_back")
        element = self.find(By.ID, "com.kejian.huahua:id/tv_mian_user")
        return element.text

    # 点击我发布的
    def publish(self):
        self.steps("../data/mine.yaml", "publish")
        element = self.find(By.ID, "com.kejian.huahua:id/tv_title")
        return element.text

    # 点击我发布的页面的返回按钮
    def publish_back(self):
        self.steps("../data/mine.yaml", "publish")
        self.steps("../data/mine.yaml", "publish_back")
        element = self.find(By.ID, "com.kejian.huahua:id/tv_mian_user")
        return element.text

    # 点击我卖出的
    def wait_send(self):
        self.steps("../data/mine.yaml", "wait_send")
        element = self.find(By.ID, "com.kejian.huahua:id/tv_title")
        return element.text

    # 点击我卖出的页面的返回按钮
    def wait_send_back(self):
        self.steps("../data/mine.yaml", "wait_send")
        self.steps("../data/mine.yaml", "wait_send_back")
        element = self.find(By.ID, "com.kejian.huahua:id/tv_mian_user")
        return element.text
    # 点击我买到的
    def wait_receipt(self):
        self.steps("../data/mine.yaml", "wait_receipt")
        element = self.find(By.ID, "com.kejian.huahua:id/tv_title")
        return element.text

    # 点击我买到的页面的返回按钮
    def wait_receipt_back(self):
        self.steps("../data/mine.yaml", "wait_receipt")
        self.steps("../data/mine.yaml", "wait_receipt_back")
        element = self.find(By.ID, "com.kejian.huahua:id/tv_mian_user")
        return element.text

    # 点击我收藏的
    def wait_evaluate(self):
        self.steps("../data/mine.yaml", "wait_evaluate")
        element = self.find(By.ID, "com.kejian.huahua:id/tv_title")
        return element.text

    # 点击我收藏的页面的返回按钮
    def wait_evaluate_back(self):
        self.steps("../data/mine.yaml", "wait_evaluate")
        self.steps("../data/mine.yaml", "wait_evaluate_back")
        element = self.find(By.ID, "com.kejian.huahua:id/tv_mian_user")
        return element.text

    # 点击认证中心
    def authentication(self):
        self.swipe(0.8,0.8,0.8,0.2)
        self.steps("../data/mine.yaml", "authentication")
        element = self.find(By.ID, "com.kejian.huahua:id/tv_feed")
        return element.text

    # 点击认证中心页面的返回按钮
    def authentication_back(self):
        self.authentication()
        self.steps("../data/mine.yaml", "authentication_back")
        element = self.find(By.ID, "com.kejian.huahua:id/tv_toolbox_title")
        return element.text