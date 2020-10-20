-- Just an example of a view that can be set up for being served as raster tiles
DROP VIEW IF EXISTS tile15 CASCADE;
CREATE VIEW tile15 AS
  SELECT ROW_NUMBER() OVER (ORDER BY pid) AS id, T_tilename(tile) as tilename, T_bounds(tile) as geom,
    ST_AsGeoJSON(T_bounds(tile)) as txt,
    ST_Centroid(T_bounds(tile)) as centroid,
    *
  FROM (
    SELECT
      MIN(points.id) as pid,
      T_tile(points.geom, 15) as tile,
      COUNT(points.id) as count,
    FROM
      points
    GROUP BY tile
    ORDER BY tile
  ) as foo;
