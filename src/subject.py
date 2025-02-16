from typing import List
from .base import BaseSubject, BaseObserver


class Subject(BaseSubject):
    def __init__(self):
        self._observer: List[BaseObserver] = []

    def subscribe(self, observer:BaseObserver):
        if observer not in self._observer:
            self._observer.append(observer)

    def unsubscribe(self, observer:BaseObserver):
        if observer in self._observer:
            self._observer.remove(observer)

    def notify(self, message):
        for observer in self._observer:
            observer.update(message)
