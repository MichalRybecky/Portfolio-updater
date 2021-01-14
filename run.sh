#!/bin/bash
cd "${0%/*}"
locate Finance.xlsx > file_location.txt
python3 app.py
