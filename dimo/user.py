class User:
    def __init__(self, request_method, get_auth_headers):
        self._request = request_method
        self._get_auth_headers = get_auth_headers

    async def user(self, access_token):
        return await self._request(
            "GET", "User", "/v1/user", headers=self._get_auth_headers(access_token)
        )

    async def update_user(self, access_token, update_user_request):
        body = {"updateUserRequest": update_user_request}
        return await self._request(
            "PUT",
            "User",
            "/v1/user",
            data=body,
            headers=self._get_auth_headers(access_token),
        )

    async def delete_user(self, access_token):
        return await self._request(
            "DELETE", "User", "/v1/user", headers=self._get_auth_headers(access_token)
        )

    async def send_confirmation_email(self, access_token):
        return await self._request(
            "POST",
            "User",
            "/v1/user/send-confirmation-email",
            headers=self._get_auth_headers(access_token),
        )

    async def confirm_email(self, access_token, confirm_email_request):
        body = {"confirmEmailRequest": confirm_email_request}
        return await self._request(
            "POST",
            "User",
            "/v1/user/confirm-email",
            data=body,
            headers=self._get_auth_headers(access_token),
        )
