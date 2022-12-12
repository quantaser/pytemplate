import numpy.random as random


class Gesture:
    """
    `Gesture` for Rock-Paper-scissors game
    """

    def __init__(self, id) -> None:
        self.id = id
        self.rep = {0: "scissor", 1: "rock", 2: "paper"}
        self.result_rep = {0: "tie", 1: "win", 2: "loss"}

    def compare(self, g: "Gesture"):
        """
        Compare with another `Gesture`.

        Args:
            * `self` (`Gesture`): A gesture.
            * `g` (`Gesture`): Another gesture.

        Returns:
            * `result` (`str`): "win", "loss" or "tie".

        Examples:
            >>> g0 = Gesture(0)
            >>> g1 = Gesture(1)
            >>> g0.compare(g1)
            'loss'
        """

        result = (3 + self.id - g.id) % 3

        return self.result_rep[result]

    def __repr__(self) -> str:
        return self.rep[self.id]

    def __str__(self) -> str:
        return self.__repr__()


def get_computer_gesture():
    """
    Get a random gesture that represents computer.

    Returns:
        * (`Gesture`): A random gesture that represents computer.
    """

    return Gesture(random.randint(0, 3))


def play(gesture_u: "Gesture"):
    """
    Play mora with computer.

    Args:
        * `gesture_u` (`Gesture`): A gesture that represents user.

    Returns:
        * `result` (`str`): "win", "loss" or "tie".
    """

    gesture_c = get_computer_gesture()
    result = gesture_u.compare(gesture_c)

    return result
