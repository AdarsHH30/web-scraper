# TimesJobs Scraper

A command-line tool that scrapes job listings from TimesJobs based on keywords you provide.

## Quick Installation Guide

1. Clone the repository by
   ```
    git clone https://github.com/AdarsHH30/web-scraping.git
   ```
2. Install dependencies:
   ```
   pip install beautifulsoup4 requests colorama lxml
   ```
3. Create a `Jobs` directory in the project folder:
   ```
   mkdir Jobs
   ```
4. Run the scraper:
   ```
   python scraper.py
   ```
5. Enter the job keyword when prompted
6. Enter the number of pages to scrape (each page has 25 job listings)
7. Results will be saved as JSON in the `Jobs` directory

The tool extracts job titles, links, descriptions, required skills, and locations from TimesJobs.com and saves them in a structured JSON format.
