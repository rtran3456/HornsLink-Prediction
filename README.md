# HornsLink-Prediction
This project focuses on the data analysis of the HornsLink site (2024-2025 academic year), the hub for the University of Texas student organizations and events, more specifically rejected organization registration submissions for annual re-registration. The aim of this project is to analyze trends in registration denial reasons by creating and analyzing the dataset of denial descriptions and what could be done to address them.

The objective of this was to decrease the workload and time for student associates (allows for less review of re-submissions) and stress for student organization leaders by allowing them to have their annual re-registration submission approved on the first try.

# About the Dataset
This dataset was aggregated and cleaned by me (Ryan Tran), utilizing Python and Chrome Selenium to webscrape submissions and registration denial reasons. The objective of this dataset is to analyze painpoints of registration denials by analyzing the highest reasons of submission denial. Included in the dataset is a primary key and the denial reason description of why the organization must re-submit their annual registration.

The dataset was easy to work with once scraped, all denial descriptions are uniform because student associates that handle these submissions must use a copy-and-paste for why their organization is denied. This allows use of keywords and phrases to easily categorize them of different reasons.

 Most information (emails, organization name, etc.) is omitted for privacy reasons.

# File Overviews

| File | Description |
| --- | --- |
| HORNSLINK - Denial Reasons Categorizer.py | Script ran to add categories to each entry |
| HornsLink Webscraper.py | Webscraper script ran to webscrape denial comment entries |
| RegistrationSubmissions - RAW DATA.csv | Raw data from webscraper |
| Categorized_RegistrationSubmissions.csv | Categorized tables from Python script |
