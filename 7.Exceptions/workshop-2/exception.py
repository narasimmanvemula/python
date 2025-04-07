import requests

def fetch_posts():
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError as http_error:
        # Test with https://jsonplaceholder.typicode.com/xposts
        print("HTTP Error occurred:", str(http_error))        
    except requests.exceptions.ConnectionError as connection_error:
        # Try with https://xjsonplaceholder.typicode.com/xposts
        print("Connection Error occurred:", str(connection_error))
    except requests.exceptions.Timeout as timeout_error:
        print("Timeout Error occurred:", str(timeout_error))
    except requests.exceptions.RequestException as request_exception:
        print("Request Exception occurred:", str(request_exception))
    except Exception as e:
        print("An error occurred:", str(e))

# Example usage
posts_data = fetch_posts()

if posts_data:
    # Process the posts data
    for post in posts_data:
        print("Post ID:", post['id'])
        print("Title:", post['title'])
        print("Body:", post['body'])
        print("--------------------")

"""
API:
https://jsonplaceholder.typicode.com/posts


- We define the function fetch_posts that sends an HTTP GET request to the "posts" endpoint of the JSONPlaceholder API. The response data is retrieved and returned as JSON.
- We handle the same set of exceptions as before to ensure error resilience during the API request and response process.
- After handling the exceptions, if the posts_data is available, we can iterate through the list of posts and process them accordingly. In this example, we print the post ID, title, and body for each post retrieved from the API.

"""