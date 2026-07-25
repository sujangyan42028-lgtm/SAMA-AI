import time

SESSION_TIMEOUT = 10


class Session:

    def __init__(self):
        self.last_activity = 0
        self.active = False

    def start(self):
        self.active = True
        self.last_activity = time.time()

    def update(self):
        self.last_activity = time.time()

    def expired(self):
        return (
            self.active and
            time.time() - self.last_activity > SESSION_TIMEOUT
        )

    def stop(self):
        self.active = False