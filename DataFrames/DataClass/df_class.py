import dataclasses
from pydantic.dataclasses import dataclass
from typing import List
from pandas import DataFrame

@dataclass
class Team:

    all_rounders: List[DataFrame]
    batsmen: List[DataFrame]
    bowlers: List[DataFrame]

