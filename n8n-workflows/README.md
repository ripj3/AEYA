# n8n Workflows

This directory contains automation workflows exported from n8n. Each JSON file defines a set of nodes and connections used by the AEYA project.

Sample Google Sheets templates used by these workflows are available in the [`sheets`](sheets) folder.

## Workflows

### `content_orchestration_core.json`
This workflow manages the core content creation pipeline:
- Initiates a chat with AEYA.
- Generates a narrative and runs an ensemble quality check via the `ensemble-review-subflow` workflow *(not included here)*.
- Sends review emails and waits for approvals.
- Based on the chosen video mode, triggers rendering with Lumia (long-form) or Pika (short-form).
- Logs results to multiple Google Sheets including `Episodes`, `Video_Log`, `LLM_Review_Log` and `Notification_Log`.

### `trigger-financial-upgrades-and-debt-paydown-FINAL.json`
This workflow monitors financial spreadsheets to determine surplus funds and next actions:
- Loads payments, expenses and the system financial plan from Google Sheets.
- Calculates surplus and decides whether to pay down VISA, trigger QuickBooks, or schedule contributions to other tools.
- Updates the financial plan and logs notifications to `Notification_Log`.

Both workflows append important events to the `Notification_Log` sheet so they can interoperate when monitoring system-wide actions.

