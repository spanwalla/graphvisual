from fastapi import FastAPI, HTTPException
from starlette.responses import HTMLResponse

from . import schemas, service

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello"}


@app.post("/visualize/adjacency_list/", response_class=HTMLResponse)
async def get_visualized_adjacency_list(graph: schemas.AdjacencyList):
    try:
        html_content = service.visualize_graph_by_adjacency_list(graph)
        return HTMLResponse(content=html_content, status_code=200)
    except Exception as e:
        raise HTTPException(422, e)
