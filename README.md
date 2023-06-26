# Click Counter

This script updates click counts in a Google Sheets document based on provided links. It uses the Google Sheets API, `gspread` library for accessing Google Sheets, and `requests` library for sending HTTP requests to retrieve HTML content. The click counts are extracted from the HTML using `BeautifulSoup`, a popular library for web scraping.

## Prerequisites

Before running the script, make sure you have the following:

- Python 3.x installed: You can download and install Python from the official Python website: https://www.python.org/downloads/
- Required Python packages: Install the required Python packages by running the following command:

  ```bash
  pip install gspread oauth2client requests beautifulsoup4
  
Google Sheets API credentials (service account JSON key file): To access the Google Sheets API, you need to create a service account and download the JSON key file. Follow the instructions in the Google Sheets API documentation to set up the service account and obtain the credentials.

Google Sheets document with the appropriate sheet set up: Create a new Google Sheets document or use an existing one. Set up a sheet where you want to update the click counts. Note down the document name and the sheet name to configure the script.

## Installation
Clone the repository:

```bash
git clone https://github.com/your-username/your-repository.git
```


Change to the project directory:

```bash
cd your-repository
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

This command installs all the necessary packages specified in the requirements.txt file.

Place your Google Sheets API credentials JSON file in the project directory. Rename the JSON file to clicks.json or update the from_json_keyfile_name function call in the script to match your JSON file name.

## Usage

Open the script file click_counter.py and modify the following variables as needed:

document_name: Name of the Google Sheets document.
sheet_name: Name of the sheet within the document.
links: Dictionary containing the links and their corresponding cell ranges in the sheet. Update this dictionary with your specific links and cell ranges.

For example, if you have a link 'https://www.example.com' and want to update the click count in cell 'A1' of the sheet, add the following entry to the links dictionary:

```python
links = {
    'https://www.example.com': 'A1'
}
```

## Run the script:

```bash
python click_counter.py
```

The script will update the click counts in the specified Google Sheets document. It sends a GET request to each link, extracts the click count from the HTML using BeautifulSoup, and updates the corresponding cell in the sheet. If a click count cannot be extracted or an error occurs during the process, appropriate messages will be displayed.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
