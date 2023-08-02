import requests


class Post:
    def __init__(self):
        url = "https://api.npoint.io/d8332566712a9f862efc"
        response = requests.get(url)
        response.raise_for_status()

        self.blogs_data = response.json()

    def get_all_posts(self):
        return self.blogs_data

    def get_post(self, num):
        # convert post number string to array integer index.
        num = int(num) - 1
        return self.blogs_data[num]
