const listConnections = {
  results: [
    {
      accept: 'auto',
      state: 'active',
      my_did: 'BEQWiPfQXj9q9DYePziaJ2',
      connection_id: 'bb6f8738-b3ee-46e4-b979-a84e6b269a0a',
      invitation_key: 'B6nQE8AjZHoYC3VgDapLGbD8iZJ6cHAepMq3evLaq6hg',
      invitation_mode: 'once',
      routing_state: 'none',
      alias: 'Btest',
      their_did: 'Tr23L12egq68Ei3Q8uYAeg',
      updated_at: '2023-06-26T22:28:49.084854Z',
      their_label: 'BBB Wallet',
      rfc23_state: 'completed',
      created_at: '2023-06-26T22:28:19.163437Z',
      connection_protocol: 'connections/1.0',
      their_role: 'invitee',
    },
    {
      accept: 'auto',
      state: 'not_active',
      my_did: 'SW9RZUxWXBgSpSvLUgS7Ne',
      connection_id: '97bacd18-2b4e-47e8-81b4-a7e7c7ef64d7',
      invitation_key: 'BHYQq7uYgvtEECn2zXSbig5NVqU7vaeDF2auLVPNDdhF',
      invitation_mode: 'once',
      routing_state: 'none',
      alias: 'Atest',
      their_did: 'QXpNavd16ts8MocfWTFMT8',
      updated_at: '2023-06-26T22:30:51.933421Z',
      their_label: 'CCC Wallet',
      rfc23_state: 'completed',
      created_at: '2023-06-26T22:30:51.421112Z',
      connection_protocol: 'connections/1.0',
      their_role: 'invitee',
    },
    {
      accept: 'auto',
      state: 'active',
      my_did: 'SW9RZUxWXBgSpSvLUgS7Ne',
      connection_id: '97bacd18-2b4e-47e8-81b4-a7e7c7ef64d7',
      invitation_key: 'BHYQq7uYgvtEECn2zXSbig5NVqU7vaeDF2auLVPNDdhF',
      invitation_mode: 'once',
      routing_state: 'none',
      alias: 'Atest',
      their_did: 'QXpNavd16ts8MocfWTFMT8',
      updated_at: '2023-06-26T22:30:51.933421Z',
      their_label: 'AAA Wallet',
      rfc23_state: 'completed',
      created_at: '2023-06-26T22:30:51.421112Z',
      connection_protocol: 'connections/1.0',
      their_role: 'invitee',
    },
  ],
};

const createConnection = {
  connection_id: 'ca1f226e-626c-43dd-b063-dcd06861d116',
  invitation: {
    '@type': 'https://didcomm.org/connections/1.0/invitation',
    '@id': 'fb084711-ab6f-4588-b644-bacfd7a2aedc',
    label: 'Jamie',
    recipientKeys: ['6dS92vrNX8eWmxUGVc4ffi7goYZ6JzPCrpwcsWTwi9zu'],
    serviceEndpoint: 'https:endpoint.com',
  },
  invitation_url:
    'https:endpoint.com?c_i=eyJAdHlwZSI6ICJodHRwczovL2RpZGNvbW0ub3JnL2Nvbm5lY3Rpb25zLzEuMC9pbnZpdGF0aW9uIiwgIkBpZCI6ICJmYjA4NDcxMS1hYjZmLTQ1ODgtYjY0NC1iYWNmZDdhMmFlZGMiLCAibGFiZWwiOiAiSmFtaWUiLCAicmVjaXBpZW50S2V5cyI6IFsiNmRTOTJ2ck5YOGVXbXhVR1ZjNGZmaTdnb1laNkp6UENycHdjc1dUd2k5enUiXSwgInNlcnZpY2VFbmRwb2ludCI6ICJodHRwczovLzI2ODItNzAtNjYtMTQwLTEwNS5uZ3Jvay1mcmVlLmFwcCJ9',
  alias: 'test.invitation',
};

