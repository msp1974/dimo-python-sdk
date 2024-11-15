class Devices:
    def __init__(self, request_method, get_auth_headers):
        self._request = request_method
        self._get_auth_headers = get_auth_headers

    async def create_vehicle(self, access_token, country_code, device_definition_id):
        body = {"countryCode": country_code, "deviceDefinitionId": device_definition_id}
        return await self._request(
            "POST",
            "Devices",
            "/v1/user/devices",
            headers=self._get_auth_headers(access_token),
            data=body,
        )

    async def create_vehicle_from_smartcar(
        self, access_token, code, country_code, redirect_uri
    ):
        body = {"code": code, "countryCode": country_code, "redirectURI": redirect_uri}
        return await self._request(
            "POST",
            "Devices",
            "/v1/user/devices/fromsmartcar",
            headers=self._get_auth_headers(access_token),
            data=body,
        )

    async def create_vehicle_from_vin(
        self, access_token, can_protocol, country_code, vin
    ):
        body = {"canProtocol": can_protocol, "countryCode": country_code, "vin": vin}
        return await self._request(
            "POST",
            "Devices",
            "/v1/user/devices/fromvin",
            headers=self._get_auth_headers(access_token),
            data=body,
        )

    async def update_vehicle_vin(self, access_token, user_device_id):
        url = f"/v1/user/devices/{user_device_id}/vin"
        return await self._request(
            "PATCH", "Devices", url, headers=self._get_auth_headers(access_token)
        )

    async def get_claiming_payload(self, access_token, serial):
        url = f"/v1/aftermarket/device/by-serial/{serial}/commands/claim"
        return await self._request(
            "POST", "Devices", url, headers=self._get_auth_headers(access_token)
        )

    async def sign_claiming_payload(self, access_token, serial, claim_request):
        body = {"claimRequest": claim_request}
        url = f"/v1/aftermarket/device/by-serial/{serial}/commands/claim"
        return await self._request(
            "POST",
            "Devices",
            url,
            headers=self._get_auth_headers(access_token),
            data=body,
        )

    async def get_minting_payload(self, access_token, user_device_id):
        url = f"/v1/user/devices/{user_device_id}/commands/mint"
        return await self._request(
            "POST", "Devices", url, headers=self._get_auth_headers(access_token)
        )

    async def sign_minting_payload(self, access_token, user_device_id, mint_request):
        body = {"mintRequest": mint_request}
        url = f"/v1/user/devices/{user_device_id}/commands/mint"
        return await self._request(
            "POST",
            "Devices",
            url,
            headers=self._get_auth_headers(access_token),
            data=body,
        )

    async def opt_in_share_data(self, access_token, user_device_id):
        url = f"/v1/user/devices/{user_device_id}/commands/opt-in"
        return await self._request(
            "POST", "Devices", url, headers=self._get_auth_headers(access_token)
        )

    async def refresh_smartcar_data(self, access_token, user_device_id):
        url = f"/v1/user/devices/{user_device_id}/commands/refresh"
        return await self._request(
            "POST", "Devices", url, headers=self._get_auth_headers(access_token)
        )

    async def get_pairing_payload(self, access_token, user_device_id):
        url = f"/v1/user/devices/{user_device_id}/aftermarket/commands/pair"
        return await self._request(
            "GET", "Devices", url, headers=self._get_auth_headers(access_token)
        )

    async def sign_pairing_payload(self, access_token, user_device_id, user_signature):
        body = {"userSignature": user_signature}
        url = f"/v1/user/devices/{user_device_id}/aftermarket/commands/pair"
        return await self._request(
            "POST",
            "Devices",
            url,
            headers=self._get_auth_headers(access_token),
            data=body,
        )

    async def get_unpairing_payload(self, access_token, user_device_id):
        url = f"/v1/user/devices/{user_device_id}/aftermarket/commands/unpair"
        return await self._request(
            "GET", "Devices", url, headers=self._get_auth_headers(access_token)
        )

    async def sign_unpairing_payload(
        self, access_token, user_device_id, user_signature
    ):
        body = {"userSignature": user_signature}
        url = f"/v1/user/devices/{user_device_id}/aftermarket/commands/unpair"
        return await self._request(
            "POST",
            "Devices",
            url,
            headers=self._get_auth_headers(access_token),
            data=body,
        )

    async def lock_doors(self, privilege_token, token_id):
        url = f"/v1/vehicle/{token_id}/commands/doors/lock"
        return await self._request(
            "POST", "Devices", url, headers=self._get_auth_headers(privilege_token)
        )

    async def unlock_doors(self, privilege_token, token_id):
        url = f"/v1/vehicle/{token_id}/commands/doors/unlock"
        return await self._request(
            "POST", "Devices", url, headers=self._get_auth_headers(privilege_token)
        )

    async def open_frunk(self, privilege_token, token_id):
        url = f"/v1/vehicle/{token_id}/commands/frunk/open"
        return await self._request(
            "POST", "Devices", url, headers=self._get_auth_headers(privilege_token)
        )

    async def open_trunk(self, privilege_token, token_id):
        url = f"/v1/vehicle/{token_id}/commands/trunk/open"
        return await self._request(
            "POST", "Devices", url, headers=self._get_auth_headers(privilege_token)
        )

    async def list_error_codes(self, access_token, user_device_id):
        url = f"/v1/user/devices/{user_device_id}/error-codes"
        return await self._request(
            "GET", "Devices", url, headers=self._get_auth_headers(access_token)
        )

    async def submit_error_codes(
        self, access_token, user_device_id, query_device_error_codes
    ):
        body = {"queryDeviceErrorCodes": query_device_error_codes}
        url = f"/v1/user/devices/{user_device_id}/error-codes"
        return await self._request(
            "POST",
            "Devices",
            url,
            headers=self._get_auth_headers(access_token),
            data=body,
        )

    async def clear_error_codes(self, access_token, user_device_id):
        url = f"/v1/user/devices/{user_device_id}/error-codes/clear"
        return await self._request(
            "POST", "Devices", url, headers=self._get_auth_headers(access_token)
        )

    async def get_aftermarket_device(self, token_id):
        url = f"/v1/aftermarket/device/{token_id}"
        self._request("GET", "Devices", url)

    async def get_aftermarket_device_image(self, token_id):
        url = f"/v1/aftermarket/device/{token_id}/image"
        self._request("GET", "Devices", url)

    async def get_aftermarket_device_metadata_by_address(self, address):
        url = f"/v1/aftermarket/device/by-address/{address}"
        self._request("GET", "Devices", url)
