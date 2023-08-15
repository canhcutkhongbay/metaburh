import requests
class metaburh:
    def __init__(self, access_token):
        self.access_token = access_token
    def _send_request(self, endpoint, method='GET', params=None):
        url = f'https://graph.facebook.com/{endpoint}'
        params = params or {}
        params['access_token'] = self.access_token
        if method == 'GET':
            response = requests.get(url, params=params)
        elif method == 'POST':
            response = requests.post(url, data=params)
        else:
            raise ValueError('Unsupported HTTP method')
        return response.json()
    def like(self, post_id):
        endpoint = f'{post_id}/likes'
        return self._send_request(endpoint, method='POST')
    def cmt(self, post_id, message):
        endpoint = f'{post_id}/comments'
        params = {
            'message': message
        }
        return self._send_request(endpoint, method='POST', params=params)
    def fl(self, target_id):
        endpoint = f'{target_id}/subscribers'
        return self._send_request(endpoint, method='POST')
    def get_newfeed(self):
        endpoint = 'me/feed'
        return self._send_request(endpoint)
    def get_user_info(self, user_id):
        endpoint = user_id
        return self._send_request(endpoint)
    def ketban(self, user_id):
        endpoint = f'{user_id}/friendrequests'
        return self._send_request(endpoint, method='POST')
    def getPostUser(self, user_id):
        endpoint = f'{user_id}/posts'
        return self._send_request(endpoint)
    def chocBan(self, friend_id):
        endpoint = f'{friend_id}/pokes'
        return self._send_request(endpoint, method='POST')
