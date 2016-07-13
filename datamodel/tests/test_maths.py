from datamodel.nodes.lib import maths


def test_sum():
    seq = [1, -4, 7, 3]
    instance = maths.Sum()
    instance.input(dict(argument=seq))
    instance.set_output_label('any')
    assert 7 == instance.output()


def test_product():
    seq = [1, -4, 7, 3]
    instance = maths.Product(argument=seq)
    instance.set_output_label('any')
    assert -84 == instance.output()


def test_floor():
    instance = maths.Floor(argument=4.237)
    instance.set_output_label('any')
    assert 4 == instance.output()


def test_ceil():
    instance = maths.Ceil(argument=4.237)
    instance.set_output_label('any')
    assert 5 == instance.output()


def test_sqrt():
    instance = maths.Sqrt(argument=16)
    instance.set_output_label('any')
    assert 4 == instance.output()


def test_max():
    instance = maths.Max(argument=[-2, -1, 8, 5])
    instance.set_output_label('any')
    assert 8 == instance.output()


def test_min():
    instance = maths.Min(argument=[-2, -1, 8, 5])
    instance.set_output_label('any')
    assert -2 == instance.output()


def test_sin():
    pi = maths.Pi().output()
    instance = maths.Sin(argument=pi / 2.)
    instance.set_output_label('any')
    assert (1 - instance.output()) < 0.00001


def test_cos():
    pi = maths.Pi().output()
    instance = maths.Cos(argument=pi / 2.)
    instance.set_output_label('any')
    assert instance.output() < 0.00001


def test_abs():
    instance = maths.Abs(argument=-4.3)
    instance.set_output_label('any')
    assert 4.3 == instance.output()

    instance = maths.Abs(argument=2)
    instance.set_output_label('any')
    assert 2 == instance.output()


def test_exp():
    instance = maths.Exp(argument=0)
    instance.set_output_label('any')
    assert 1 == instance.output()


def test_log():
    instance = maths.Log(argument=maths.E().output())
    instance.set_output_label('any')
    assert 1 == instance.output()


def test_log10():
    instance = maths.Log10(argument=1000)
    instance.set_output_label('any')
    assert 3 == instance.output()


def test_power():
    expected_reqs = ['base', 'exponent']
    instance = maths.Power(base=3, exponent=3)
    assert expected_reqs == instance.requirements
    instance.set_output_label('any')
    assert 27 == instance.output()
