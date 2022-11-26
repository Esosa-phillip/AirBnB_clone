#!/usr/bin/python3
"""A Beautiful code that passes the
pycodestyle checks."""


class Robot:
    """Represents a robot with a name"""

    # A class variable counting the number of robots

    population = 0

    def __init__(self, name):
        """Initializes the data"""
        self.name = name
        print("(Initializing {})".format(self.name))
        Robot.population += 1

    def die(self):
        """Kill Robot"""
        print("{} is being destroyed!".format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are {:d} robots working.".format(Robot.population))

    def say_hi(self):
        """Greeting by the robot"""
        print("Greetings, I am called {}".format(self.name))

    @classmethod
    def how_many(cls):
        """Prints the current population"""
        print("There are currently {:d} robots.".format(cls.population))


new = Robot("Siri")
current = Robot("Alexa")
top = Robot("Waw")
new.say_hi()
current.say_hi()
top.say_hi()
Robot.how_many()
print("All robots finished their task")
new.die()
top.die()
Robot.how_many()
current.die()
Robot.how_many()
print("Awesome")
