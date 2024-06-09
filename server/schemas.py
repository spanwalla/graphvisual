from typing import Union
from pydantic import BaseModel


class AdjacencyList(BaseModel):
    edges: dict[int, set[int]]
    directed: bool = True
    physics: bool = False
    labels: Union[dict[int, str], None] = None
    colors: Union[dict[int, str], None] = None
    default_color: str = "gray"
