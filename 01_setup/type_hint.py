from typing import Literal
a: int = 1
b: float
c: str
d: bool


e: list[int] = [1, 2]
f: dict[str, bool] = {'flag': True}

g: Literal["OK", "NG"] = "OK"


def sample(x: str) -> bool:
    return True
