class DummyObserver:
    def __init__(self):
        self.notified = False

    def notify(self, message: str):
        self.notified = True


def test_observer_is_notified():
    observer = DummyObserver()
    observer.notify("test message")
    assert observer.notified is True
