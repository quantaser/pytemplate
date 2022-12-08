import pytemplate.rock_paper_scissors as rps


def test_gesture():
    gs, gr, gp = rps.Gesture(0), rps.Gesture(1), rps.Gesture(2)

    assert (gs.id, gr.id, gp.id) == (0, 1, 2)

    assert (str(gs), str(gr), str(gp)) == ("scissor", "rock", "paper")

    result_rep = ["tie", "win", "loss"]
    for i, gu in enumerate([gs, gr, gp]):
        for j, gc in enumerate([gs, gr, gp]):
            assert gu.compare(gc) == result_rep[(3 + i - j) % 3]


def test_get_computer_gesture():
    for _ in range(100):
        assert rps.get_computer_gesture().id in [0, 1, 2]


def test_play():
    for _ in range(100):
        assert rps.play(rps.get_computer_gesture()) in \
            ["tie", "win", "loss"]
