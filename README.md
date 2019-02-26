# Bike Share Efficiency Amongst Modern City Transportation

## Abstract

 One of the biggest responsibilities of any city is to provide means of transportation to its residents and visitors. Traditionally “providing transportation” meant maintaining a road network, and perhaps in addition offering some sort of metro and/or bus network for its residents to utilize. In recent years, numerous other modes of transportation have emerged, giving rise to more choice by consumers. This paper explores over 300,000 bikeshare journeys to draw conclusions on when a consumer should, and should not, utilize bike share. The paper concludes by discovering that journeys under 1.5 miles can be done fastest with a bike. Other conclusions are that while trips in the center of a city can generally be done much faster on a bike, trips several miles away from the city center can generally be done in comparable time regardless of mode of transportation.

## Meta

This project, done in collaboration with Tom Bain, served as my final project for the [Social and Technlogical Networks](http://www.inf.ed.ac.uk/teaching/courses/stn/) course at the University of Edinburgh.

This repo contains various [data-sets](/data-sets) for trip duration between two locations in London.  Each trip duration is recorded as if taken via bike-share, uber, and Tube.  Various [calculations-and-experiments](/calculations-and-experiments) were conducted and can be reviewed within the provided iPython file.  Helper [scripts](/scripts) used throughout the research phase can be found as well.

## Findings

These experiments were used to generate the [findings-graphs](/findings-graphs) which I draw conclusions upon in my final [report](/STN Project - Submitted.pdf).  Findings are split into two categories: proximity (prox) and range, as well as the specified interval.  Each edge that exists is also assigned a color based on the **optimal** mode of transport in that experiment.  The colors are:

Bike | blue
Train | green
Uber | orange


## Usage 

To run the entirely of the provided code, API tokens for Google Maps and Uber are needed.  All token I had used previously have been revoked.  Data is provided and with (minimal) tweaking should be sufficient to calculate your own results.  See the iPython file for more information.  

 
 ## Attribution
 
 See the provided iPython file for attribution.
