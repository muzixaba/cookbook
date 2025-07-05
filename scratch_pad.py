#!/usr/bin/env -S uv run --script

# /// script
# dependencies =[
# "requests",
# "beautifulsoup4",
# ]
# ///

import requests
from bs4 import BeautifulSoup

def decode_doc(doc_url):
    """
    Decodes a message from a google doc.
    The message is printed onto a 2D grid.
    
    Args:
        doc_url (str): URL of the published Google Doc
    """
    # Download the doc
    resp = requests.get(doc_url)
    resp.raise_for_status()

    # Parse the HTML content
    soup = BeautifulSoup(resp.text, 'html.parser')
    
    # Initialize variables to track grid dimensions
    max_x = 0
    max_y = 0
    coordinates = []
    
    # Extract the table content
    table = soup.find('table')
    if table:
        # Get all rows and skip the first one (header)
        rows = table.find_all('tr')[1:]  # Skip header row
        
        # Process the table rows
        for row in rows:
            # Get cells
            cells = row.find_all('td')
            if len(cells) == 3:
                try:
                    x = int(cells[0].text.strip())
                    char = cells[1].text.strip()
                    y = int(cells[2].text.strip())
                    
                    # Update maximum coordinates
                    max_x = max(max_x, x)
                    max_y = max(max_y, y)
                    
                    # Store the coordinate and character
                    coordinates.append((x, y, char))
                except ValueError:
                    continue  # Skip rows that can't be parsed as integers
    
    # Create the grid with correct orientation: rows = y, columns = x
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    
    # Fill in the characters
    for x, y, char in coordinates:
        grid[y][x] = char
    
    # Print the grid
    for row in grid:
        print(''.join(row))

if __name__ == "__main__":
    # Example usage with the provided URL
    doc_url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
    decode_doc(doc_url)    