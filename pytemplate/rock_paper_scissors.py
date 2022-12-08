import numpy.random as random


class Gesture:
    def __init__(self, id) -> None:
        self.id = id
        self.rep = {0: "scissor", 1: "rock", 2: "paper"}
        self.result_rep = {0: "tie", 1: "win", 2: "loss"}

    def compare(self, g: "Gesture"):
        result = (3 + self.id - g.id) % 3

        return self.result_rep[result]

    def __repr__(self) -> str:
        return self.rep[self.id]

    def __str__(self) -> str:
        return self.__repr__()


def get_computer_gesture():
    return Gesture(random.randint(0, 3))


def play(gesture_u: "Gesture"):
    """
        play(gesture_u: "Gesture")
    Play mora with computer
    :args gesture_u: a `Gesture`
    :return result: "win", "loss" or "tie
    """
    gesture_c = get_computer_gesture()
    result = gesture_u.compare(gesture_c)

    return result
