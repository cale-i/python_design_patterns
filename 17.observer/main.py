from observers.generators import (
    RandomNumberGenerator,
)
from observers.observers import (
    DigitObserver,
    GraphObserver,
)


def main():
    generator: RandomNumberGenerator = RandomNumberGenerator()
    digit_observer: DigitObserver = DigitObserver()
    graph_observer: GraphObserver = GraphObserver()
    generator.add_observer(digit_observer)
    generator.add_observer(graph_observer)
    generator.execute()


if __name__ == '__main__':
    main()
