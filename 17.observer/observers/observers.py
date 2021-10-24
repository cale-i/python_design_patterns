from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from observers.generators import NumberGenerator

import time
from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, generator: NumberGenerator) -> None:
        raise NotImplementedError


class DigitObserver(Observer):
    def update(self, generator: NumberGenerator) -> None:
        print(f'DigitObserver:{generator.number}')
        time.sleep(0.1)


class GraphObserver(Observer):
    def update(self, generator: NumberGenerator) -> None:
        print('GraphObserver: ', end="")
        count = generator.number
        print('*' * count)
        time.sleep(0.1)
