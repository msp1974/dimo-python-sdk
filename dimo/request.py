import json
import requests
import asyncio


class Request:
    session = requests.Session()

    def __init__(self, http_method, url):
        self.http_method = http_method
        self.url = url

    async def make_request(self, headers=None, data=None, params=None, **kwargs):
        headers = headers or {}
        headers.update(kwargs.pop("headers", {}))

        if (
            data
            and isinstance(data, dict)
            and headers.get("Content-Type") == "application/json"
        ):
            data = json.dumps(data)

        loop = asyncio.get_running_loop()
        result = await loop.run_in_executor(
            None, self.execute_request, headers, data, params, **kwargs
        )
        return result

    def execute_request(self, headers=None, data=None, params=None, **kwargs):
        response = self.session.request(
            method=self.http_method,
            url=self.url,
            params=params,
            data=data,
            headers=headers,
            **kwargs,
        )

        # TODO: Better error responses
        response.raise_for_status()

        if response.content:
            return response.json()
        return None
