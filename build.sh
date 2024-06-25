#!/bin/bash

# Array of pages to build
pages=("index" "about" "blog" "projects" "contact")

# Create docs directory if it doesn't exist
mkdir -p docs

# Loop through each page and build the HTML
for page in "${pages[@]}"
do
    cat templates/top.html content/$page.html templates/bottom.html > docs/$page.html
done
