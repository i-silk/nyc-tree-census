# NYC Street Tree Census Analysis
---
The code in this repository is for analyzing New York City's tree census data collected in [1995](https://data.cityofnewyork.us/Environment/1995-Street-Tree-Census/kyad-zm4j), [2005](https://data.cityofnewyork.us/Environment/2005-Street-Tree-Census/29bw-z7pj), and [2015](https://data.cityofnewyork.us/Environment/2015-Street-Tree-Census-Tree-Data/uvpi-gqnh). The data is provided by Department of Parks and Recreation (DPR) and owned
by NYC OpenData. The census has been collected by volunteers and staff of DPR.

Areas of zip codes are scraped from [city-data website](http://www.city-data.com/zipmaps/New-York-New-York.html). Areas of the boroughs were found on [Wikipedia](https://en.wikipedia.org/wiki/Boroughs_of_New_York_City).

The analysis examines changes in tree numbers and neighborhood tree densities for both dead and alive trees.

### Methodology
Examine dead trees and alive trees separately.
Exclude trees from zip codes that are not part of New York City such as Mt. Vernon.
The land areas of [10 biggest parks](https://www.nycgovparks.org/about/faq) in NYC are subtracted from the land area of the boroughs, as well as the areas of LaGuardia and JFK airports.
The areas of the zip codes are not adjusted in any way. The 1995 (2005) dataset has 20,933 (8735) alive trees in zip code 0 and 896 (176) dead trees in zip code 0. Those trees were excluded from all visualizations that use zip code information.
10,761 trees of unknown status from 1995 are excluded from all of the plots, since it is not known weather those trees are dead or alive.
There are 9300 unknown alive trees in 1995, 17,505 unknown alive trees in 2005, and 5 unknown alive trees in 2015. They do not appear in the most popular species visualization.
For 2015 dataset, "Sophora" species name is changed to Japanese Pagoda Tree, since there are no Sophoras in the earlier years, and Sophora Japonica is Japanese Pagoda Tree.
The tree species in the most popular tree visualization were selected by getting the top 15 trees for the three datasets and taking their union.
