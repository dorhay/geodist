# Geodist
Finds the distance between a POI (point of interest) and a geometric shape on Earth's surface

## Objective
Find the distance between a point of interest and a geometric shape – polygon, circle, line string and a Point on earth’s surface using latitude and longitude associated with the geographic coordinate system


## Install
```
pip install geodist
```
## How Does It Work?
First, we convert an array of points (lng, lat) to a planar geometric object.

Then, we project the geometric object from the World Geodetic System (aka: WGS84) to the World Azimuthal Equidistant Projection (aka: ESRI:54032) with our POI as the center point of the projection.

The azimuthal equidistant projection is a map projection where all points on the map are at proportionally correct distances from the center.

![HowDoesItWork](https://github.com/dorhay/geodist/raw/master/docs/images/objective.png)

## Examples

### Polygon

The distance between a polygon and a POI
```
>>> from geodist import GeoDist
>>> coords = [(4.3466824, 50.8584046), (4.3371552, 50.8490306), (4.3429917, 50.8336379), (4.3488282, 50.8330958),
...           (4.3658226, 50.8409013), (4.3695992, 50.8473506), (4.3679684, 50.8526612), (4.3466824, 50.8584046)]
... 
>>> lng, lat = 4.3821081, 50.8133681
>>> GeoDist(coords).distance(lng, lat)
3153.3015428957347
```

![Polygon](https://github.com/dorhay/geodist/raw/master/docs/images/polygon_example.png)


### Circle
The distance between circles and a POI
```
>>> from geodist import GeoDist
>>> coords = [(-77.120923, 39.056418)]
>>> lng, lat = -77.145146, 39.047193
>>> GeoDist(coords, radius=1000).distance(lng, lat)
1334.582257003439
>>> GeoDist(coords, radius=2000).distance(lng, lat)
335.7868006642301
>>> GeoDist(coords, radius=3000).distance(lng, lat)
663.0086557682768
```

Another feature of GeoDist can tell if the POI is inside or outside the shape:
```
>>> a = GeoDist(coords, radius=1000)
>>> distance = a.distance(lng, lat)
>>> a.within
False

>>> b = GeoDist(coords, radius=3000)
>>> distance = b.distance(lng, lat)
>>> b.within
True
```

![Circle](https://github.com/dorhay/geodist/raw/master/docs/images/circle_example.png)

### Linestring
The distance between a Linestring and a POI
```
>>> from geodist import GeoDist
>>> coords = [(-121.77919, 36.24285), (-121.77939, 36.24317), (-121.77955, 36.24336), (-121.77967, 36.24347),
          (-121.77977, 36.24358), (-121.78, 36.24378), (-121.78033, 36.24409), (-121.78052, 36.24433),
..............]
>>> lng, lat = -121.88728, 37.33901
>>> GeoDist(coords).distance(lng, lat)
39603.30198998547
```

![Linestring](https://github.com/dorhay/geodist/raw/master/docs/images/linestring_example.png)
