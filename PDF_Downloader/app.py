import requests
import os

# The JSON data
# pdf_data = [
#   # { "url": "https://mca.gov.in/Ministry/pdf/Notification_20022015.pdf", "name": "G.S.R 111(E) dated 16 Feb 2015" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS101.pdf", "name": "Indian Accounting Standard (Ind AS) 101" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS102.pdf", "name": "Indian Accounting Standard (Ind AS) 102" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS103.pdf", "name": "Indian Accounting Standard (Ind AS) 103" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS104.pdf", "name": "Indian Accounting Standard (Ind AS) 104" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS105.pdf", "name": "Indian Accounting Standard (Ind AS) 105" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS106.pdf", "name": "Indian Accounting Standard (Ind AS) 106" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS107.pdf", "name": "Indian Accounting Standard (Ind AS) 107" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS108.pdf", "name": "Indian Accounting Standard (Ind AS) 108" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS109.pdf", "name": "Indian Accounting Standard (Ind AS) 109" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS110.pdf", "name": "Indian Accounting Standard (Ind AS) 110" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS111.pdf", "name": "Indian Accounting Standard (Ind AS) 111" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS112.pdf", "name": "Indian Accounting Standard (Ind AS) 112" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS113.pdf", "name": "Indian Accounting Standard (Ind AS) 113" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS114.pdf", "name": "Indian Accounting Standard (Ind AS) 114" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS115.pdf", "name": "Indian Accounting Standard (Ind AS) 115" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS1.pdf", "name": "Indian Accounting Standard (Ind AS) 1" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS2.pdf", "name": "Indian Accounting Standard (Ind AS) 2" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS7.pdf", "name": "Indian Accounting Standard (Ind AS) 7" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS8.pdf", "name": "Indian Accounting Standard (Ind AS) 8" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS10.pdf", "name": "Indian Accounting Standard (Ind AS) 10" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS12.pdf", "name": "Indian Accounting Standard (Ind AS) 12" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS16.pdf", "name": "Indian Accounting Standard (Ind AS) 16" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS17.pdf", "name": "Indian Accounting Standard (Ind AS) 17" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS19.pdf", "name": "Indian Accounting Standard (Ind AS) 19" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS20.pdf", "name": "Indian Accounting Standard (Ind AS) 20" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS21.pdf", "name": "Indian Accounting Standard (Ind AS) 21" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS23.pdf", "name": "Indian Accounting Standard (Ind AS) 23" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS24.pdf", "name": "Indian Accounting Standard (Ind AS) 24" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS27.pdf", "name": "Indian Accounting Standard (Ind AS) 27" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS28.pdf", "name": "Indian Accounting Standard (Ind AS) 28" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS29.pdf", "name": "Indian Accounting Standard (Ind AS) 29" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS32.pdf", "name": "Indian Accounting Standard (Ind AS) 32" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS33.pdf", "name": "Indian Accounting Standard (Ind AS) 33" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS34.pdf", "name": "Indian Accounting Standard (Ind AS) 34" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS36.pdf", "name": "Indian Accounting Standard (Ind AS) 36" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS37.pdf", "name": "Indian Accounting Standard (Ind AS) 37" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS38.pdf", "name": "Indian Accounting Standard (Ind AS) 38" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS40.pdf", "name": "Indian Accounting Standard (Ind AS) 40" },
#   { "url": "https://mca.gov.in/Ministry/pdf/INDAS41.pdf", "name": "Indian Accounting Standard (Ind AS) 41" }
# ]

