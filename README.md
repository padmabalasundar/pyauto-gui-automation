# PyAuto GUI Automation Bot

## Project Overview

This project is a simple desktop automation bot built using **Python** and **PyAutoGUI**.

The bot automatically performs the following tasks:

1. Opens Google Chrome.
2. Navigates to a public Stock website.
3. Copies the required information from the webpage.
4. Opens Microsoft Excel.
5. Creates a new row containing:
   - Current Date & Time
   - Retrieved Data
   - A short comment
6. Saves the Excel file with today's date in the filename.
7. Takes a screenshot of the completed Excel sheet and saves it.

Example output:

| Date & Time | Data | Comment |
|-------------|------|---------|
| 2025-06-17 09:30 AM | NIFTY 50: 25,120.45 | Market opened positive |

---

## Technologies Used

- Python 3.x
- PyAutoGUI
- Pyperclip
- Microsoft Excel
- Google Chrome

---

## How It Works

The automation follows these steps:

1. Launch Google Chrome.
2. Open the target website.
3. Wait until the page finishes loading.
4. Select and copy the required information.
5. Launch Microsoft Excel.
6. Create a new workbook.
7. Enter:
   - Current date and time
   - Retrieved data
   - A predefined comment
8. Save the workbook using today's date.
9. Capture a screenshot of the final Excel sheet.
10. Save the screenshot.

The bot uses keyboard shortcuts and mouse actions through **PyAutoGUI** to automate the complete workflow.

---

## Project Structure

```
Daily-Report-Bot/
│
├── main.py
├── README.md
├── screenshots/
├── reports/
└── requirements.txt
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/padmabalasundar/pyauto-gui-automation.git
```

### 2. Navigate to the project folder

```bash
cd pyauto-gui-automation
```

### 3. Create a virtual environment

**Windows**

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### 4. Install the required packages

```bash
pip install -r requirements.txt
```

---

## Running the Project

Run the Python script:

```bash
python main.py
```

The bot will automatically:

- Open Chrome
- Fetch the required information
- Open Excel
- Enter the data
- Save the Excel file
- Capture a screenshot

---

## Output

The project generates:

- Excel report

```
daily_report_YYYY-MM-DD.xlsx
```

Example:

```
daily_report_2025-06-17.xlsx
```

- Screenshot

```
daily_report_YYYY-MM-DD.png
```

---

## Notes

- Make sure Google Chrome and Microsoft Excel are installed.
- Do not use the keyboard or mouse while the automation is running.
- Keep the screen unlocked during execution.
- The bot uses screen-based automation, so application loading times may vary.

---

## Future Improvements

- Read data directly from websites using Python libraries.
- Support multiple websites.
- Add error handling for slow-loading pages.
- Automatically create daily reports.
- Schedule the automation to run at a specific time.

---

## Author

PadmaBalasundar - Developed as a desktop automation project using Python and PyAutoGUI.