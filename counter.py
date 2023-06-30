import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Set up Google Sheets API credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('click_counter\clicks.json', scope)
client = gspread.authorize(credentials)

# Update Google Sheets with click counts per day
def update_click_counts(document_name:str, sheet_name:str, links:dict):
    """
    Update the click counts per day in a Google Sheets document based on the provided links.

    Args:
        document_name (str): Name of the Google Sheets document.
        sheet_name (str): Name of the sheet within the document.
        links (dict): Dictionary containing the links and their corresponding cell ranges in the sheet.

    Returns:
        None

    """
    # Open the Google Sheets document
    sheet = client.open(document_name).worksheet(sheet_name)

    # Get the current date
    current_date = datetime.now().strftime("%d-%m-%Y")

    for link, cell_range in links.items():
        try:
            # Send a GET request to get the HTML content
            response = requests.get(link)
            html_content = response.text

            # Parse the HTML using BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')

            # Extract the click count from the parsed HTML
            click_count = extract_click_count(soup)

            # Get the cell corresponding to the current date
            cell = sheet.find(current_date)

            # Update the corresponding cell in the sheet with the click count
            if click_count is not None:
                sheet.update_cell(int(cell_range), cell.col, click_count)
                print(f'Successfully updated {cell_range} with click count {click_count} for {current_date}')
            else:
                print(f'Unable to extract click count for {cell_range}')

        except requests.exceptions.RequestException as e:
            print(f'Error occurred while updating {cell_range}: {e}')

# Extract the click count from the parsed HTML
def extract_click_count(soup):
    """
    Extract the click count from the parsed HTML content.

    Args:
        soup (BeautifulSoup): Parsed HTML content using BeautifulSoup.

    Returns:
        str or None: Click count as a string with the format '{count} clicks', or None if the click count element is not found.

    """
    # Find the <div> element with class 'squareboxtext'
    squareboxtext_div = soup.find('div', class_='squareboxtext')

    if squareboxtext_div is not None:
        # Extract the click count from the text within the <div> element
        click_count = squareboxtext_div.text.strip()
        return f'{click_count} clicks'

    # Return None if the click count element is not found
    return None

if __name__ == '__main__':
    # Google Sheets document and sheet name
    document_name = 'clicks counter'
    sheet_name = 'Sheet1'

    # Links and corresponding cell range in the sheet
    links = {
        'https://www.shorturl.at/url-total-clicks.php?u=shorturl.at/fqGMQ': 4,
        'https://www.shorturl.at/url-total-clicks.php?u=shorturl.at/mwyDV': 11,
        'https://www.shorturl.at/url-total-clicks.php?u=shorturl.at/pCLSY': 20,
        'https://www.shorturl.at/url-total-clicks.php?u=shorturl.at/tORT2': 21,
        'https://www.shorturl.at/url-total-clicks.php?u=shorturl.at/asvD2': 22
    }

    update_click_counts(document_name, sheet_name, links)