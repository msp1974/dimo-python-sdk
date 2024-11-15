from web3 import Web3
from eth_account.messages import encode_defunct
from dimo.constants import dimo_constants
from urllib.parse import urlencode


class Auth:
    def __init__(self, request_method, get_auth_headers):
        self._request = request_method
        self._get_auth_headers = get_auth_headers

    async def generate_challenge(
        self,
        client_id,
        domain,
        address,
        headers,
        scope="openid email",
        response_type="code",
    ):
        body = {
            "client_id": client_id,
            "domain": domain,
            "scope": scope,
            "response_type": response_type,
            "address": address,
        }
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        return await self._request(
            "POST",
            "Auth",
            "/auth/web3/generate_challenge",
            data=urlencode(body),
            headers=headers,
        )

    async def sign_challenge(self, message, private_key, env="Production"):
        web3 = Web3(Web3.HTTPProvider(dimo_constants[env]["RPC_provider"]))
        signed_message = web3.eth.account.sign_message(
            encode_defunct(text=message), private_key=private_key
        )
        return signed_message.signature.hex()

    async def submit_challenge(self, form_data, headers):
        return await self._request(
            "POST",
            "Auth",
            "/auth/web3/submit_challenge",
            data=form_data,
            headers=headers,
        )

    # Requires client_id, domain, and private_key. Address defaults to client_id.
    async def get_token(
        self,
        client_id,
        domain,
        private_key,
        address=None,
        scope="openid email",
        response_type="code",
        grant_type="authorization_code",
        env="Production",
    ):
        if address is None:
            address = client_id

        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        challenge = await self.generate_challenge(
            headers=headers,
            client_id=client_id,
            domain=domain,
            scope=scope,
            response_type=response_type,
            address=address,
        )

        sign = await self.sign_challenge(
            message=challenge["challenge"], private_key=private_key, env=env
        )

        body = {
            "client_id": client_id,
            "domain": domain,
            "state": challenge["state"],
            "signature": sign,
            "grant_type": grant_type,
        }

        submit = await self.submit_challenge(body, headers)
        return submit
