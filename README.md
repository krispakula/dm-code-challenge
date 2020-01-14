
### dosing.py README

---

This project provides the basic instructions to run the dosing.py script.

#### Usage

1. configure virtual environment
   >virtualenv env

2. Install packages
   >pip install -r requirements.txt

3. run dosing.py script with optional parameters viscode, svdose, ecsdstxt and results
   >python dosing.py [--viscode=VISCODE] [--svdose=SVDOSE] [--ecsdstxt=ECSDSTXT] [--results=RESULTS]

   ###### Example:

   >python dosing.py --viscode='w02' --svdose='Y' --ecsdstxt='180.0' --results=="results.csv"
   >python dosing.py --help
