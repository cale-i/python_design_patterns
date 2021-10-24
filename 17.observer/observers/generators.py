from __future__ import annotations

from abc import ABCMeta, abstractmethod
from random import randint
from typing import (
    TYPE_CHECKING,
    List,
)

if TYPE_CHECKING:
    from observers.observers import Observer


class NumberGenerator(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.__observers: List[Observer] = []

    def add_observer(self, observer: Observer) -> None:
        self.__observers.append(observer)

    def delete_observer(self, observer: Observer) -> None:
        self.__observers.remove(observer)

    def notify_observers(self) -> None:
        [o.update(self) for o in self.__observers]

    @property
    @abstractmethod
    def number(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def execute(self) -> None:
        raise NotImplementedError


class RandomNumberGenerator(NumberGenerator):
    def __init__(self) -> None:
        self.__number: int = 0
        super(RandomNumberGenerator, self).__init__()

    @property
    def number(self) -> int:
        return self.__number

    def execute(self) -> None:
        for _ in range(20):
            self.__number = randint(0, 49)
            self.notify_observers()
