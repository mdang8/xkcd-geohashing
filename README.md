# xkcd-geohashing
## What is this?
This is a little script to calculate a set of coordinates based on the "Geohashing algorithm" described in the xkcd comic [*Geohashing*](https://xkcd.com/426/ "xkcd #426: Geohashing"). 

The steps taken by the algorithm are:
- Take in a string concatenation of a date (in yyyy-mm-dd format) and the opening value for the Dow Jones Industrial Average for that date.
- Get the MD5 hash of the string.
- Split the resulting hash into two halves.
- Convert each half to decimal.
- Take the integer part of the coordinates and append the decimal values to them.

The two values given after the append are the latitude-longitude coordinates of the destination.
## Requirements
* [requests](https://pypi.python.org/pypi/requests/)

## Usage
```python
>>> python xkcd_geohashing.py <Date+Dow> <City>
```
## Examples
```python
>>> python xkcd_geohashing.py "2007-08-01-13211.09" "Paris, France"
```

**Output:** "Destination Coordinates: (48.3722044228, 2.17055150304)"
```python
>>> python xkcd_geohashing.py "2015-09-17-16738.08" "Cambridge, MA"
```
**Output:** "Destination Coordinates: (42.1970221909, -71.4021888806)"
