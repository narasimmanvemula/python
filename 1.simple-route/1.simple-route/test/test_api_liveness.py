
import requests
import pytest

@pytest.mark.location
def test_api_provides_200_ok_response():
    url = "http://localhost:5000/api/v1/version";
    response = requests.get(url, headers={});
    assert (response.status_code == 200), "API server is not live";
	# assertEqual(response.status_code, 200)