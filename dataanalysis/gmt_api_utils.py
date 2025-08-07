import requests

def fetch_phase_stats(selected_id, api_key):
    """
    Fetch phase stats for a given run ID from the GMT API.
    Args:
        selected_id (str): The run ID to fetch phase stats for.
        api_key (str): The API key for authentication.
    Returns:
        dict: The phase stats data, or None if the request fails.
    """
    url = f"https://api.green-coding.io/v1/phase_stats/single/{selected_id}"
    headers = {
        "x-authentication": api_key
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('data', {}).get('data', {})
    else:
        print(f"Failed to fetch phase stats for Run ID {selected_id}: {response.status_code} {response.reason}")
        return None

def get_run_ids(repository_url, api_key):
    """
    Call GMT API to get run IDs for the specified repository.
    Args:
        repository_url (str): The repository URL to query.
        api_key (str): The API key for authentication.
    Returns:
        requests.Response: The response object from the API call.
    """
    url = "https://api.green-coding.io/v2/runs"
    headers = {
        "x-authentication": api_key
    }
    params = {
        "uri": repository_url
    }
    response = requests.get(url, headers=headers, params=params)
    print(f"Request Status: {response.status_code} {response.reason}")
    response_json = response.json()
    print(f"Number of Runs: {len(response_json.get('data', []))}")
    return response

def fetch_measurement_data(run_id, api_key):
    url = f"https://api.green-coding.io/v1/measurements/single/{run_id}"
    headers = {
        "x-authentication": api_key
    }
    response = requests.get(url, headers=headers)
    return response.json()
