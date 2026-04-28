# Textile Cost Tracker

Mini Odoo module to manage textile clients and projects, track material and labor costs, and review totals with simple graph/pivot views. Built as a beginner-friendly showcase module.

## Features

- Manage textile clients
- Manage textile projects
- Compute total cost (materials + labor)
- Track project status
- Graph and pivot analysis views

## Models

- `textile.client`
  - `name` (required)
  - `email`

- `textile.project`
  - `name` (required)
  - `client_id`
  - `material_cost`
  - `labor_cost`
  - `total_cost` (computed)
  - `state` (draft/in_progress/done)

## Module Structure

```
cost_tracker/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── textile_client.py
│   └── textile_project.py
├── security/
│   └── ir.model.access.csv
└── views/
    └── textile_project_views.xml
```

## Install

1. Ensure the module folder is in your `addons_path`.
2. Update apps list.
3. Install **Textile Cost Tracker**.

CLI upgrade:

```bash
./odoo-bin -d <db_name> -u cost_tracker
```

## Usage

- Open the **Textile Cost Tracker** menu.
- Create clients (from the client dropdown in projects or via model data).
- Create projects and enter material/labor costs.
- Use graph/pivot view switchers to analyze costs.

## Notes for Odoo 17

- List views use `<list>` instead of `<tree>`.
- `states` attributes on buttons are removed; use separate logic if needed.
