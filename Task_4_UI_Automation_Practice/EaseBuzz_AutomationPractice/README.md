# Pytest Automation Framework



## Project Structure

```
MyntraApplication/
├── assets/                 # Static assets (e.g., CSS)
├── data/                   # Test data (e.g., test_data.json)
├── logs/                   # Log files
├── pages/                  # Page Object Model classes
├── reports/                # Test reports (Excel, Allure)
├── tests/                  # Test scripts and conftest.py
├── utils/                  # Utilities (config, data loader)
├── requirements.txt        # Python dependencies
├── main.py                 # Script to run tests and generate reports
├── .gitignore              # Git ignore rules
└── README.md               # Project documentation
```


### Installation
1. Clone the repository:
   ```
   
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On macOS/Linux
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Running Tests
- To run all tests and generate Excel and Allure reports:
  ```sh
  pytest --alluredir=reports/allure-results
  ```
- To view the Allure report:
  ```sh
  allure serve reports/allure-results
  ```
- The Excel report will be generated at `reports/test_report.xlsx`.

### Configuration
- Environments and URLs are managed in `utils/config.py`.
- Test data is stored in `data/test_data.json`.






---


