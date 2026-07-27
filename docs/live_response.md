# Live Response Evidence Collection

## Objective

The Live Response Evidence Collection module enables the ARC-IR Orchestrator to remotely collect forensic evidence from a compromised endpoint after containment has been completed. The module provides a standardized interface for executing live response actions while keeping the Incident Response Orchestrator independent of any specific Enterprise Endpoint Detection and Response (EDR) platform.

The current implementation uses a **MockLiveResponseClient** to simulate Enterprise EDR live response capabilities during development and testing. This allows developers to validate workflows without requiring access to production security tools.

---

# Purpose of Live Response

After an endpoint has been contained, investigators need forensic evidence to understand what happened during the security incident. Live Response allows remote evidence collection without requiring physical access to the affected device.

Typical evidence includes:

- Memory captures
- Running processes
- System information
- Event logs
- Network connections
- Browser artifacts
- File system metadata
- Registry information
- KAPE forensic collections

This information helps security analysts investigate attacks and determine the scope of an incident.

---

# Why Forensic Evidence Collection Is Important

Collecting forensic evidence immediately after containment provides several benefits:

- Preserves important evidence before it changes.
- Helps identify malware and attacker activity.
- Supports incident investigation and root cause analysis.
- Assists with compliance and audit requirements.
- Enables reconstruction of the attack timeline.
- Improves future detection and response capabilities.

---

# Module Architecture

The Live Response module is integrated into the Incident Response Orchestrator.

```text
Incident Alert
      │
      ▼
IncidentOrchestrator
      │
      ▼
EvidenceCollectionService
      │
      ▼
MockLiveResponseClient
      ├── Execute KAPE
      └── Capture Memory
```

## Architecture Explanation

### IncidentOrchestrator

Coordinates the overall incident response workflow and determines when evidence collection should begin.

### EvidenceCollectionService

Contains business logic for forensic evidence collection and coordinates communication with the Live Response client.

### MockLiveResponseClient

Simulates Enterprise EDR Live Response capabilities and executes mock forensic commands.

---

# Workflow

The Live Response workflow consists of the following steps:

### Step 1 – Incident Alert

The Incident Response Orchestrator receives a validated security incident.

### Step 2 – Containment

The endpoint is isolated using the containment workflow.

### Step 3 – Evidence Collection Request

The IncidentOrchestrator requests forensic evidence collection.

### Step 4 – EvidenceCollectionService

The service validates the request and determines which evidence should be collected.

### Step 5 – MockLiveResponseClient

The client simulates execution of remote forensic commands such as:

- Execute KAPE
- Capture Memory

### Step 6 – Response Generation

The simulated client returns a standardized response.

### Step 7 – Final Result

EvidenceCollectionService processes the response and returns the final result to the IncidentOrchestrator.

---

# Component Responsibilities

## EvidenceCollectionService

EvidenceCollectionService is responsible for coordinating forensic evidence collection.

### Responsibilities

- Coordinates forensic evidence collection.
- Contains business logic.
- Validates requests.
- Determines required evidence collection actions.
- Calls the MockLiveResponseClient.
- Processes responses.
- Handles errors.
- Returns standardized responses.

### Why Business Logic Exists Inside EvidenceCollectionService

EvidenceCollectionService determines **what** forensic evidence should be collected and **when** it should be collected.

Keeping business logic inside the service allows the underlying Live Response client to remain simple and makes it easier to replace the mock implementation with a real Enterprise EDR integration.

---

## MockLiveResponseClient

MockLiveResponseClient simulates Enterprise EDR Live Response functionality.

### Responsibilities

- Simulates Enterprise EDR Live Response.
- Executes remote forensic commands.
- Simulates KAPE execution.
- Simulates memory capture.
- Returns standardized responses.
- Contains **no business logic**.

### Why It Contains No Business Logic

MockLiveResponseClient only simulates provider behavior.

It does not:

- Make containment decisions.
- Validate security incidents.
- Decide which evidence should be collected.
- Apply business rules.

Its responsibility is limited to simulating Enterprise EDR operations.

---

# API Contract

## EvidenceCollectionService

| Method | Description |
|---------|-------------|
| execute_kape(hostname: str) | Initiates simulated KAPE evidence collection. |
| capture_memory(hostname: str) | Initiates simulated memory acquisition. |

---

## MockLiveResponseClient

| Method | Description |
|---------|-------------|
| execute_kape(hostname: str) | Simulates execution of KAPE. |
| capture_memory(hostname: str) | Simulates memory capture. |

---

# Standard Response Format

Every Live Response operation returns a standardized dictionary.

```json
{
    "status": "success",
    "action": "capture_memory",
    "hostname": "DESKTOP-001",
    "message": "Memory capture completed successfully."
}
```

## Response Fields

| Field | Description |
|---------|-------------|
| status | Indicates whether the operation succeeded or failed. |
| action | The forensic action that was executed. |
| hostname | The endpoint hostname. |
| message | Human-readable result of the operation. |

---

## Example Success Response

```json
{
    "status": "success",
    "action": "execute_kape",
    "hostname": "DESKTOP-001",
    "message": "KAPE evidence collection completed successfully."
}
```

---

## Example Failure Response

```json
{
    "status": "failed",
    "action": "capture_memory",
    "hostname": "DESKTOP-001",
    "message": "Endpoint is offline."
}
```

---

# Future Integration

The current implementation uses a MockLiveResponseClient for development and testing.

Future project phases will replace the mock implementation with real Enterprise EDR integrations, including:

- Microsoft Defender for Endpoint
- CrowdStrike Falcon
- SentinelOne
- VMware Carbon Black

Additional enhancements may include:

- Automated forensic artifact uploads to secure cloud storage.
- Secure evidence encryption.
- Evidence integrity verification using cryptographic hashes.
- Chain of custody tracking.
- Automated investigation reports.
- Integration with enterprise case management systems.

---

# Developer Notes

When working with this module:

- Keep business logic inside EvidenceCollectionService.
- Keep MockLiveResponseClient lightweight.
- Do not implement business rules inside the mock client.
- Maintain standardized response formats.
- Follow separation of concerns.
- Update this documentation whenever new forensic capabilities are added.

---

# Summary

The Live Response Evidence Collection module provides a structured and extensible framework for remotely collecting forensic evidence after endpoint containment. By separating business logic from provider-specific implementation, the ARC-IR Orchestrator can easily integrate with Enterprise EDR platforms in future project phases while maintaining a clean and maintainable architecture.