class strings:

    dbstrings = {
        "db_path" : "resources/normanpd.db",
        "create_db" : "CREATE TABLE incidents (incident_time TEXT,incident_number TEXT,incident_location TEXT, nature TEXT, incident_ori TEXT)",
        "insert_db" : "INSERT INTO incidents VALUES ",
        "select_db" : "SELECT nature, COUNT(*) AS nature_count FROM incidents GROUP BY nature",
        "select_all_db" : "SELECT * FROM incidents",
        "drop_table" : "DROP TABLE IF EXISTS incidents"
    }

    file_paths = {
        "local_file_path" : "dwpdf.pdf"
    }

    field_names = {
        "date_time" : "DateTime",
        "incident_number" : "IncidentNumber",
        "location" : "Location",
        "nature" : "nature",
        "incident_type" : "IncidentType"
    }

    other = {
        "provide_incidents_url" : "Please provide the --incidents argument with a URL.",
        "seperator" : "|",
        "new_line" : "\n",
        "comma" : ","
    }