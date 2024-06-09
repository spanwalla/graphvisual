from pydantic import BaseModel, Field
from bson.objectid import ObjectId


class AdjacencyList(BaseModel):
    edges: dict[int, list[int]]
    directed: bool = True
    physics: bool = False
    labels: dict[int, str] | None = None
    colors: dict[int, str] | None = None
    default_color: str = "gray"


class AdjacencyListDb(AdjacencyList):
    id: str = Field(default_factory=lambda: str(ObjectId()))


class UploadRequest(BaseModel):
    token: str | None = None
    graph: AdjacencyList
