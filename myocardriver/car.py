####
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
####
"""This module handles the control interface for the car."""


class Car():
    """
    This class represents the raspbery pi car. It contains the various methods
    used to control the car.
    """

    ####
    # Moving
    ####

    def move_forward(self):
        """
        Move the car forward.
        """
        print("Move Forward")

    def move_backward(self):
        """
        Move the car backward.
        """
        print("Move Backward")

    def stop_moving(self):
        """
        Stop the car from moving.
        """
        print("Stop Moving")

    ####
    # Turning
    ####

    def turn_left(self):
        """
        Turn the car left.
        """
        print("Turn Left")

    def turn_right(self):
        """
        Turn the car right.
        """
        print("Turn Right")

    def stop_turning(self):
        """
        Stop the car from turning.
        """
        print("Stop Turning")
