
# Robot Introduction

class Robot:
    maker = "Future Tech"

    def __init__(self, name, model, battery):
        self.name = name
        self.model = model
        self.battery = max(0, min(battery, 100))

    def introduce(self):
        return f"Hello! My name is {self.name}. I am a {self.model} robot made by {self.maker}. Battery level: {self.battery}%"

    def charge(self, amount):
        if amount <= 0:
            return "Please enter a positive charge amount."

        self.battery = min(self.battery + amount, 100)
        return f"{self.name}'s battery is now {self.battery}%."


# Create two robots
tom = Robot("Alex", "X-500", 35)
jerry = Robot("Max", "R-300", 120)

print(tom.introduce())
print(jerry.introduce())

print(tom.charge(40))
print(tom.charge(50))
print(tom.charge(-5))
