# NYC Street Tree Census Analysis
---
The code in this repository is for analyzing New York City's tree census data
collected in [1995]{https://data.cityofnewyork.us/Environment/1995-Street-Tree-Census/kyad-zm4j}, [2005]{https://data.cityofnewyork.us/Environment/2005-Street-Tree-Census/29bw-z7pj}, and [2015]{https://data.cityofnewyork.us/Environment/2015-Street-Tree-Census-Tree-Data/uvpi-gqnh}. The data is provided by Department of Parks and Recreation (DPR) and owned
by NYC OpenData. The census has been collected by volunteers and staff of DPR.

Areas of zip codes are scraped from [city-data website]{http://www.city-data.com/zipmaps/New-York-New-York.html}.

The analysis examines changes in tree numbers and neighborhood tree densities.

### Methodology
Only include live trees.
Only look at trees inside NYC zip codes.
Parks were excluded from the boroughs' area calculations since this census is
only for street trees.
