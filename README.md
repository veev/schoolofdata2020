# schoolofdata2020
Code for School of Data Workshop 2020 about Energy Use in NYC's Buildings

## javascript-mapbox
The html files in the javascript-mapbox folder are map-based visualizations of various climate related open datasets, such as data pertaining to NYC's Local Law 84, or Local Law 24 which prioritizes solar installations on municipal buildings. They use the mapbox gl js library primarily, as well as some d3 color scales

## python-analysis-cleaning
The files in here are created with jupyter notebooks that uses python and primarily the pandas library to read in csv data, make transformations to the columns and rows, and save out new versions of the files. These were then joined to NYC's building footprints shapefiles based on the BBL (Borough, Block and Lot number), which is a unique identifier for buildings in the city.