const receiveInvitation = {
  accept: 'auto',
  state: 'request',
  my_did: 'CV6hpNHfEZC6XiUdNeHSpX',
  connection_id: '0dbf3d6d-ae96-4c81-8e6a-24350fd830ff',
  invitation_key: '7pZ4SMd7KBDSqPT2HUnsbocJ1YjZQMrzzcGcsfN5NfTr',
  invitation_mode: 'once',
  routing_state: 'none',
  invitation_msg_id: '8fbc2934-f7d1-4f46-aa98-41252847b3b9',
  alias: 'faber.agent',
  updated_at: '2023-06-30T22:04:05.287225Z',
  their_label: 'Jamie',
  rfc23_state: 'request-sent',
  created_at: '2023-06-30T22:04:05.229798Z',
  connection_protocol: 'connections/1.0',
  their_role: 'inviter',
  request_id: '657093be-86dd-4650-86b9-ea8ed454997d',
};

const getContact = {
  invitation_mode: 'once',
  their_did: 'CvcxvRBZLccBNF16DrPQC6',
  accept: 'manual',
  their_role: 'inviter',
  my_did: 'X3N8xPdizduz1ArZZpKxmg',
  connection_protocol: 'didexchange/1.0',
  updated_at: '2023-07-05T16:13:15.717908Z',
  rfc23_state: 'completed',
  request_id: 'f90ffe70-89bc-4b20-b43c-e875c1863fd9',
  alias: 'endorser',
  their_public_did: 'SVfHGCEEvEFmpBPcxgNqRR',
  routing_state: 'none',
  state: 'active',
  connection_id: 'e4f01e1e-99db-4241-aa56-132b0aaa0178',
  created_at: '2023-07-05T16:13:14.305039Z',
};

const getConnectionInvitation = {
  connection_id: '6ed3f674-a204-4171-939f-e2b3bc7257b5',
  invitation: {
    '@type': 'https://didcomm.org/connections/1.0/invitation',
    '@id': 'e010b0bc-5785-4438-949c-ebe76ccd7613',
    serviceEndpoint: 'https://33ad-70-66-140-105.ngrok-free.app',
    recipientKeys: ['3TYBV3sYokWP5abzTerpd5GPFkKbbfmcAz3NS8obxhUL'],
    label: 'Jamie',
  },
  invitation_url:
    'https://33ad-70-66-140-105.ngrok-free.app?c_i=eyJAdHlwZSI6ICJodHRwczovL2RpZGNvbW0ub3JnL2Nvbm5lY3Rpb25zLzEuMC9pbnZpdGF0aW9uIiwgIkBpZCI6ICJlMDEwYjBiYy01Nzg1LTQ0MzgtOTQ5Yy1lYmU3NmNjZDc2MTMiLCAic2VydmljZUVuZHBvaW50IjogImh0dHBzOi8vMzNhZC03MC02Ni0xNDAtMTA1Lm5ncm9rLWZyZWUuYXBwIiwgInJlY2lwaWVudEtleXMiOiBbIjNUWUJWM3NZb2tXUDVhYnpUZXJwZDVHUEZrS2JiZm1jQXozTlM4b2J4aFVMIl0sICJsYWJlbCI6ICJKYW1pZSJ9',
  alias: 'test.invitation',
};

const didExchange = {
  accept: 'auto',
  alias: 'Bob, providing quotes',
  connection_id: '3fa85f64-5717-4562-b3fc-2c963f66afa6',
  connection_protocol: 'connections/1.0',
  created_at: '2021-12-31T23:59:59Z',
  error_msg: 'No DIDDoc provided; cannot connect to public DID',
  inbound_connection_id: '3fa85f64-5717-4562-b3fc-2c963f66afa6',
  invitation_key: 'H3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV',
  invitation_mode: 'once',
  invitation_msg_id: '3fa85f64-5717-4562-b3fc-2c963f66afa6',
  my_did: 'WgWxqztrNooG92RXvxSTWv',
  request_id: '3fa85f64-5717-4562-b3fc-2c963f66afa6',
  rfc23_state: 'invitation-sent',
  routing_state: 'active',
  state: 'active',
  their_did: 'WgWxqztrNooG92RXvxSTWv',
  their_label: 'Bob',
  their_public_did: '2cpBmR3FqGKWi5EyUbpRY8',
  their_role: 'requester',
  updated_at: '2021-12-31T23:59:59Z',
};

export default {
  createConnection,
  didExchange,
  getConnectionInvitation,
  getContact,
  listConnections,
  receiveInvitation,
};
