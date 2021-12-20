import pytest
from app import fizbazz


def test_fizbuzz_must_be_1():
    expected = 1
    result = fizbazz(1)

    assert expected == result


def test_fizbazz_must_be_fiz():
    expected = "fiz"
    result = fizbazz(3)

    assert expected == result


def test_fizbazz_must_be_bazz():
    expected = "bazz"
    result = fizbazz(5)

    assert expected == result


def test_fizbazz_must_be_fizbazz():
    expected = "fizbazz"
    result = fizbazz(15)

    assert expected == result


def test_fizbazz_must_be_0():
    expected == 0
    result = fizbazz(0)

    assert expected == result