pdf_data = [
  {
    "url": "https://www.mca.gov.in/Ministry/pdf/Ind_AS1.pdf",
    "name": "Indian Accounting Standards(Ind AS) 1"
  },
  {
    "url": "https://www.mca.gov.in/Ministry/pdf/Ind_AS2.pdf",
    "name": "Indian Accounting Standards(Ind AS) 2"
  },
  {
    "url": "https://www.mca.gov.in/Ministry/pdf/Ind_AS7.pdf",
    "name": "Indian Accounting Standards(Ind AS) 7"
  },
  {
    "url": "https://www.mca.gov.in/Ministry/pdf/Ind_AS8.pdf",
    "name": "Indian Accounting Standards(Ind AS) 8"
  },
  {
    "url": "https://www.mca.gov.in/Ministry/pdf/Ind_AS10.pdf",
    "name": "Indian Accounting Standards(Ind AS) 10"
  },
  {
    "url": "https://www.mca.gov.in/Ministry/pdf/Ind_AS11.pdf",
    "name": "Indian Accounting Standards(Ind AS) 11"
  },
  {
    "url": "https://www.mca.gov.in/Ministry/pdf/Ind_AS12.pdf",
    "name": "Indian Accounting Standards(Ind AS) 12"
  },
  {
    "url": "https://www.mca.gov.in/Ministry/pdf/Ind_AS16.pdf",
    "name": "Indian Accounting Standards(Ind AS) 16"
  },
  {
    "url": "https://www.mca.gov.in/Ministry/pdf/Ind_AS17.pdf",
    "name": "Indian Accounting Standards(Ind AS) 17"
  },
  {
    "url": "https://www.mca.gov.in/Ministry/pdf/Ind_AS18.pdf",
    "name": "Indian Accounting Standards(Ind AS) 18"
  },
  {
    "url": "https://www.mca.gov.in/Ministry/pdf/Ind_AS19.pdf",
    "name": "Indian Accounting Standards(Ind AS) 19"
  },
  {
    "url": "https://www.mca.gov.in/Ministry/pdf/Ind_AS20.pdf",
    "name": "Indian Accounting Standards(Ind AS) 20"
  },
  {
    "url": "https://www.mca.gov.in/Ministry/pdf/Ind_AS21.pdf",
    "name": "Indian Accounting Standards(Ind AS) 21"
  },
  {
    "url": "https://www.mca.gov.in/Ministry/pdf/Ind_AS23.pdf",
    "name": "Indian Accounting Standards(Ind AS) 23"
  },
  {
    "url": "https://www.mca.gov.in/Ministry/pdf/Ind_AS24.pdf",
    "name": "Indian Accounting Standards(Ind AS) 24"
  },
  {
    "url": "https://www.mca.gov.in/Ministry/pdf/Ind_AS27.pdf",
    "name": "Indian Accounting Standards(Ind AS) 27"
  },
  {
    "url": "https://www.mca.gov.in/Ministry/pdf/Ind_AS28.pdf",
    "name": "Indian Accounting Standards(Ind AS) 28"
  },
  {
    "url": "https://www.mca.gov.in/Ministry/pdf/Ind_AS29.pdf",
    "name": "Indian Accounting Standards(Ind AS) 29"
  },
  {
    "url": "https://www.mca.gov.in/Ministry/pdf/Ind_AS31.pdf",
    "name": "Indian Accounting Standards(Ind AS) 31"
  },
  {
    "url": "https://www.mca.gov.in/Ministry/pdf/Ind_AS32.pdf",
    "name": "Indian Accounting Standards(Ind AS) 32"
  },
  {
    "url": "https://www.mca.gov.in/Ministry/pdf/Ind_AS33.pdf",
    "name": "Indian Accounting Standards(Ind AS) 33"
  },
  {
    "url": "https://www.mca.gov.in/Ministry/pdf/Ind_AS34.pdf",
    "name": "Indian Accounting Standards(Ind AS) 34"
  },
  {
    "url": "https://www.mca.gov.in/Ministry/pdf/Ind_AS36.pdf",
    "name": "Indian Accounting Standards(Ind AS) 36"
  },
  {
    "url": "https://www.mca.gov.in/Ministry/pdf/Ind_AS37.pdf",
    "name": "Indian Accounting Standards(Ind AS) 37"
  },
  {
    "url": "https://www.mca.gov.in/Ministry/pdf/Ind_AS38.pdf",
    "name": "Indian Accounting Standards(Ind AS) 38"
  },
  {
    "url": "https://www.mca.gov.in/Ministry/pdf/Ind_AS39.pdf",
    "name": "Indian Accounting Standards(Ind AS) 39"
  },
  {
    "url": "https://www.mca.gov.in/Ministry/pdf/Ind_AS40.pdf",
    "name": "Indian Accounting Standards(Ind AS) 40"
  },
  {
    "url": "https://www.mca.gov.in/Ministry/pdf/Ind_AS101.pdf",
    "name": "Indian Accounting Standards(Ind AS) 101"
  },
  {
    "url": "https://www.mca.gov.in/Ministry/pdf/Ind_AS102.pdf",
    "name": "Indian Accounting Standards(Ind AS) 102"
  },
  {
    "url": "https://www.mca.gov.in/Ministry/pdf/Ind_AS103.pdf",
    "name": "Indian Accounting Standards(Ind AS) 103"
  },
  {
    "url": "https://www.mca.gov.in/Ministry/pdf/Ind_AS104.pdf",
    "name": "Indian Accounting Standards(Ind AS) 104"
  },
  {
    "url": "https://www.mca.gov.in/Ministry/pdf/Ind_AS105.pdf",
    "name": "Indian Accounting Standards(Ind AS) 105"
  },
  {
    "url": "https://www.mca.gov.in/Ministry/pdf/Ind_AS106.pdf",
    "name": "Indian Accounting Standards(Ind AS) 106"
  },
  {
    "url": "https://www.mca.gov.in/Ministry/pdf/Ind_AS107.pdf",
    "name": "Indian Accounting Standards(Ind AS) 107"
  },
  {
    "url": "https://www.mca.gov.in/Ministry/pdf/Ind_AS108.pdf",
    "name": "Indian Accounting Standards(Ind AS) 108"
  }
]


# Function to download PDF
def download_pdf(url, filename):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    response = requests.get(url, headers=headers, verify=False)


    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"{filename} downloaded successfully.")
    else:
        print(f"Failed to download {filename}. Status code: {response.status_code}")


# Directory to save PDFs
output_dir = 'pdf_downloads'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Download each PDF from the list
# for item in pdf_data:
#     pdf_url = item["url"]
#     pdf_name = item["name"].replace(" ", "_").replace("/", "_") + "_v1.pdf"  # Ensure valid filenames
#     pdf_path = os.path.join(output_dir, pdf_name)
#
#     download_pdf(pdf_url, pdf_path)


url = "https://www.mca.gov.in/bin/ebook/dms/getdocument?doc=NDc5Mjg5MDE1&docCategory=Accounting%20Standards&type=open"
download_pdf(url, os.path.join(output_dir, 'India_accounting_standards-38_apr-2022.pdf'))