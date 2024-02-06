import pytest
from assignment0.main import createdb, connectdb, deletedb, extract_data_from_pdf

@pytest.mark.parametrize("pdf_path, expected_count", [
    ("tmp/2024-01-01_daily_incident_summary.pdf", 329),
    ("tmp/2024-01-04_daily_incident_summary.pdf", 337)
])
def test_extract_data_from_pdf(pdf_path, expected_count):
    result = extract_data_from_pdf(pdf_path)
    assert len(result) == expected_count
