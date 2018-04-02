#!/usr/bin/env python3

import requests


def send_to_api(hash, abspath, fileName, api_scheme, api_host, api_port, logger):
    """
    Send file and hash value to hash_api
    """

    url = f'{api_scheme}://{api_host}:{api_port}/api/v1/events/create'

    logger.debug(f'Requesting URL: {url}')
    r = requests.post(
        url=url,
        headers={'Content-Type': 'application/json'},
        json={
            'abspath': abspath,
            'filename': fileName,
            'hashvalue': hash
        }
    )
    resp = r.json()
    id = resp['id']
    logger.debug(f'Received response code: {r.status_code} with id: {id}')
    if r.status_code in (200, 201, 202):
        return True

    else: return False
