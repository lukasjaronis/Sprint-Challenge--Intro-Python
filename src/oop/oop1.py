# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    pass


# GroundVehicle from BASE => class Vehicle
class GroundVehicle(Vehicle):
    pass


# Car => class GroundVehicle => BASE class Vehicle
class Car(GroundVehicle):
    pass


# Motorcycle => class GroundVehicle => BASE class Vehicle
class Motorcycle(GroundVehicle):
    pass


# FlightVehicle from BASE => class Vehicle
class FlightVehicle(Vehicle):
    pass

# Starship => class FlightVehicle => BASE class Vehicle
class Starship(FlightVehicle):
    pass

# Airplane => class FlightVehicle => BASE class Vehicle
class Airplane(FlightVehicle):
    pass
