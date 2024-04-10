from page.app import App


class TestRecycle:
    def setup(self):
        self.recycle = App().start().main().goto_recycle()

    def test_recycle(self):
        assert "回收收益(元)" in self.recycle.recycle()


