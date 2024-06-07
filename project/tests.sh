#!/bin/bash

if ! command -v python3 >/dev/null 2>&1 
then
    echo "The data pipeline needs Python 3 to run, but it is not installed."
    echo "Install Python 3 e.g. via apt \(sudo apt install python3\)."
    echo "Aborting..."
    exit
fi

python3 -m pip install -r ./project/requirements.txt

echo "Starting data pipeline script"
echo
python3 ./project/pipeline.py

if [ ! -f ./data/data.sqlite ]; then
    echo "SQLite database wasn't found. Seems like the data pipeline ran into an error..."
    exit
fi

echo "Starting test script"
echo
python3 ./project/tests.py

echo
echo "All tests for the data pipeline passed."