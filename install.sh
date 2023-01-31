#!/bin/sh

echo "1" > ~/workspace/alpha2phi/install.txt

# Install the libraries
pip install -r requirements.txt

# Install browser
playwright install firefox

# Login to ChatGPT
chatgpt install


