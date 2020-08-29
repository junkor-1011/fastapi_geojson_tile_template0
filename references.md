Reference & Usefull Links
=============================

## [FastAPI Official Doc](https://fastapi.tiangolo.com/)

- [Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/)
- [Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/)

## [openstreetmap wiki](https://wiki.openstreetmap.org/wiki/Main_Page)

### [Slippy_map_tilenames](https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames)

タイル座標から緯度経度座標への変換

- [Tile numbers to lon.lat. (Python)](https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#Tile_numbers_to_lon..2Flat._2)


## [国土地理院ベクトルタイル提供実験](https://github.com/gsi-cyberjapan/vector-tile-experiment)

全般的に参考になる

- [タイル仕様](http://maps.gsi.go.jp/development/siyou.html)
- [タイル座標確認ページ](https://maps.gsi.go.jp/development/tileCoordCheck.html)
    - 地図上でどのエリアがどの`{z}/{x}/{y}`になるのか分かるので、APIのデバッグなどにも便利


## Format

### GeoJSON

- https://s.kitazaki.name/docs/geojson-spec-ja.html
- https://docs.geolonia.com/geojson/
- https://gis-oer.github.io/gitbook/book/materials/web_gis/GeoJSON/GeoJSON.html

### protobuf

ext: `.mvt` or `.pbf`

- https://docs.mapbox.com/vector-tiles/specification/
- https://gdal.org/drivers/vector/mvt.html
- https://github.com/tilezen/mapbox-vector-tile#encoding
    - 座標はそのままの緯度経度ではなく、各タイル内での相対座標(defaultではx, y方向で`[0, 4096)`の整数値)


## Visualization

地図上で意図通りに描画・表示出来ることを持って製作したタイルサーバーの挙動を確認

### Leaflet

- https://qiita.com/frogcat/items/97ab41c6675213b1a3f4
- https://qiita.com/frogcat/items/3d795c5cbe026c372bf4
- https://qiita.com/frogcat/items/d0579fbe1d7c375842b0

-------

## Other FrameWorks

### GeoDjango + PostGIS

PostGISを利用したgeometry型のカラムを持つテーブル(Model)を使ってベクトルタイルレイヤーを生成出来るとのこと

- https://blog.bitmeister.jp/?p=3511
- https://django-geojson.readthedocs.io/en/latest/views.html
    - [github source](https://github.com/makinacorpus/django-geojson/blob/master/djgeojson/views.py)

### tornado + PostGIS

- https://qiita.com/R_28/items/2fe16a1f37e2e46b135c


---

## Others

直接は関係無いが、有用な参考情報

### staticなベクトルタイル

- [mapbox/tippecanoe](https://github.com/mapbox/tippecanoe)
    - 静的なバイナリベクトルタイル(`pbf/mvt`)の生成が出来る


### geobuf

動的なタイルサーバーは負荷やレスポンス時間の問題が考えられるため、この辺りの手法が現実的かもしれない

- https://shimz.me/blog/leaflet-js/5574
- https://observablehq.com/@saifulazfar/geobuf-l-vectorgrid-slicer-with-leaflet
- https://observablehq.com/@saifulazfar/geobuf-with-leaflet?collection=@saifulazfar/map
- https://observablehq.com/@saifulazfar/geobuf-with-importable-map-control-from-tmcw-map?collection=@saifulazfar/map
- https://github.com/mapbox/geobuf
    - [using in python](https://github.com/pygeobuf/pygeobuf)
