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



## Leaflet (Visualization)

地図上で意図通りに描画・表示出来ることを持って製作したタイルサーバーの挙動を確認

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
