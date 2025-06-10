# Web Scraping Application

## Description
A robust web scraping application built with Python that features a graphical user interface for scraping and analyzing data from websites. The application uses Selenium WebDriver for web automation and PyQt6 for the user interface.

## Features
- **GUI Interface**: User-friendly interface built with PyQt6
- **Automated Web Scraping**: Uses Selenium WebDriver for reliable web data extraction
- **Data Processing**: Collects and processes various data points including:
  - Organization Type
  - Titles
  - Reviews
  - Organization Information
  - Descriptions
  - Resources
  - Data Sets
- **Progress Tracking**: Real-time progress monitoring during scraping
- **Pause/Resume**: Ability to pause and resume scraping operations
- **CSV Export**: Automatic data export to CSV format

## Requirements
- Python 3.x
- Chrome Browser
- ChromeDriver
- Required Python packages:
  ```
  PyQt6
  selenium
  pandas
  asyncio
  ```

## Installation
1. Clone the repository:
```bash
git clone https://github.com/Ahmed8881/WebScrapping.git
```

2. Install required dependencies:
```bash
pip install PyQt6 selenium pandas asyncio
```

3. Download and install ChromeDriver:
   - Download ChromeDriver from the [official website](https://sites.google.com/chromium.org/driver/)
   - Extract and place the chromedriver.exe in the specified path:
     `C:\Users\[username]\chromedriver-win64\chromedriver-win64\chromedriver.exe`

## Usage
1. Run the main application:
```bash
python main.py
```

2. The GUI will appear with options to:
   - Start scraping
   - Pause/Resume operations
   - Monitor progress
   - View results

3. Data will be automatically saved to `data_ptr.csv` in the project directory

## Project Structure
- `main.py` - Main application entry point and GUI initialization
- `scrapper.py` - Core scraping functionality
- `Algorithms.py` - Data processing algorithms
- `RunTimeScrapping.py` - Runtime scraping management
- `ui.py` - UI definitions and components

## Technical Details
### Scraping Process
- The scraper navigates through multiple pages
- Extracts data using BeautifulSoup-style selectors
- Handles various data fields with error checking
- Implements pause/resume functionality
- Progress tracking through QtCore.QThread

### Data Processing
- Cleans and formats extracted data
- Removes duplicate spaces and newlines
- Handles missing data gracefully
- Writes to CSV in a structured format

## Error Handling
- Robust error handling for network issues
- Graceful handling of missing data elements
- User feedback through GUI for errors

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.




## Project Status
Active development - Features and improvements being added regularly.

## Acknowledgments
- Selenium WebDriver team
- PyQt6 development team
- Contributors and testers
