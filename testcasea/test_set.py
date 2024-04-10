from page.app import App


class TestSet:
    def setup(self):
        self.set = App().start().main().goto_set()

    # 点击资料设置按钮,进入修改资料页
    def test_set_profil(self):
        assert "修改资料" in self.set.set_profil()

    # 点击账号与安全按钮
    def test_set_accout_safe(self):
        assert "手机号" in self.set.set_accout_safe()

    # 点击隐私设置
    def test_set_privacy(self):
        assert "好友设置" in self.set.set_privacy()

    # 点击开启消息通知
    def test_set_messgae(self):
        assert "哗哗" in self.set.set_message()

    # 点击我的地址
    def test_set_address(self):
        assert "我的地址" in self.set.set_address()

    # 点击切换账号
    def test_set_switch_account(self):
        assert "管理" in self.set.set_switch_account()

    # 点击清除缓存
    def test_set_Clean(self):
        assert "取消" in self.set.set_Clean()

    def test_set_clean_cancel(self):
        assert "资料设置" in self.set.set_clean_cancel()

    def test_set_clean_confirm(self):
        assert "0.00MB" in self.set.set_clean_confirm()
