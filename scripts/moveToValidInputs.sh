#!/bin/bash

timestamp=$(date +%s)

mv uberResults.csv validOutputs/f-$timestamp.csv
mv uberRawResults.csv validOutputs/f-raw-$timestamp.csv
