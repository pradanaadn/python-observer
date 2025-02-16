from .base import BaseObserver


class PrintObserver(BaseObserver):
    def update(self, message):
        print(f"PrintObserver recieved: {message}")


class LogObserver(BaseObserver):
    def update(self, message):
        print(f"LogObserver logs: {message}")
