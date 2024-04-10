from page.app import App


class TestHome:
    def setup(self):
        self.home = App().start().main().goto_home()

    def test_home(self):
        assert "首页" in self.home.home()

    def test_store(self):
        assert "特色服务" in self.home.store()

    def test_store_back(self):
        assert "首页" in self.home.store_back()

    def test_store_keyword(self):
        assert "取消" in self.home.store_keyword()