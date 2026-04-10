#
#assert abs(-42) == 42, "не верное значение"
from email.policy import strict

#подставлять пользовательские значения в строки с помощью функции .format()
#print("проверка функции {} в строке {}.".format("Формат", "просто"))

#f-strings В фигурных скобках указывается имя переменной, значение которой надо подставить в строку
#print(f"сумма {5+3}")

import pytest

@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False