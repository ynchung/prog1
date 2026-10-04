
from statistics import mean, median
from time import sleep
import destinations
import trafficComponents as tc


class TrafficSystem:
    """Defines a traffic system"""

    def __init__(self):
        """Initialize all components of the traffic
        system."""
        self.time = 0
        
        self.lane1 = tc.Lane(5)
        self.lane2 = tc.Lane(5)

        self.light = tc.Light(10, 8)
        self.generator = destinations.DestinationGenerator()

        self.queue = []

    def snapshot(self):
        """Print a snap shot of the current state of the system."""
        print(self.lane1, self.light, self.lane2, [vehicle.destination for vehicle in self.queue])
        print(f'Time step {self.time}')

    def step(self):
        """Take one time step for all components."""
        self.lane1.remove_first()
        self.lane1.step()

        if self.light.is_green() and self.lane2.get_first() is not None:
            self.lane1.enter(self.lane2.remove_first())

        self.light.step()
        self.lane2.step()

        destination = self.generator.step()

        if destination is not None:
            vehicle = tc.Vehicle(destination, self.time)
            self.queue.append(vehicle)

        if self.queue and self.lane2.last_free():
            vehicle = self.queue.pop(0)
            self.lane2.enter(vehicle)

        self.time += 1


def main():
    ts = TrafficSystem()
    for i in range(100):
        ts.snapshot()
        ts.step()
        sleep(0.1) # Pause for 0.1 s.
    print('\nFinal state:')
    ts.snapshot()
    print()


if __name__ == '__main__':
    main()