# Identity Provider Integration

## Objective

The Identity Provider module integrates the ARC-IR Orchestrator with an Identity Provider (IdP) to automate identity containment during security incidents. When an Endpoint Detection and Response (EDR) alert is validated, the module automatically suspends compromised user accounts and revokes their active sessions to reduce the risk of unauthorized access.

The current implementation uses a **Mock Identity Provider** to simulate enterprise Identity Provider operations. This allows developers to build, test, and validate the containment workflow without requiring access to real identity infrastructure.

The architecture is intentionally designed to separate business logic from provider implementation, making it easy to replace the mock provider with enterprise Identity Providers in the future.

---

# Architecture

The Identity Provider module is part of the automated containment workflow inside the ARC-IR Orchestrator.

```text
Webhook
   │
   ▼
Alert Parser
   │
   ▼
Containment Service
   │
   ▼
Identity Service
   │
   ▼
Mock Identity Provider
   ├── Disable User Account
   └── Revoke Active Sessions
```

## Architecture Explanation

- **Webhook** receives security alerts from the EDR platform.
- **Alert Parser** validates and extracts the username and incident details.
- **Containment Service** decides whether identity containment is required.
- **Identity Service** contains the business logic and coordinates identity operations.
- **Mock Identity Provider** simulates enterprise Identity Provider APIs and returns standardized responses.

This layered architecture separates orchestration logic from provider-specific implementation, improving maintainability and scalability.

---

# Identity Containment Workflow

The identity containment workflow follows these steps:

### Step 1 – Receive Security Alert

The Webhook receives an incoming EDR alert.

### Step 2 – Parse Alert

The Alert Parser validates the payload and extracts the affected username.

### Step 3 – Containment Decision

The Containment Service determines whether the user account should be suspended based on the validated alert.

### Step 4 – Identity Service

The Identity Service receives the containment request, validates it, and coordinates the required identity operations.

### Step 5 – Suspend User

The Identity Service calls the Mock Identity Provider to suspend the compromised user account.

### Step 6 – Revoke Sessions

If account suspension succeeds, all active user sessions are revoked.

### Step 7 – Return Response

A standardized response is returned to the Containment Service and ultimately back to the API consumer.

---

# Component Responsibilities

## Identity Service

The Identity Service acts as the orchestration layer between the Incident Response Orchestrator and the Identity Provider.

### Responsibilities

- Handles all business logic.
- Validates containment requests.
- Coordinates the identity containment workflow.
- Calls the configured Identity Provider.
- Processes provider responses.
- Handles exceptions.
- Returns standardized responses.
- Acts as the future integration point for Microsoft Entra ID, Active Directory, Okta, and other enterprise Identity Providers.

### Why Business Logic Exists Inside IdentityService

IdentityService determines **what** action should be performed based on the security incident.

Examples include:

- Whether the account should be suspended.
- Whether user sessions should be revoked.
- How failures should be handled.
- How responses should be formatted.

Keeping business logic inside IdentityService ensures that provider implementations remain simple and interchangeable.

---

## Mock Identity Provider

The Mock Identity Provider simulates an enterprise Identity Provider.

### Responsibilities

- Simulates enterprise Identity Provider APIs.
- Performs mock identity operations.
- Simulates account suspension.
- Simulates session revocation.
- Returns standardized provider responses.
- Supports testing without external dependencies.

### Why It Contains No Business Logic

The Mock Identity Provider only performs the requested simulated operation.

It does **not**:

- Decide whether containment should occur.
- Validate incidents.
- Process security alerts.
- Make business decisions.

Its sole purpose is to imitate the behavior of a real Identity Provider.

---

# API Contract

## IdentityService

### Methods

| Method | Description |
|---------|-------------|
| suspend_user(username: str) | Suspends a compromised user account. |
| revoke_user_sessions(username: str) | Revokes all active user sessions. |

---

## MockIdentityProvider

### Methods

| Method | Description |
|---------|-------------|
| disable_user(username: str) | Simulates disabling a user account. |
| revoke_sessions(username: str) | Simulates revoking all active sessions. |

---

# Standard Response Format

Every identity operation returns a standardized dictionary.

```json
{
    "status": "success",
    "action": "disable_user",
    "username": "john.smith",
    "message": "User account disabled."
}
```

## Response Fields

| Field | Description |
|---------|-------------|
| status | Indicates whether the operation succeeded or failed. |
| action | Identity operation that was executed. |
| username | Username of the affected account. |
| message | Human-readable description of the operation result. |

---

## Example Success Response

```json
{
    "status": "success",
    "action": "disable_user",
    "username": "john.smith",
    "message": "User account disabled."
}
```

---

## Example Failure Response

```json
{
    "status": "failed",
    "action": "disable_user",
    "username": "john.smith",
    "message": "User not found."
}
```

---

# Complete Workflow

1. The Webhook receives an EDR alert.
2. The Alert Parser validates the alert and extracts the username.
3. The Containment Service decides that identity containment is required.
4. IdentityService validates the request.
5. IdentityService calls MockIdentityProvider.
6. MockIdentityProvider simulates disabling the user account.
7. If successful, active sessions are revoked.
8. A standardized response is generated.
9. The response is returned to the Containment Service.
10. The API returns the final containment result.

---

# Future Enterprise Integration

The current implementation uses a Mock Identity Provider for development and testing.

In production, it can easily be replaced with enterprise Identity Providers such as:

- Microsoft Entra ID (Azure AD)
- Active Directory
- Okta
- AWS IAM Identity Center
- Google Workspace
- Ping Identity
- LDAP
- OAuth 2.0 / OpenID Connect compatible providers

Because all business logic resides inside IdentityService, replacing the provider requires minimal code changes.

Possible future enhancements include:

- Multi-Factor Authentication (MFA) management
- Password reset automation
- Conditional Access integration
- Identity Risk Protection
- Role-Based Access Control (RBAC)
- Audit logging
- SCIM provisioning
- Single Sign-On (SSO) integration

---

# Notes for Developers

- Keep all business logic inside IdentityService.
- Keep MockIdentityProvider lightweight and focused only on provider simulation.
- Do not implement validation or containment decisions inside the provider.
- Maintain standardized response formats across all identity operations.
- Follow separation of concerns to simplify maintenance and future provider integration.
- Update this documentation whenever new identity operations or enterprise providers are added.

---

# Summary

The Identity Provider module enables automated identity containment within the ARC-IR Orchestrator by suspending compromised user accounts and revoking active sessions after validated security alerts. The separation of business logic in IdentityService and provider-specific implementation in MockIdentityProvider creates a modular, maintainable, and scalable architecture that can easily support future enterprise Identity Providers without significant changes to the application.