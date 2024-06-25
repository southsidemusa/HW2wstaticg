import os

# Define the pages to build
pages = ["index", "about", "blog", "projects", "contact"]

# Create docs directory if it doesn't exist
if not os.path.exists("docs"):
    os.makedirs("docs")

# Loop through each page and build the HTML
for page in pages:
    with open(f"templates/top.html", "r") as top_file:
        top_content = top_file.read()

    with open(f"content/{page}.html", "r") as content_file:
        page_content = content_file.read()

    with open(f"templates/bottom.html", "r") as bottom_file:
        bottom_content = bottom_file.read()

    with open(f"docs/{page}.html", "w") as output_file:
        output_file.write(top_content + page_content + bottom_content)
