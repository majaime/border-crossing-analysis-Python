#!/bin/bash

# First we need to provide the root access
#sudo chmod 777 ~/Dropbox/border-crossing-analysis-Python/run.sh
#sudo chmod 777 ~/Dropbox/border-crossing-analysis-Python/insight_testsuite/run_tests.sh

# Compiling the code
#java src/Main.java
#Python src/border-crossing-analysis.py

# Returning to the src root and running the code
#cd src
#java Main
#Python border-crossing-analysis.py
#sudo chmod 777 ~/Dropbox/border-crossing-analysis-Python/src/border_crossing_analysis.py
python .src/border_crossing_analysis.py --input/Border_Crossing_Entry_Data.csv --output/report.csv
