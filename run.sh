#!/bin/bash
locate Finance.xlsx > file_location.txt
cd "${0%/*}"
python3 app.py
