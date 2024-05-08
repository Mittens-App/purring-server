#  Global response object
class Response(object):
    def __init__(self, body, status):
        self.body = body
        self.status = status