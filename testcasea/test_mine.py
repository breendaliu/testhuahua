from selenium.webdriver.common.by import By

from page.app import App


class TestMine:
    def setup(self):
        self.mine = App().start().main().goto_mine()

    def test_qrcode(self):
        assert "我的二维码" in self.mine.qrcode()

    def test_qrcode_bind_wx(self):
        assert self.mine.qrcode_bind_wx() is None

    def test_qrcode_back(self):
        assert "主页" in self.mine.qrcode_back()

    def test_set(self):
        assert "资料设置" in self.mine.set()

    def test_set_back(self):
        assert "主页" in self.mine.set_back()

    def test_goto_mian_user(self):
        assert "动态" in self.mine.goto_mian_user()

    def test_mian_user_back(self):
        assert "主页" in self.mine.mian_user_back()

    # 点击获赞数
    def test_liked(self):
        assert "我知道了" in self.mine.liked()

    # 点击获赞弹窗中的我知道了按钮
    def test_liked_know(self):
        assert "主页" in self.mine.liked_know()

    # 点击关注
    def test_focus(self):
        assert "我的关注" in self.mine.focus()

    # 点击朋友页面的返回按钮
    def test_friends_back(self):
        assert "主页" in self.mine.friends_back()

    # 点击粉丝数
    def test_fans(self):
        assert "我的关注" in self.mine.fans()

    # 点击我的钱包
    def test_wallet(self):
        assert "我的钱包" in self.mine.wallet()

    # 点击我的钱包页面返回按钮
    def test_wallet_back(self):
        assert "主页" in self.mine.wallet_back()

    # 点击福利中心
    def test_welfare(self):
        assert "福利中心" in self.mine.welfare()

    # 点击福利中心页面返回按钮
    def test_welfare_back(self):
        assert "主页" in self.mine.welfare_back()

    # 点击我发布的
    def test_publish(self):
        assert "我发布的" in self.mine.publish()

    # 点击我发布的页面的返回按钮
    def test_publish_back(self):
        assert "主页" in self.mine.publish_back()

    # 点击我卖出的
    def test_wait_send(self):
        assert "我卖出的" in self.mine.wait_send()

    # 点击我卖出的页面的返回按钮
    def test_wait_send_back(self):
        assert "主页" in self.mine.wait_send_back()

    # 点击我买到的
    def test_wait_receipt(self):
        assert "我买到的" in self.mine.wait_receipt()

    # 点击我买到的页面的返回按钮
    def test_wait_receipt_back(self):
        assert "主页" in self.mine.wait_receipt_back()

    # 点击我收藏的
    def test_wait_evaluate(self):
        assert "我的收藏" in self.mine.wait_evaluate()

    # 点击我收藏的页面的返回按钮
    def test_wait_evaluate_back(self):
        assert "主页" in self.mine.wait_evaluate_back()

    # 点击认证中心
    def test_authentication(self):
        assert "提交意见" in self.mine.authentication()

    # 点击认证中心页面的返回按钮
    def test_authentication_back(self):
        assert "其他服务" in self.mine.authentication_back()