from page.app import App


class TestIdle:
    def setup(self):
        self.idle = App().start().main().goto_idle()

    def test_idle(self):
        assert "二手" in self.idle.idle()