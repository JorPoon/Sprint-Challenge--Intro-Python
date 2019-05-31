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

#base class tier 1
class Vehicle:
    pass
# class tier 2
class FlightVehicle(Vehicle):
    pass

#class tier 3
class StarShip(FlightVehicle):
    pass

class Airplane(FlightVehicle):
    pass



