# AEYA

This repository contains the n8n workflows and helper scripts used in the
"Tunes Do Travel" AI pre-production pipeline. The project automates script
generation, quality checks and video creation for the channel, and it includes a
finance-related workflow for managing upgrades and debt paydown.

## Repository layout

```
.
├── convert_connections.py  # convert legacy connection objects
├── fix_connections.py      # normalize n8n connection structures
├── n8n-workflows/          # exported workflow JSON files
│   ├── content_orchestration_core.json
│   ├── ensemble_review_subflow.json
│   ├── trigger-financial-upgrades-and-debt-paydown-FINAL.json
│   └── sheets/             # example spreadsheets referenced by workflows
│       └── *.csv
└── README.md
```

### Helper scripts

The Python utilities deal with the `connections` property of exported n8n
workflows. Older exports or manual edits can produce inconsistent formats. The
scripts rewrite the JSON so that every node has an object of the form
`{"main": [[ {"node": "dest", "type": "main", "index": 0}, ... ]]}`.

* **`convert_connections.py`** – handles simple cases where the connections are a
  dictionary mapping node names to their `main` arrays. When it encounters a
  nested list it flattens it and rewrites the file in place.
* **`fix_connections.py`** – a more robust normalizer. It accepts connection
  lists, single objects or partially formed dictionaries and converts them to the
  structure n8n expects.

Run either script with one or more workflow files as arguments:

```bash
python fix_connections.py path/to/workflow.json
```

### n8n workflows

The `n8n-workflows` directory contains JSON definitions that can be imported
into an n8n instance.

* **`content_orchestration_core.json`** – main workflow that orchestrates
  pre‑production. It accepts a chat input, generates a script, runs the
  `ensemble-review-subflow` for quality control, emails previews for approval and
  optionally renders videos using WaveSpeed AI. Episode status, LLM review logs
  and notifications are appended to Google Sheets.
* **`ensemble_review_subflow.json`** – called by the core workflow. It queries
  three Hugging Face models (Mistral, Falcon and FLAN‑T5) and aggregates their
  responses via a code node. Confidence scores are normalized and the overall
  risk level drops to *MEDIUM* when the average is below `0.6`.
* **`trigger-financial-upgrades-and-debt-paydown-FINAL.json`** – scheduled
  financial assistant. It reads payment and expense sheets, calculates surplus
  funds and determines whether to trigger QuickBooks, Lindy or Devin automation
  based on the available balance. Notifications and plan updates are written back
  to Google Sheets.
* **`sheets/*.csv`** – placeholder spreadsheets referenced by the workflows.
  These provide the column structure for the Episodes log, Expenses log and other
  tracking files.

### Usage

Import the JSON files into your n8n instance via the "Import from file" option.
If the workflows fail to load due to malformed connections, run
`fix_connections.py` on the JSON file and try again. The example CSV files can be
uploaded to Google Sheets and connected through the appropriate credentials.

The workflows rely on environment variables such as `HUGGINGFACE_API_KEY` for
calling the hosted models. Ensure these variables are configured within n8n
before executing the flows.

## License

No license information is included in this repository. All rights reserved by
the original authors.
