import pypdf
import re
import sqlite3
import argparse
import urllib
import urllib.request

def download_data(url):
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

    data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()
    local_file_path = "dwpdf.pdf"
    with open(local_file_path, "wb") as local_file:
        local_file.write(data)

    return local_file_path

def extract_data_from_pdf(pdf_path):
    # print("pdf path", pdf_path)
    # Open the PDF file in binary mode
    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object
        # pdf = io.BytesIO(pdf_path)
        pdf_reader = pypdf.PdfReader(pdf_path)
        # pdf = pdftotext.PDF(f)

        # Extract text from each page
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text(extraction_mode="layout")  #try layout mode

    # print("mmmmmm", text)
    lines = text.splitlines()

    data = []
    for l in lines:
        if(l != ""):
            # print("++++++++++", re.split("   ", l))

            date_pattern = r'\d{1,2}/\d{1,2}/\d{4} \d{1,2}:\d{2}'

            # Find all occurrences of the date pattern in the line
            matches = re.finditer(date_pattern, l)

            # If there are matches, split the line at each match
            if matches:
                indices = [match.start() for match in matches]
                matched_lines = [l[i:j].strip() for i, j in zip([0] + indices, indices + [None])]

                # Filter out empty lines
                matched_lines = list(filter(None, matched_lines))
                for ml in matched_lines:
                    split_line = re.split("   ", ml)
                    non_empty_list = [value for value in split_line if value is not None and value != ""]
                    if(len(non_empty_list) == 5):
                        # print("****", non_empty_list[0], non_empty_list[1], non_empty_list[2], non_empty_list[3], non_empty_list[4])
                        # Define categories
                        categories = ["Date/Time", "Incident Number", "Location", "Nature", "Incident ORI"]
                        date_time = non_empty_list[0].strip()
                        incident_number = non_empty_list[1].strip()
                        location = non_empty_list[2].strip()
                        nature = non_empty_list[3].strip()
                        incident_type = non_empty_list[4].strip()

                        extracted_data = {
                            'DateTime': date_time,
                            'IncidentNumber': incident_number,
                            'Location': location,
                            'nature' : nature,
                            'IncidentType': incident_type
                        }

                        # Append the data to the list
                        data.append(extracted_data)

            else:
                matched_lines =  [l.strip()]
                split_line = re.split("   ", l)

                non_empty_list = [value for value in split_line if value is not None and value != ""]
                if(len(non_empty_list) == 5):
                    # print("****", non_empty_list[0], non_empty_list[1], non_empty_list[2], non_empty_list[3], non_empty_list[4])


                    # Define categories
                    categories = ["Date/Time", "Incident Number", "Location", "Nature", "Incident ORI"]
                    date_time = non_empty_list[0].strip()
                    incident_number = non_empty_list[1].strip()
                    location = non_empty_list[2].strip()
                    nature = non_empty_list[3].strip()
                    incident_type = non_empty_list[4].strip()

                    extracted_data = {
                        'DateTime': date_time,
                        'IncidentNumber': incident_number,
                        'Location': location,
                        'nature' : nature,
                        'IncidentType': incident_type
                    }

                    # Append the data to the list
                    data.append(extracted_data)

    return data

def connectdb():
    con = sqlite3.connect("normanpd.db")
    cur = con.cursor()
    return (cur, con)

def createdb():
    (cur, con) = connectdb()
    statement = cur.execute("CREATE TABLE incidents (incident_time TEXT,incident_number TEXT,incident_location TEXT, nature TEXT, incident_ori TEXT)")
    return statement

def populatedb(result : list[dict[str, str]]):
    (cur, con) = connectdb()
    queryString = "INSERT INTO incidents VALUES "
    for entry in result:
        queryString =  queryString + "(" + "\'" + entry.get("DateTime") + "\'" + "," +  "\'" + entry.get("IncidentNumber") + "\'" + "," + "\'" + entry.get("Location") + "\'" + "," + "\'" + entry.get("nature") + "\'" + "," + "\'" + entry.get("IncidentType") + "\'" + ")" + ","

    queryString = queryString[: -1]

    statement = cur.execute(queryString)
    con.commit()
    return statement.rowcount

def status():
    queryString = "SELECT nature, COUNT(*) AS nature_count FROM incidents GROUP BY nature"
    (cur, con) = connectdb()
    statement = cur.execute(queryString)
    data = statement.fetchall()
    sorted_data = sorted(data, key=lambda x: (-x[1], x[0]))
    return sorted_data

def print_status():
    sorted_data = status()
    for data in sorted_data:
        print(data[0] + "|" +  str(data[1]))

def getdb():
    (cur, con) = connectdb()
    statement = cur.execute("SELECT * FROM incidents")
    return statement.fetchall()

def deletedb():
    (cur, con) = connectdb()
    statement = cur.execute("DROP TABLE IF EXISTS incidents")

def execute_functions(url):
    pdf = download_data(url)
    pdf_path = url
    result = extract_data_from_pdf(pdf)
    deletedb()
    createdb()
    populatedb(result)
    print_status()
    # getdb()

def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description='Process incidents from a given URL.')

    # Add a positional argument for the URL
    parser.add_argument('--incidents', help='URL to fetch incidents data')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Check if the --incidents argument is provided
    if args.incidents:
        url = args.incidents
        url = "https://www.normanok.gov/sites/default/files/documents/2024-01/2024-01-01_daily_incident_summary.pdf"
        execute_functions(url)
        # Now you can use the 'url' variable in your code

        # Rest of your code here...

    else:
        print("Please provide the --incidents argument with a URL.")

if __name__ == "__main__":
    main()
