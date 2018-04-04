#!/usr/bin/env python3

import json

import requests


class HashApi(object):
    def __init__(self, api_scheme, api_host, api_port, version, username, password):
        self.api_scheme = api_scheme
        self.api_host = api_host
        self.api_port = api_port
        self.version = version
        self.username = username
        self.password = password
        self.hash_api_url = '{0}://{1}:{2}/api/v{3}'.format(
            self.api_scheme, self.api_host, self.api_port, self.version
        )
        self.auth_url = f'{self.hash_api_url}/user/auth'
        self.refresh_url = f'{self.hash_api_url}/token/refresh'
        self.logout_url = f'{self.hash_api_url}/user/logout'
        self.hash_event_url = f'{self.hash_api_url}/events/create'
        self.hash_api_headers = {'Content-Type': 'application/json'}


class HttpClient(HashApi):
    def __init__(
        self, api_scheme, api_host, api_port, logger, version, username, password
    ):
        super().__init__(api_scheme, api_host, api_port, version, username, password)
        self.log = logger
        self.access_token = None
        self.refresh_token = None

    def get_jwt_token(self):
        try:
            self.log.debug('[!] Requesting an initial access token.')
            r = requests.post(
                url=self.auth_url,
                headers=self.hash_api_headers,
                json={
                    'username': self.username,
                    'password': self.password
                }
            )
            if r.status_code in (200, 201, 202):
                self.log.debug('[!] Received initial access token.')
                response = json.loads(r.content.decode('utf-8'))
                self.access_token = response['access_token']
                self.refresh_token = response['refresh_token']
                return response

            else:
                self.log.error(f'[-] Received invalid response code: {r.status_code}')
                return None

        except requests.exceptions.Timeout as error:
            self.log.error(f'[-] Request Timeout Error Occurred: {error}')
            return None

        except requests.exceptions.ConnectionError as error:
            self.log.error(f'[-] Request Connection Error Occurred: {error}')
            return None

        except requests.exceptions.RequestException as error:
            self.log.error(f'[-] Generic Request Exception Occurred: {error}')
            return None

    def refresh_access_token(self):
        try:
            self.log.debug('[!] Requesting new access and refresh tokens.')
            self.hash_api_headers['Authorization'] = f'Bearer {self.refresh_token}'
            r = requests.post(
                url=self.refresh_url,
                headers=self.hash_api_headers
            )
            if r.status_code in (200, 201, 202):
                self.log.debug('[!] Received new access and refresh tokens.')
                response = json.loads(r.content.decode('utf-8'))
                self.access_token = response['access_token']
                self.refresh_token = response['refresh_token']
                return True

        except requests.exceptions.Timeout as error:
            self.log.error(f'[-] Request Timeout Error Occurred: {error}')
            return None

        except requests.exceptions.ConnectionError as error:
            self.log.error(f'[-] Request Connection Error Occurred: {error}')
            return None

        except requests.exceptions.RequestException as error:
            self.log.error(f'[-] Generic Request Exception Occurred: {error}')
            return None

    def send_hash_event(self, payload):
        try:
            self.log.debug('[!] Sending hash events: {}'.format(len(payload)))
            self.hash_api_headers['Authorization'] = f'Bearer {self.access_token}'
            r = requests.post(
                url=self.hash_event_url,
                headers=self.hash_api_headers,
                json=payload
            )
            if r.status_code == 401:
                self.log.debug('[!] Refreshing token')
                token_updated = self.refresh_access_token()
                if token_updated:
                    self.send_hash_event(payload=payload)

            elif r.status_code in (200, 201, 202):
                self.log.debug('[!] Successfully processed hash event.')
                response = json.loads(r.content.decode('utf-8'))
                return response

            else:
                self.log.error(f'[-] Received invalid response code: {r.status_code}')
                return None

        except requests.exceptions.Timeout as error:
            self.log.error(f'[-] Request Timeout Error Occurred: {error}')
            return None

        except requests.exceptions.ConnectionError as error:
            self.log.error(f'[-] Request Connection Error Occurred: {error}')
            return None

        except requests.exceptions.RequestException as error:
            self.log.error(f'[-] Generic Request Exception Occurred: {error}')
            return None

    def destroy_auth_token(self):
        try:
            self.log.debug('[!] Received token destroy request.')
            self.hash_api_headers['Authorization'] = f'Bearer {self.access_token}'
            r = requests.delete(
                url=self.logout_url,
                headers=self.hash_api_headers
            )
            if r.status_code in (200, 201, 202):
                self.log.debug('[!] Successfully processed token destroy event.')
                response = json.loads(r.content.decode('utf-8'))
                return response

            else:
                self.log.error(f'[-] Received invalid response code: {r.status_code}')
                return None

        except requests.exceptions.Timeout as error:
            self.log.error(f'[-] Request Timeout Error Occurred: {error}')
            return None

        except requests.exceptions.ConnectionError as error:
            self.log.error(f'[-] Request Connection Error Occurred: {error}')
            return None

        except requests.exceptions.RequestException as error:
            self.log.error(f'[-] Generic Request Exception Occurred: {error}')
            return None
