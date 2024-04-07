from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By



class TestHuahuaB:

    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "2NSDU20411000448"
        caps["appPackage"] = "com.kejian.huahua"
        caps["appActivity"] = ".SplashActivity"
        caps["automationName"] = "UiAutomator2"
        caps["autoGrantPermissions"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(30)


    # 正确密码登录
    def test_login_password(self):
        # 同意用户协议
        es1 = self.driver.find_element(By.ID, "com.kejian.huahua:id/tv_positive")
        es1.click()
        # 跳过启动页
       # self.driver.find_element(MobileBy.ID, "com.kejian.huahua:id/iv_into").click()
        # 同意隐私协议
        self.driver.find_element(MobileBy.ID, "com.kejian.huahua:id/iv_chose_state").click()
        # 手机号登录
        self.driver.find_element(MobileBy.ID, "com.kejian.huahua:id/rl_phone_login").click()
        # 点击密码登录
        self.driver.find_element(MobileBy.ID, "com.kejian.huahua:id/tvPSwLogin").click()
        # 输入手机号码
        self.driver.find_element(MobileBy.ID, "com.kejian.huahua:id/et_phone").send_keys("18500000015")
        # 输入密码
        self.driver.find_element(MobileBy.ID, "com.kejian.huahua:id/et_pswd").send_keys("123456")
        # 点击登录
        self.driver.find_element(MobileBy.ID, "com.kejian.huahua:id/rl_login_bg").click()
        # 断言，跳转到首页，获取位置权限
        #response = self.driver.find_element(MobileBy.ID, "com.android.permissioncontroller:id/permission_message")
        self.driver.find_element(MobileBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button").click()
        # self.driver.toggle_location_services()
        # self.driver.find_element(MobileBy.XPATH, "*//[@text='本次运行允许']")
        self.driver.find_element(MobileBy.ID, "com.kejian.huahua:id/iv_del_img").click()
        #response = self.driver.find_element(MobileBy.ID, "com.kejian.huahua:id/tv_home")
        response = self.driver.find_element(MobileBy.ID, "com.kejian.huahua:id/tv_my_community")

        assert "我的社区" in response.text


    def teardown(self):

        self.driver.quit()




