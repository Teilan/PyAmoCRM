class OAuthTokenManager:
    def __init__(self, client_id, client_secret, grant_type, code, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.grant_type = grant_type
        self.code = code
        self.redirect_uri = redirect_uri

    def creates_tokens(self): ...

    def save_tokens(self): ...
