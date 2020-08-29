"""
test api using GeoPandas(NOT using DB)
"""

import json
import math
# import pathlib
from typing import (
    Optional,
    List,
)

from fastapi import (
    APIRouter,
    HTTPException,
    Response,
)
import pandas as pd
import geopandas as gpd
import shapely.geometry
# import mapbox_vector_tile
# import geobuf


router = APIRouter()


# const
EXT_DATA_PATH = "./app/data/"   # TMP

# test data
gdf_testdata = gpd.read_file(EXT_DATA_PATH + "test.geojson")


@router.get("/")
async def site_root():
    """test"""
    return {"message": "Hello, API using GeoPandas"}


@router.get("/test.{ext}")
async def test_mono_geojson(
    ext: str = "geojson",
) -> dict:
    """
    return GeoJSON
    """
    # ext: json / geojson
    if not (ext in ["json", "geojson"]):
        raise HTTPException(
            status_code=404,
            detail="'ext' should be json or geojson"
        )

    # test data
    gdf = gdf_testdata.copy()

    return json.loads(
        gdf.to_json()
    )


@router.get("/test/{z}/{x}/{y}.geojson")
async def test_tile_geojson(
    z: int,
    x: int,
    y: int,
    limit_zmin: Optional[int] = 8,
) -> dict:
    """
    return GeoJSON Tile
    """

    if limit_zmin is not None:
        if z < limit_zmin:
            raise HTTPException(status_code=404, detail="Over limit of zoom")

    # test data
    gdf = gdf_testdata.copy()

    bbox_polygon = tile_bbox_polygon(z, x, y)

    # filtering
    intersections = gdf.geometry.intersection(bbox_polygon)
    gs_filtered = intersections[~intersections.is_empty]    # geoseries
    gdf_filtered = gpd.GeoDataFrame(
        gdf.loc[gs_filtered.index, :].drop(columns=['geometry']),
        geometry=gs_filtered,
    )

    # NO DATA
    if len(gs_filtered) == 0:
        raise HTTPException(status_code=404, detail="No Data")

    # return geojson
    return json.loads(
        gdf_filtered.to_json()
    )


def tile_coord(
    zoom: int,
    xtile: int,
    ytile: int,
) -> (float, float):
    """
    This returns the NW-corner of the square. Use the function
    with xtile+1 and/or ytile+1 to get the other corners.
    With xtile+0.5 & ytile+0.5 it will return the center of the tile.
    http://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#Tile_numbers_to_lon..2Flat._2
    """
    n = 2.0 ** zoom
    lon_deg = xtile / n * 360.0 - 180.0
    lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * ytile / n)))
    lat_deg = math.degrees(lat_rad)
    return (lon_deg, lat_deg)


def tile_bbox_polygon(
    zoom: int,
    xtile: int,
    ytile: int,
) -> shapely.geometry.Polygon:
    """
    create bbox for Tile by using shapely.geometry
    """
    z = zoom
    x = xtile
    y = ytile

    # get bbox
    nw = tile_coord(z, x, y)
    se = tile_coord(z, x+1, y+1)
    bbox = shapely.geometry.Polygon(
        [
            nw, (se[0], nw[1]),
            se, (nw[0], se[1]), nw
        ]
    )
    return bbox
