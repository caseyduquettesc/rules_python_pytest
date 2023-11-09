import os


def test_shard_0():
    assert os.environ["TEST_SHARD_INDEX"] == "0"


def test_shard_1():
    assert os.environ["TEST_SHARD_INDEX"] == "1"
