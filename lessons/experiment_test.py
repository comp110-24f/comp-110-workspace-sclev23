"""Experiment testing."""

from experiment import add_key_to_dicts


def test_add_key_to_dicts_use_case() -> None:
    dict1: dict[str, int] = {"one": 1, "two": 2}
    dict2: dict[str, int] = {"three": 3, "four": 4}
    dict_list: list[dict] = [dict1, dict2]
    add_key_to_dicts(dict_list, "five", 5)
    assert dict1 == {"one": 1, "two": 2, "five": 5} and dict2 == {
        "three": 3,
        "four": 4,
        "five": 5,
    }
