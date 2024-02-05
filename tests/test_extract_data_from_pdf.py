# import pytest
# from assignment0.main import createdb, connectdb, deletedb, extract_data_from_pdf
#
# @pytest.mark.parametrize("pdf_path, expected_count", [
#     ("/Users/aishwaryatonpe/Downloads/2024-01-04_daily_incident_summary.pdf", 336),  # Update with actual paths and expected counts
#     ("/Users/aishwaryatonpe/Downloads/2024-01-01_daily_incident_summary.pdf", 329)
#     # Add more test cases as needed
# ])
# def test_extract_data_from_pdf(pdf_path, expected_count):
#     result = extract_data_from_pdf(pdf_path)
#     assert len(result) == expected_count
#     # Add more assertions based on your specific requirements
