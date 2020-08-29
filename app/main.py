"""
app main
"""

import pathlib

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse, HTMLResponse

from .routers import (
    tiles,
)

# const
PATH_STATIC = str(pathlib.Path(__file__).resolve().parent / "client")


def create_app():
    """create app"""
    _app = FastAPI()

    # api using GeoPandas (not using DB)
    _app.include_router(
        tiles.router,
        prefix="/tiles",
        tags=["tiles"],
        responses={404: {"description": "not found"}},
    )

    # static
    _app.mount(
        "/client",
        StaticFiles(directory=PATH_STATIC, html=True),
        name="client",
    )

    return _app


app = create_app()


@app.get('/', response_class=HTMLResponse)
async def site_root():
    """root"""
    return RedirectResponse("/client")
