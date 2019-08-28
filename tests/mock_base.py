class MockBase(object):
    #def __init__(self, json_data, status_code):

    class MockGetResponse(object):
        
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code
        
        def json(self):
            return self.json_data

    class MockPostResponse(object):
        
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    def mock_get(*args, **kwargs):
        # Raise not-implemented-error instead?
        pass