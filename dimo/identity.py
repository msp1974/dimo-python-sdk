class Identity:
    def __init__(self, dimo_instance):
        self.dimo = dimo_instance

    # Primary query method
    async def query(self, query):
        return await self.dimo.query("Identity", query)

    # Sample query - count DIMO vehicles
    async def count_dimo_vehicles(self):
        query = """
      {
          vehicles (first:10) {
              totalCount,
          }
      }
      """
        return await self.dimo.query("Identity", query)

    # Sample query - list vehicle definitions per address
    async def list_vehicle_definitions_per_address(self, address, limit):
        query = """
      query ListVehicleDefinitionsPerAddress($owner: Address!, $first: Int!) {
        vehicles(filterBy: {owner: $owner}, first: $first) {
          nodes {
            aftermarketDevice {
              tokenId
              address
            }
            syntheticDevice {
              address
              tokenId
            }
            definition {
              make
              model
              year
            }
          }
        }
      }
      """
        variables = {"owner": address, "first": limit}

        return await self.dimo.query("Identity", query, variables=variables)

    # Sample query - MMY per owner
    async def mmy_by_owner(self, address, limit):
        query = """
    query MMYByOwner($owner: Address!, $first: Int!) {
      vehicles(filterBy: {owner: $owner}, first: $first) {
        nodes {
          definition {
            make
            model
            year
          }
        }
      }
    }
    """
        variables = {"owner": address, "first": limit}

        return await self.dimo.query("Identity", query, variables=variables)

    # Sample query - tokenIDs & privileges by owner
    async def list_token_ids_privileges_by_owner(
        self, address, vehicle_limit, privileges_limit
    ):
        query = """
    query TokenIDsPrivilegesByOwner($owner: Address!, $firstVehicles: Int!, $firstPrivileges: Int!) {
      vehicles(filterBy: {owner: $owner}, first: $firstVehicles) {
        nodes {
          tokenId
          privileges(first: $firstPrivileges) {
            nodes {
              setAt
              expiresAt
              id
            }
          }
        }
      }
    }
    """
        variables = {
            "owner": address,
            "firstVehicles": vehicle_limit,
            "firstPrivileges": privileges_limit,
        }

        return await self.dimo.query("Identity", query, variables=variables)

    # Sample query - list of tokenIDs granted to a dev from an owner
    async def list_token_ids_granted_to_dev_by_owner(
        self, dev_address, owner_address, limit
    ):
        query = """
    query ListTokenIdsGrantedToDevByOwner($privileged: Address!, $owner: Address!, $first: Int!) {
      vehicles(filterBy: {privileged: $privileged, owner: $owner}, first: $first) {
        nodes {
          tokenId
          definition {
            make
          }
          aftermarketDevice {
            manufacturer {
              name
            }
          }
        }
      }
    }
      """
        variables = {"owner": owner_address, "privileged": dev_address, "first": limit}

        return await self.dimo.query("Identity", query, variables=variables)

    # Sample query - DCNs by Owner
    async def dcn_by_owner(self, address, limit):
        query = """
    query DCNByOwner($owner: Address!, $first: Int!) {
      vehicles(filterBy: {owner: $owner}, first: $first) {
        nodes {
          dcn {
            node
            name
            vehicle {
              tokenId
            }
          }
        }
      }
    }
    """
        variables = {"owner": address, "first": limit}

        return await self.dimo.query("Identity", query, variables=variables)

    # Sample query - MMY by TokenID
    async def mmy_by_token_id(self, token_id):
        query = """
      query MMYByTokenID($tokenId: Int!) {
        vehicle (tokenId: $tokenId) {
          aftermarketDevice {
            tokenId
            address
          }
          syntheticDevice {
            tokenId
            address
          }
          definition {
            make
            model
            year
          }
        }
      }
      """
        variables = {"tokenId": token_id}

        return await self.dimo.query("Identity", query, variables=variables)

    # Sample query - Rewards by owner
    async def rewards_by_owner(self, address):
        query = """
      query RewardsByOwner($owner: Address!) {
        rewards (user: $owner) {
          totalTokens
        }
      }
      """
        variables = {"owner": address}

        return await self.dimo.query("Identity", query, variables=variables)

    # Sample query - get rewards history by owner
    async def rewards_history_by_owner(self, address, limit):
        query = """
      query GetVehicleDataByOwner($owner: Address!, $first: Int!) {
        vehicles (filterBy: {owner: $owner}, first: $first) {
          nodes {
            earnings {
              history (first: $first) {
                edges {
                  node {
                    week
                    aftermarketDeviceTokens
                    syntheticDeviceTokens
                    sentAt
                    beneficiary
                    connectionStreak
                    streakTokens
                  }
                }
              }
              totalTokens
            }
          }
        }
      }
      """
        variables = {"owner": address, "first": limit}

        return await self.dimo.query("Identity", query, variables=variables)
