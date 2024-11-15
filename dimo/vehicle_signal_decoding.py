class VehicleSignalDecoding:
    def __init__(self, request_method, get_auth_headers):
        self._request = request_method
        self._get_auth_headers = get_auth_headers

    async def list_config_urls_by_vin(self, vin, protocol=None):
        params = {}
        if protocol is not None:
            params["protocol"] = protocol
        url = f"/v1/device-config/vin/{vin}/urls"
        return await self._request("GET", "VehicleSignalDecoding", url, params=params)

    async def list_config_urls_by_address(self, address, protocol=None):
        params = {}
        if protocol is not None:
            params["protocol"] = protocol
        url = f"/v1/device-config/eth-addr/{address}/urls"
        return await self._request("GET", "VehicleSignalDecoding", url, params=params)

    async def get_pid_configs(self, template_name):
        url = f"/v1/device-config/pids/{template_name}"
        return await self._request("GET", "VehicleSignalDecoding", url)

    async def get_device_settings(self, template_name):
        url = f"/v1/device-config/settings/{template_name}"
        return await self._request("GET", "VehicleSignalDecoding", url)

    async def get_dbc_text(self, template_name):
        url = f"/v1/device-config/dbc/{template_name}"
        return await self._request("GET", "VehicleSignalDecoding", url)

    async def get_device_status_by_address(self, address):
        url = f"/v1/device-config/eth-addr/{address}/status"
        return await self._request("GET", "VehicleSignalDecoding", url)

    async def set_device_status_by_address(self, privilege_token, address, config):
        body = {"config": config}
        url = f"/v1/device-config/eth-addr/{address}/status"
        return await self._request(
            "PATCH",
            "VehicleSignalDecoding",
            url,
            data=body,
            headers=self._get_auth_headers(privilege_token),
        )

    async def get_jobs_by_address(self, address):
        url = f"/v1/device-config/eth-addr/{address}/jobs"
        return await self._request("GET", "VehicleSignalDecoding", url)

    async def get_pending_jobs_by_address(self, address):
        url = f"/v1/device-config/eth-addr/{address}/jobs/pending"
        return await self._request("GET", "VehicleSignalDecoding", url)

    async def set_job_status_by_address(self, privilege_token, address, job_id, status):
        url = f"/v1/device-config/eth-addr/{address}/jobs/{job_id}/{status}"
        return await self._request(
            "PATCH",
            "VehicleSignalDecoding",
            url,
            headers=self._get_auth_headers(privilege_token),
        )
