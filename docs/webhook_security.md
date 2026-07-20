# Webhook Authentication Security

## Overview

Webhook authentication ensures that only trusted Endpoint Detection and Response (EDR) systems can send security alerts to the backend.

Without authentication, anyone could send fake HTTP requests, which could create false incidents or disrupt the security workflow.

The current implementation uses a simple API key verification mechanism with MockEDR.

---

# Why Webhook Authentication is Necessary

Webhooks receive HTTP requests from external systems.

If the backend accepts every incoming request without verification, attackers could:

- Send fake security alerts.
- Trigger unnecessary incident responses.
- Flood the system with malicious requests.
- Cause denial-of-service conditions.
- Reduce trust in security alerts.

Authentication prevents unauthorized systems from accessing the webhook endpoint.

---

# Trusted EDR Providers

Only trusted EDR platforms should be allowed to communicate with the backend.

Examples include:

- MockEDR (Current)
- CrowdStrike Falcon (Future)
- Microsoft Defender for Endpoint (Future)

The backend verifies every incoming request before processing the alert.

---

# API Endpoint

```
POST /api/v1/webhooks/edr
```

---

# Required Header

```
X-API-Key: mock-edr-secret
```

The X-API-Key header contains a shared secret between MockEDR and the backend.

---

# Authentication Process

Every incoming webhook request follows these steps:

```
MockEDR
      │
      ▼
Webhook Endpoint
      │
      ▼
Verify X-API-Key
      │
      ▼
Parser
      │
      ▼
Incident Orchestrator
```

---

# Successful Authentication

If the API key is correct:

- Request is accepted.
- Webhook data is processed.
- Parser extracts security event details.
- Incident Orchestrator handles the alert.

Response:

```
200 OK
```

Message:

```
Webhook authenticated successfully.
```

---

# Invalid API Key

If the provided API key is incorrect:

- Request is rejected immediately.
- No processing occurs.
- Parser is never executed.
- Incident Orchestrator is never reached.

Flow:

```
MockEDR
      │
      ▼
Webhook Endpoint
      │
      ▼
Verify API Key
      │
      ▼
401 Unauthorized
```

Response:

```
401 Unauthorized
```

Message:

```
Invalid API key.
```

---

# Missing API Key

If the X-API-Key header is missing:

- Authentication fails.
- Backend rejects the request.
- No security event is processed.

Response:

```
401 Unauthorized
```

Message:

```
Missing API key.
```

---

# Current Implementation

The project currently uses MockEDR to simulate an Endpoint Detection and Response system.

MockEDR sends webhook requests containing:

- Security event data
- X-API-Key header

The backend compares the received API key with the configured secret.

If both values match, the request is authenticated.

---

# Future Improvements

In enterprise environments, API keys may be replaced with provider-specific authentication mechanisms.

Examples include:

- CrowdStrike Falcon webhook signature verification
- Microsoft Defender signature validation
- HMAC-based request signing
- Certificate-based authentication

These methods provide stronger security and ensure that webhook requests originate from legitimate providers.

---

# Expected Responses

| Status Code | Description |
|-------------|-------------|
| 200 OK | Webhook authenticated successfully |
| 401 Unauthorized | Invalid or missing API key |

---

# Summary

Webhook authentication protects the backend by ensuring that only trusted EDR providers can submit security alerts.

The current implementation uses an X-API-Key header with MockEDR.

Future versions can replace this mechanism with enterprise-grade authentication provided by real EDR vendors such as CrowdStrike and Microsoft Defender.