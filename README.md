# NAME: AISHWARYA TONPE

# ASSIGNMENT DESCRIPTION:
THIS IS ASSIGNMENT 0 IN THE CIS6930 DATA ENGINEERING COURSE. THE ASSIGNMENT FOCUSES ON EXTRACTING DATA. IN THIS ASSIGNMENT
GRAB AN INCIDENTS PDF FILE FORM THE NORMAN, OKLAHAMA POLICE DEPARTMENT'S WEBSITE AND THEN EXTRACT THE DATA FROM THIS PDF
AND PRINT OUT THE DIFFERENT CATEGORIES OF THE INCIDENTS.


# How to install
pipenv install

## How to run
pipenv run python assignment0/main.py --incidents https://www.normanok.gov/sites/default/files/documents/2024-01/2024-01-08_daily_incident_summary.pdf
Video -

## Functions
#### main.py \
1. download_data(url)
    - Downloads data from a given URL.
    - Uses the `urllib.request` module to make an HTTP request and fetch the data.
    - Saves the downloaded data to a local file.

2. extract_data_from_pdf(pdf_path)
    - Takes a local PDF file path as input.
    - Uses the `pypdf` module to extract text from each page of the PDF.
    - Splits the extracted text into lines and processes each line to extract relevant information such as date, incident number, location, nature, and incident type.
    - Returns a list of dictionaries, where each dictionary represents an incident with extracted information.

3. connectdb()
    - Establishes a connection to an SQLite database named "normanpd.db".
    - Returns a tuple containing a cursor and the connection.

4. createdb()
    - Creates an SQLite table named "incidents" with specific columns for incident details like time, number, location, nature, and ORI.
    - Returns the SQLite statement after execution.

5. populatedb(result)
    - Takes a list of dictionaries (`result`) representing incident data.
    - Inserts the incident data into the "incidents" table in the SQLite database.
    - Returns the number of rows modified after the insert operation.

6. status()
    - Executes an SQL query to get the count of incidents grouped by nature from the "incidents" table.
    - Sorts the result first by count (in descending order) and then alphabetically by nature.
    - Returns a sorted list of tuples containing nature and count.

7. print_status()
    - Calls `status()` to get the sorted incident data.
    - Prints the sorted data in the format "nature | count".

8. getdb()
    - Retrieves all data from the "incidents" table in the SQLite database.
    - Returns a list of tuples representing all incidents.

9. deletedb()
    - Deletes the "incidents" table from the SQLite database.

10. execute_functions(url)
    - Downloads a PDF file from the given URL using `download_data(url)`.
    - Extracts incident data from the downloaded PDF using `extract_data_from_pdf(pdf)`.
    - Deletes the existing "incidents" table, creates a new one, and populates it with the extracted data using `deletedb()`, `createdb()`, and `populatedb(result)`.
    - Prints the status of incidents using `print_status()`.

11. main()
    - Defines a command-line interface using `argparse`.
    - Parses the command-line arguments, specifically the `--incidents` argument for the URL.
    - Calls `execute_functions(url)` with the provided URL.

## Database Development
1. Connect to the Database (`connectdb()`):
    - Establish a connection to an SQLite database named "normanpd.db" using the `sqlite3` module.
    - Create a cursor to interact with the database.

2. Create the Incidents Table (`createdb()`):
    - Execute an SQL statement to create a table named "incidents" in the database.
    - Define the columns of the table, such as `incident_time`, `incident_number`, `incident_location`, `nature`, and `incident_ori`.
    - Use appropriate data types for each column (e.g., TEXT).

3. Populate the Incidents Table (`populatedb(result)`):
    - For each incident entry in the extracted data:
        - Construct an SQL `INSERT` statement to insert the data into the "incidents" table.
        - Execute the `INSERT` statement using the cursor.
        - Commit the changes to the database.

4. Query and Sort Incident Data (`status()`):
    - Execute an SQL query to get the count of incidents grouped by nature from the "incidents" table.
    - Sort the results first by count (in descending order) and then alphabetically by nature.

5. Print Sorted Incident Data (`print_status()`):
    - Print the sorted incident data in the format "nature | count".
    - Display the nature of incidents along with the corresponding count.

6. Retrieve All Incident Data (`getdb()`):
    - Execute an SQL query to retrieve all data from the "incidents" table.
    - Return a list of tuples representing all incidents.

7. Delete the Incidents Table (`deletedb()`):
    - Execute an SQL statement to drop the "incidents" table if it already exists.
    - This step is usually performed before creating a new table to avoid conflicts.

## Bugs and Assumptions
1. It is assumed that the layout of the pdf files will be constant adn it will not change.
2. It is also assumed that the except the `Nature` field all the other fields are alphanumeric.
