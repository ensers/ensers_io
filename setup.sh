#!/bin/bash
sudo su
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp xpdf-tools-linux-4.04/bin64/pdftotext /usr/local/bin