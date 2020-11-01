from typing import List, Tuple
from pyproj import CRS, Transformer
from shapely.ops import transform
from shapely.geometry import LineString, Point
from shapely.geometry.base import BaseGeometry


class GeoDist:
    # World Geodetic System:
    wgs_string = 'EPSG:4326'
    # World Azimuthal Equidistant string:
    wae_string = '+proj=aeqd +lat_0={lat} +lon_0={lng} +x_0=0 +y_0=0 +ellps=WGS84 +datum=WGS84 +units=m +no_defs'

    def __init__(self, coordinates: List[Tuple[float, float]], radius: int = 0):
        self.zone = coordinates
        self.radius = radius
        self.wgs84 = CRS(self.wgs_string)
        self.geometric_shape = self._format_shape()
        self.within = None
        self.utm_shape = None
        self.utm_point = None

    @staticmethod
    def _validate_point(lng, lat):
        if lng > 180.0 or lng < -180.0:
            raise ValueError('Longitude must be between -180 and 180 degrees')
        if lat > 90.0 or lat < -90.0:
            raise ValueError('Latitude must be between -90 and 90 degrees')

    def _format_shape(self) -> BaseGeometry:
        if not isinstance(self.zone, list):
            raise TypeError('Coordinates must be a list object')

        if self.radius and len(self.zone) == 1:
            return self._create_circle()

        if len(self.zone) == 1:
            return Point(self.zone)

        return LineString(self.zone)

    def _create_circle(self):
        utm = CRS(self.wae_string.format(lat=self.zone[0][1], lng=self.zone[0][0]))

        project = Transformer.from_crs(utm, self.wgs84, always_xy=True).transform
        buf = Point(0, 0).buffer(self.radius)
        circle = transform(project, buf)

        return circle

    def distance(self, lng, lat) -> float:
        self._validate_point(lng, lat)
        geometric_point = Point(lng, lat)

        utm = CRS(self.wae_string.format(lng=lng, lat=lat))
        project = Transformer.from_crs(self.wgs84, utm, always_xy=True).transform

        utm_shape = transform(project, self.geometric_shape)
        utm_point = transform(project, geometric_point)

        self.utm_shape = utm_shape
        self.utm_point = utm_point

        self.within = utm_point.within(utm_shape)

        if self.within and self.geometric_shape.type == 'Polygon':
            return utm_point.distance(utm_shape.exterior)
        return utm_point.distance(utm_shape)

    def __repr__(self):
        return 'Coords={} \n  Radius={} \n  Shape={}'.format(self.zone, self.radius, self.geometric_shape)
