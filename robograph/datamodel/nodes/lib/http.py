import requests

from robograph.datamodel.base import node


class HttpClient(node.Node):

    """
    Abstract base class for HTTP methods wrappers
    Requirements:
      url --> str, the URL to be called
      headers --> dict, HTTP headers (optional)
      auth --> tuple, username and password for basic HTTP authentication (optional)
      timeout_secs --> int, how many secs wait before stopping to wait for server response (optional)
      verify_ssl --> bool, whether to check for SSL certs validity or not (optional)
    """

    _reqs = ['url', 'headers', 'auth', 'timeout_secs', 'verify_ssl']
    DEFAULT_TIMEOUT_SECS = 3

    def _encode_payload(self, response, mime_type):
        if 'json' in mime_type:  # json
            return response.json()
        elif 'text' in mime_type:  # text
            return response.text
        else:
            return response.content  # binary data


# Status codes

class StatusCode(node.Node):
    """
    This node returns the status code of a raw HTTP response (requests.Response)
    Requirements:
      response --> requests.Response object
    """
    _reqs = ['response']

    def output(self):
        return self._params['response'].status_code


class StatusCodeOk(node.Node):
    """
    This node tells whether the status code of a raw HTTP response
    (requests.Response)is OK (2xx) or not
    Requirements:
      response --> requests.Response object
    """
    _reqs = ['response']

    def output(self):
        sc = self._params['response'].status_code
        return sc >= 200 and sc < 300


# GET

class RawGet(HttpClient):
    """
    This node returns a raw HTTP response (requests.Response) to a GET request
    Requirements:
      query --> dict, query parameters (optional)
    """

    _reqs = HttpClient._reqs + ['query']

    def output(self):
        r = requests.get(
            self._params['url'],
            auth=self._params['auth'],
            params=self._params['query'],
            headers=self._params['headers'],
            timeout=self._params['timeout_secs'] or self.DEFAULT_TIMEOUT_SECS,
            verify=self._params['verify_ssl'] if self._params['verify_ssl'] is not None else True)
        return r


class Get(RawGet):
    """
    This node returns the payload response to a HTTP GET call. The payload format
    depends on the specified MIME type
    Requirements:
      mime_type --> str, MIME type for server response payload
    """

    _reqs = RawGet._reqs + ['mime_type']

    def output(self):
        raw_response = RawGet.output(self)
        payload = self._encode_payload(raw_response,
                                       self._params['mime_type'] or 'application/json')
        return payload


# POST

class RawPost(HttpClient):
    """
    This node returns a raw HTTP response (requests.Response) to a POST request
    Requirements:
      post_data --> dict, the post-ed form data
      files --> dict, multipart post-ed data (optional)
    """

    _reqs = HttpClient._reqs + ['post_data', 'files']

    def output(self):
        r = requests.post(
            self._params['url'],
            data=self._params['post_data'],
            auth=self._params['auth'],
            files=self._params['files'],
            headers=self._params['headers'],
            timeout=self._params['timeout_secs'] or self.DEFAULT_TIMEOUT_SECS,
            verify=self._params['verify_ssl'] if self._params['verify_ssl'] is not None else True)
        return r


class Post(RawPost):
    """
    This node returns the payload response to a HTTP POST call. The payload format
    depends on the specified MIME type
    Requirements:
      mime_type --> str, MIME type for server response payload
    """

    _reqs = RawPost._reqs + ['mime_type']

    def output(self):
        raw_response = RawPost.output(self)
        payload = self._encode_payload(raw_response,
                                       self._params['mime_type'] or 'application/json')
        return payload


# PUT

class RawPut(HttpClient):
    """
    This node returns a raw HTTP response (requests.Response) to a PUT request
    Requirements:
      put_data --> dict, the put form data (optional)
    """

    _reqs = HttpClient._reqs + ['put_data']

    def output(self):
        r = requests.put(
            self._params['url'],
            data=self._params['put_data'],
            auth=self._params['auth'],
            headers=self._params['headers'],
            timeout=self._params['timeout_secs'] or self.DEFAULT_TIMEOUT_SECS,
            verify=self._params['verify_ssl'] if self._params['verify_ssl'] is not None else True)
        return r


class Put(RawPut):
    """
    This node returns the payload response to a HTTP PUT call. The payload format
    depends on the specified MIME type
    Requirements:
      mime_type --> str, MIME type for server response payload
    """

    _reqs = RawPut._reqs + ['mime_type']

    def output(self):
        raw_response = RawPut.output(self)
        payload = self._encode_payload(raw_response,
                                       self._params['mime_type'] or 'application/json')
        return payload


# DELETE

class RawDelete(HttpClient):
    """
    This node returns a raw HTTP response (requests.Response) to a DELETE request
    Requirements:
      delete_data --> dict, the delete form data (optional)
    """

    _reqs = HttpClient._reqs + ['delete_data']

    def output(self):
        r = requests.put(
            self._params['url'],
            data=self._params['delete_data'],
            auth=self._params['auth'],
            headers=self._params['headers'],
            timeout=self._params['timeout_secs'] or self.DEFAULT_TIMEOUT_SECS,
            verify=self._params['verify_ssl'] if self._params['verify_ssl'] is not None else True)
        return r


class Delete(RawDelete):
    """
    This node returns the payload response to a HTTP DELETE call. The payload
    format depends on the specified MIME type
    Requirements:
      mime_type --> str, MIME type for server response payload
    """

    _reqs = RawDelete._reqs + ['mime_type']

    def output(self):
        raw_response = RawDelete.output(self)
        payload = self._encode_payload(raw_response,
                                       self._params['mime_type'] or 'application/json')
        return payload
