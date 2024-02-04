import PyPDF2
import re
import sqlite3

def extract_data_from_pdf(pdf_path):
    # Open the PDF file in binary mode
    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        # pdf = pdftotext.PDF(f)

        # Extract text from each page
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
        text += page.extract_text(extraction_mode="layout")  #try layout mode

    # Define a regular expression pattern to match the desired format
    pattern = re.compile(r'\d+/\d+/\d+ \d+:\d+ \d+-\d+ \w+ \w+.*?(?:\n|$)')

    # Find all matches in the extracted text
    matches = re.findall(pattern, text)
    # print("^^^^", matches)

    # Process the matches and extract relevant information
    data = []
    for match in matches:
        # Split the matched string into fields using whitespace
        fields = re.split(r'\s{1,}', match)
        # print("*********", fields)

        # Extract relevant information (modify as needed)
        date_time = fields[0] + ' ' + fields[1]
        incident_number = fields[2]
        location = ' '.join(fields[3:-4])
        nature = fields[-3]
        incident_type = fields[-2]

        # Create a dictionary or a tuple with the extracted information
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
    # result = extract_data_from_pdf(pdf_path)
    queryString = "INSERT INTO incidents VALUES "
    for entry in result:
        queryString =  queryString + "(" + "\'" + entry.get("DateTime") + "\'" + "," +  "\'" + entry.get("IncidentNumber") + "\'" + "," + "\'" + entry.get("Location") + "\'" + "," + "\'" + entry.get("nature") + "\'" + "," + "\'" + entry.get("IncidentType") + "\'" + ")" + ","

    queryString = queryString[: -1]

    print("&&&&&", queryString)
    statement = cur.execute(queryString)
    con.commit()
    # print(statement.rowcount)

def status():
    queryString = "SELECT nature, COUNT(*) AS nature_count FROM incidents GROUP BY nature"
    (cur, con) = connectdb()
    statement = cur.execute(queryString)
    sorted_data = sorted(statement, key=lambda x: (x[1], x[0]), reverse=True)
    print("======", sorted_data)
    return sorted_data

def print_status():
    sorted_data = status()
    for data in sorted_data:
        print(data[0] + "|" +  str(data[1]))


def getdb():
    (cur, con) = connectdb()
    statement = cur.execute("SELECT * FROM incidents")
    print("%%%%%", statement.fetchall())


def deletedb():
    (cur, con) = connectdb()
    statement = cur.execute("DROP TABLE IF EXISTS incidents")

def execute_functions():
    pdf_path = '/Users/aishwaryatonpe/Downloads/2023-12-01_daily_incident_summary.pdf'
    result = extract_data_from_pdf(pdf_path)
    deletedb()
    createdb()
    populatedb(result)
    print_status()
    getdb()

execute_functions()
