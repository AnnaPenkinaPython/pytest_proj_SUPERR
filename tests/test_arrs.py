import pytest

from utils import arrs, dicts



@pytest.fixture
def data():
    return {"vcs": "mercurial"}


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]


def test_get_val(data):
    assert dicts.get_val(data, "vcs") == "mercurial"
    assert dicts.get_val({}, "vcs", "test") == "test"
    assert dicts.get_val(data, "nokey") == "git"
