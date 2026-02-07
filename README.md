# 🛒 Carousell Scraper (DrissionPage Version)

A robust Python web scraper designed to extract product details from Carousell listings. Built with **DrissionPage** to effectively handle dynamic content and bypass basic anti-bot protections (like Cloudflare challenges).

## 🚀 Features

* **Anti-Detection**: Uses `DrissionPage` (ChromiumPage) to interact with the browser like a real user, minimizing bot detection.
* **Cloudflare Handling**: Includes basic logic to detect and wait for Cloudflare verification challenges.
* **Data Extraction**: Scrapes Product Title, Price, Description, and Source URL.
* **Batch Processing**: Reads URLs from an input CSV and saves results incrementally to an output CSV.
* **Error Logging**: Automatically logs failed URLs to `error_log.txt` for review.

## 📋 Prerequisites

* Python 3.8+
* Google Chrome browser installed

## 🛠️ Installation

1.  Clone the repository:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/carousell-scraper.git](https://github.com/YOUR_USERNAME/carousell-scraper.git)
    cd carousell-scraper
    ```

2.  Install the required dependencies:
    ```bash
    pip install DrissionPage
    ```

## 📖 Usage

1.  **Prepare your Input File**:
    Create a CSV file (e.g., `links.csv`). The script expects the **first column** to contain the target URLs.
    
    *Format example (links.csv):*
    ```csv
    product_info,product_name,D_mm 4
    https://www.carousell.com.my/p/macbook-air-m1-2020-16-gb-ram-1380808693/,MacBook Air M1 2020 16 GB RAM,"RM2,299"
    https://www.carousell.com.my/p/macbook-air-13inch-m1-16gb-256gb-1381485514/,MacBook Air 13inch M1 16gb 256gb,"RM2,299"
    https://www.carousell.com.my/p/macbook-air-13inch-m1-16gb-256gb-1382348050/,MacBook Air 13inch m1 16gb 256gb,"RM2,299"
    https://www.carousell.com.my/p/macbook-air-13inch-m1-16gb-1384204068/,MacBook Air 13inch M1 16gb,"RM2,299"
    ```

2.  **Run the Script**:
    ```bash
    python main.py
    ```

3.  **Follow Prompts**:
    * Enter input filename: `links.csv`
    * Enter output filename: `results.csv`

## 📂 Project Structure

```text
.
├── main.py           # Main scraping script
├── links.csv         # Input file (User provided)
├── results.csv       # Output file (Generated)
└── README.md         # Documentation
