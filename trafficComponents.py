# Traffic system components


class Vehicle:
    """Represents vehicles in traffic simulations"""

    def __init__(self, destination, borntime):
        """Creates the vehicle with specified properties."""
        # Implement this constructor.
        self.destination = destination
        self.borntime = borntime

    def __str__(self):
        return f"Vehicle({self.destination}, {self.borntime})"


class Lane:
    """Represents a lane with (possibly) vehicles"""

    def __init__(self, length):
        """Creates a lane of specified length."""
        # Implement this constructor.
        self.lane = [None] * length

    def __str__(self):
        """String representation of lane contents."""
        result = "["

        for vehicle in self.lane:
            if vehicle is None:
                result += "."
            else:
                result += vehicle.destination
        result += "]"
        return result

    def enter(self, vehicle):
        """Called when a new vehicle enters the end of the lane."""
        # Implement this method.
        self.lane[-1] = vehicle

    def last_free(self):
        """Reports whether there is space for a vehicle at the
        end of the lane."""
        # Implement this method.
        return self.lane[-1] is None

    def step(self):
        """Execute one time step."""
        # Implement this method.
        for i in range(1, len(self.lane)):
            if self.lane[i] is not None and self.lane[i - 1] is None:
                self.lane[i - 1] = self.lane[i]
                self.lane[i] = None

    def get_first(self):
        """Return the first vehicle in the lane, or None."""
        # Implement this method.
        return self.lane[0]

    def remove_first(self):
        """Remove the first vehicle in the lane.
           Return the vehicle removed.
           If no vehicle is a the front of the lane, returns None
           without removing anything."""
        # Implement this method.
        removed_vehicle = self.lane[0]
        self.lane[0] = None
        return removed_vehicle

    def number_in_lane(self):
        """Return the number of vehicles currently in the lane."""
        count = 0
        for vehicle in self.lane:
            if vehicle is not None:
                count += 1
        return count


def demo_lane():
    """For demonstration of the class Lane"""
    a_lane = Lane(10)
    print(a_lane)
    v = Vehicle('N', 34)
    a_lane.enter(v)
    print(a_lane)

    a_lane.step()
    print(a_lane)
    for i in range(20):
        if i % 2 == 0:
            u = Vehicle('S', i)
            a_lane.enter(u)
        a_lane.step()
        print(a_lane)
        if i % 3 == 0:
            print('  out: ',
                  a_lane.remove_first())
    print('Number in lane:',
          a_lane.number_in_lane())


class Light:
    """Represents a traffic light"""

    def __init__(self, period, green_period):
        """Create a light with the specified timers."""
        self.period = period
        self.green_period = green_period
        self.clock = 0

    def __str__(self):
        """Report current state of the light."""
        if self.is_green():
            return "(G)"
        else:
            return "(R)"

    def step(self):
        """Take one light time step."""
        # Implement this method.
        self.clock = (self.clock + 1) % self.period
        # clock = 0 → (0+1)%7 = 1
        # clock = 1 → (1+1)%7 = 2
        # clock = 2 → (2+1)%7 = 3
        # ...
        # clock = 5 → (5+1)%7 = 6
        # clock = 6 → (6+1)%7 = 0

    def is_green(self):
        """Return whether the light is currently green."""
        # Implement this method.
        return self.clock < self.green_period


def demo_light():
    """Demonstrats the Light class"""
    a_light = Light(7, 3)
    for i in range(15):
        print(i, a_light,
              a_light.is_green())
        a_light.step()


def main():
    """Demonstrates the classes"""
    print('\nLight demonstration\n')
    demo_light()
    print('\nLane demonstration')
    demo_lane()


if __name__ == '__main__':
    main()