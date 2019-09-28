import oauth2


# Function to use oauth to run scripts
def oauth_req(url, token_key, token_secret, http_method="GET", post_body=b"", http_headers=None):
    consumer = oauth2.Consumer(key=con_key, secret=con_secret)
    token = oauth2.Token(key=token_key, secret=token_secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request(url, method=http_method, body=post_body, headers=http_headers)
    return content


