# URL Phishing Detection Using Domain Analysis

## Overview

This project is a simple web application built using Flask to identify potential phishing URLs. The application analyzes user-provided URLs and determines if they are phishing links or legitimate websites based on predefined rules and a list of known trusted domains.

The app also provides options to handle unshortened URLs and includes basic domain verification.

---

## Features

- **URL Analysis:** Extract and analyze domains from provided URLs.
- **Domain Verification:** Compares extracted domains against a list of trusted domains to classify URLs.
- **URL Unshortening:** Handles shortened URLs by resolving redirects to analyze the final URL.
- **User-Friendly Interface:** Flask-based web application to easily submit and analyze URLs.
- **Real-Time Feedback:** Returns the result of URL analysis instantly to the user.

---

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Flask
- Requests library

You can install Flask and Requests using pip:

```bash
pip install flask requests
```

### Steps to Start the Project

1. Clone the repository:

```bash
git clone https://github.com/praveency046/url_phishing_detection.git
```

2. Navigate to the project folder:

```bash
cd url_phishing_detection
```

3. Place your HTML template for the user interface (`index.html`) inside the `templates` folder.

4. Run the application:

```bash
python app.py
```

5. Open the web browser and access the application at:

```
http://127.0.0.1:5000/
```

---

## Usage

### How to Use

1. Start the application by running `python app.py`.
2. Open the web interface.
3. Enter a URL in the input box and submit.
4. The application will analyze the URL and display one of the following results:
   - "The URL is predicted to be a legitimate URL."
   - "The URL is predicted to be a phishing URL."
   - "The URL is predicted to be a phishing URL" (specific rule-based detection).

---

## File Structure

- `app.py`: Main application script with Flask routes and logic for URL analysis.
- `templates/index.html`: HTML template for the user interface.

---

## Customization

- **Trusted Domains:** Update the `trueDomains` list in the `check_domain` function in `app.py` to include or exclude specific domains based on your use case.
- **HTML Template:** Modify the `index.html` file in the `templates` folder to customize the user interface.

---

## Acknowledgments

Special thanks to the open-source community for resources and inspiration in building this project.

Feel free to fork, customize, and contribute to the repository!

