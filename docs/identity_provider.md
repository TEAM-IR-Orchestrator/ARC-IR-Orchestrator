# Identity Provider Integration

## Objective

Integrate the ARC-IR Orchestrator with a mock Identity Provider to automatically suspend compromised user accounts and revoke active session tokens after an EDR alert has been validated.

---

# Architecture

Webhook

↓

Alert Parser

↓

Containment Service

↓

Identity Service

↓

Mock Identity Provider

    ├── Disable User Account

    └── Revoke Active Sessions

---

# Component Responsibilities

## Identity Service

Responsibilities:

- Handles business logic.
- Coordinates identity containment workflow.
- Calls the Identity Provider.
- Returns standardized responses.
- Future integration point for Azure AD / Microsoft Entra ID.

---

## Mock Identity Provider

Responsibilities:

- Simulates enterprise Identity Provider APIs.
- Performs mock identity operations.
- Does not contain business logic.
- Returns standardized provider responses.

---

# API Contract

## IdentityService

Methods:

- suspend_user(username: str)
- revoke_user_sessions(username: str)

---

## MockIdentityProvider

Methods:

- disable_user(username: str)
- revoke_sessions(username: str)

---

# Standard Response Format

Every identity operation should return a dictionary using the following structure:

{
    "status": "...",
    "action": "...",
    "username": "...",
    "message": "..."
}

---

Example Success

{
    "status": "success",
    "action": "disable_user",
    "username": "john.smith",
    "message": "User account disabled."
}

---

Example Failure

{
    "status": "failed",
    "action": "disable_user",
    "username": "john.smith",
    "message": "User not found."
}

---

# Workflow

1. Receive validated username.
2. Suspend compromised user account.
3. If suspension succeeds, revoke active sessions.
4. Return final response.

---

# Future Integration

The mock implementation can later be replaced with any of these:

- Microsoft Entra ID (Azure AD)
- Active Directory
- Okta
- AWS IAM Identity Center

without changing business logic inside IdentityService.