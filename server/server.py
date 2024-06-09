from fastapi import FastAPI, HTTPException
from starlette.responses import HTMLResponse

from . import models, service, database

with open('authorized.txt', 'r') as file:
    authorized_tokens = file.readlines()

authorized_tokens = [token.strip() for token in authorized_tokens]

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello"}


@app.post("/upload/adjacency_list/")
async def add_adjacency_list(request: models.UploadRequest):
    if authorized_tokens and request.token not in authorized_tokens:
        raise HTTPException(403, "You don't have permission to upload graphs.")

    result = await database.create_adjacency_list(request.graph)
    return {"key": result["_id"]}


@app.get("/show/adjacency_list/{key}/", response_class=HTMLResponse)
async def get_visualized_adjacency_list(key: str):
    try:
        graph = await database.read_adjacency_list(key)
        if graph is None:
            raise HTTPException(404, "Graph not found")

        html_content = service.visualize_graph_by_adjacency_list(graph)
        return HTMLResponse(content=html_content, status_code=200)
    except Exception as e:
        raise HTTPException(404, e)


@app.post("/instant/adjacency_list/", response_class=HTMLResponse)
async def get_visualized_adjacency_list_without_save(graph: models.AdjacencyList):
    try:
        html_content = service.visualize_graph_by_adjacency_list(graph)
        return HTMLResponse(content=html_content, status_code=200)
    except Exception as e:
        raise HTTPException(422, e)
