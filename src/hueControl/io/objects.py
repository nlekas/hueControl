import json
from typing import Dict, Optional

import requests


class Io:
    def __init__(
        self,
        bridge: str,
        user: str,
    ):
        self.bridge: str = bridge
        self.user: str = user
        self.headers: Dict = {"hue-application-key": user}
        self.base_url: str = f"https://{bridge}/clip/v2"

    def get(self, path: str, id: Optional[str]) -> Optional[Dict]:
        url = f"{self.base_url}/{path}"
        res = requests.get(url, verify=False, headers=self.headers)
        if res.ok:
            return res.json()
        else:
            return None

    def put(self, path: str, payload: Dict) -> bool:
        url = f"{self.base_url}/{path}"
        payload_str: str = json.dumps(payload)
        res = requests.put(
            url=url, verify=False, headers=self.headers, data=payload_str
        )
        if res.ok:
            return True
        else:
            return False

    def post(self, path: str, payload: Dict, id: str) -> bool:
        url = f"{self.base_url}/{path}/{id}"
        payload_str: str = json.dumps(payload)
        res = requests.post(
            url=url, verify=False, headers=self.headers, data=payload_str
        )
        if res.ok:
            return True
        else:
            return False

    def delete(self, path: str, id: str):
        url = f"{self.base_url}/{path}/{id}"
        res = requests.delete(url=url, verify=False, headers=self.headers)
        if res.ok:
            return True
        else:
            return False
