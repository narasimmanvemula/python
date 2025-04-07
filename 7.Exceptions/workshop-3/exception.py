# For a given post, get the post details

import requests

def fetch_post(post_id):
    try:
        url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError as http_error:
        print("HTTP Error occurred:", str(http_error))
    except requests.exceptions.ConnectionError as connection_error:
        print("Connection Error occurred:", str(connection_error))
    except requests.exceptions.Timeout as timeout_error:
        print("Timeout Error occurred:", str(timeout_error))
    except requests.exceptions.RequestException as request_exception:
        print("Request Exception occurred:", str(request_exception))
    except Exception as e:
        print("An error occurred:", str(e))

# Example usage
post_id = 1
post_data = fetch_post(post_id)

if post_data:
    print("Post ID:", post_data['id'])
    print("Title:", post_data['title'])
    print("Body:", post_data['body'])
    print("--------------------")
