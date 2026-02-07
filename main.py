from DrissionPage import ChromiumPage
import time
import csv
import os

def main():
    input_file = input("Please enter the input CSV filename containing Carousell links: ")
    output_file = input("Please enter the output CSV filename for results: ")

    urls_to_scrape = []
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                if row:
                    urls_to_scrape.append(row[0])
        print(f"Successfully loaded {len(urls_to_scrape)} links. Starting scrape...")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return

    page = ChromiumPage()
    
    file_exists = os.path.isfile(output_file)
    
    with open(output_file, 'a', newline='', encoding='utf-8-sig') as f_out:
        writer = csv.writer(f_out)
        if not file_exists:
            writer.writerow(['Title', 'Price', 'Description', 'URL'])

        for i, url in enumerate(urls_to_scrape):
            print(f"\n[{i+1}/{len(urls_to_scrape)}] Processing: {url}")
            
            try:
                page.get(url)
                
                if "Just a moment" in page.title or "Challenge" in page.html:
                    print("⚠️ Cloudflare challenge detected. Waiting for verification...")
                    time.sleep(5)
                    if "Just a moment" not in page.title:
                        print("✅ Verification passed.")
                    else:
                        print("❌ Verification failed. Skipping this entry.")
                        continue

                # Extract Product Title
                title_ele = page.ele('tag:h1', timeout=2)
                title = title_ele.text if title_ele else "N/A"
                print(f"Title: {title}")

                # Extract Price
                price_ele = page.ele('tag:h3', timeout=2)
                if not price_ele:
                    price_ele = page.ele('text:RM', timeout=1)
                
                price = price_ele.text if price_ele else "N/A"
                print(f"Price: {price}")

                # Extract Description
                description = ""
                try:
                    desc_ele = page.ele('tag:p@style:line-clamp', timeout=1)
                    if desc_ele:
                        description = desc_ele.text
                        print("Description: Successfully extracted.")
                    else:
                        header = page.ele('text:Description', timeout=0.5)
                        if header:
                            description = header.parent().next().text # type: ignore
                            print("Description: Extracted via backup selector.")
                        else:
                            print("Description: Content not found (Empty).")
                except Exception:
                    description = ""
                    print("Description: Extraction error. Set to empty.")

                writer.writerow([title, price, description, url])
                
                time.sleep(2)

            except Exception as e:
                print(f"⚠️ Unknown error occurred while processing: {e}")
                with open('error_log.txt', 'a') as f_err:
                    f_err.write(f"{url} - Error: {e}\n")

    print("\nAll tasks completed!")
    page.quit()

if __name__ == "__main__":
    main()
