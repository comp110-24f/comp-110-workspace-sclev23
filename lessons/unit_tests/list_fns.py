"""Unit testing."""


def get_first(list: list[str]) -> str:
    if len(list) == 0:
        return ""
    return list[0]


def remove_first(list: list[str]) -> None:
    list.pop(0)


def get_and_remove_first(list: list[str]) -> str:
    first_char: str = list[0]
    list.pop(0)
    return first_char


lis: list[str] = ["Wow", "WW", "www"]
print(get_first(lis))
print(get_and_remove_first(lis))
print(lis)
