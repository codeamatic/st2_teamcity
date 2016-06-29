from st2actions.runners.pythonrunner import Action
import base64

import requests


class TeamCityAction(Action):
    """A simple representation of a human being.

    :param config: A list, configurations needed for communicating with TeamCity
    """
    def __init__(self, config):
        super(TeamCityAction, self).__init__(config)

        self._version = self.config['version']
        self._username = self.config['username']
        self._password = self.config['password']
        self._url = self._get_baseurl(self.config['url'])
        self._headers = self._get_headers()

    def _get_baseurl(self, url):
        """Configure base url used for all TeamCity api requests

        Args:
            url: The domain name including http/https

        Returns:
            string: URL used for TeamCity api requests
        """
        if not self.config['url']:
            raise ValueError('TeamCity url config must be defined.')

        baseuri = ""

        if url[-1] == '/':
            baseurl = url.rstrip('/')
        else:
            baseurl = url

        if self._username and self._password:
            baseuri = 'httpAuth'

        if self._version:
            baseurl += '/' + baseuri + '/app/rest' + self._version
        else:
            baseurl += '/' + baseuri + '/app/rest'

        return baseurl

    def _get_headers(self):
        """Return headers used in all requests made to the TeamCity api.

        If the a username and password has been configured, then a
        base64 encoding is created for basic authentication.
        """
        headers = {
            'Accept': 'application/json'
        }

        if self._username and self._password:
            auth_header = base64.b64encode('{}:{}'.format(self._username,
                                                          self._password))
            headers['Authorization'] = 'Basic {}'.format(auth_header)

        return headers

    def _api_get(self, endpoint, params=None):
        """Make get request to the TeamCity api.

         Args:
             endpoint: A string, endpoint uri request is being made to.
             params: A list, parameters to be added as query string members in request
        Returns:
            string: Json string response
        """
        if endpoint[0] == '/':
            endpoint = endpoint.lstrip('/')

        url = '/'.join([self._url, endpoint])
        r = requests.get(url, params, headers=self._headers)
        r.raise_for_status()
        return r.json()

    def _api_post(self, endpoint, data):
        """Make get request to the TeamCity api.

         Args:
             endpoint: A string, endpoint uri request is being made to.
             data: Json data to be added to the body of the request
        Returns:
            string: Json string response
        """
        if endpoint[0] == '/':
            endpoint = endpoint.lstrip('/')

        self._headers['Content-Type'] = 'application/xml'

        url = '/'.join([self._url, endpoint])
        r = requests.post(url, data=data, headers=self._headers)
        r.raise_for_status()
        return r.json()
