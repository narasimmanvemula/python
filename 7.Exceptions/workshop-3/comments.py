# Fetch all comments for a given post (post id)

import requests

def fetch_post_comments(post_id):
    try:
        url = f'https://jsonplaceholder.typicode.com/posts/{post_id}/comments'
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
comments_data = fetch_post_comments(post_id)

if comments_data:
    print("Comments for Post ID:", post_id)
    for comment in comments_data:
        print("Comment ID:", comment['id'])
        print("Name:", comment['name'])
        print("Email:", comment['email'])
        print("Body:", comment['body'])
        print("--------------------")
