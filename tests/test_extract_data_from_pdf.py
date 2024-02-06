import pytest
from assignment0.main import createdb, connectdb, deletedb, extract_data_from_pdf
from assignment0.constants import strings

@pytest.mark.parametrize("pdf_path, expected_count", [
    (strings.test_constants["extract_data_test_url_1"], strings.test_constants["extract_data_test_expected_count_1"]),
    (strings.test_constants["extract_data_test_url_2"], strings.test_constants["extract_data_test_expected_count_2"])
])
def test_extract_data_from_pdf(pdf_path, expected_count):
    result = extract_data_from_pdf(pdf_path)
    assert len(result) == expected_count
