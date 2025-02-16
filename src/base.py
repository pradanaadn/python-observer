from abc import ABC, abstractmethod


class BaseObserver(ABC):
    @abstractmethod
    def update(self, message):
        pass

class BaseSubject(ABC):
    def subscribe(self, observer:BaseObserver):
        pass
    def unsubscribe(self, observer:BaseObserver):
        pass
    def notify(self, message):
        pass