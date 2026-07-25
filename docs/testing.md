# AlertParser Unit Tests

## Overview

This directory contains unit tests for the `AlertParser` service.

The purpose of these tests is to verify that the parser correctly converts a `RawAlert` into a `ParsedAlert` without modifying the parser implementation.

## Test File

```
tests/test_alert_parser.py
```

## Test Cases

The following test cases are included:

1. Manual alert is parsed successfully.
2. Critical severity remains `critical`.
3. Hostname is parsed correctly.
4. Username is parsed correctly.
5. Process hash is parsed correctly.

## Test Data

The tests use a sample `RawAlert` object containing:

- Provider
- Alert ID
- Severity
- Timestamp
- Hostname
- IP Address
- Device ID
- Username
- Process Name
- Process Hash
- Title
- Description

## Running the Tests

Activate the virtual environment:

```bash
venv\Scripts\activate
```

Install dependencies (if required):

```bash
python -m pip install -r requirements.txt
```

Run the test suite:

```bash
python -m pytest
```

or

```bash
pytest
```

## Expected Result

All AlertParser unit tests should pass successfully.

## Notes

- The parser implementation was not modified.
- The tests follow the current `RawAlert` schema.
- The parser is invoked using:

```python
parsed = parser.parse(
    alert_data=sample_raw_alert.model_dump(),
    provider=sample_raw_alert.provider,
)
```

- Assertions validate the parsed provider, severity, hostname, username, and process hash.