# MSWDO Laguna Dynamic Platform (FastAPI + OOP)

## Government-Formal Scope
- Dynamic branch-aware MSWDO public and internal services
- Citizen's Charter-aligned workflows and tracking
- Shared ledger and auditable records
- Text-first UI (tables, forms, and headings only)
- DSWD branding-locked theme and admin-controlled logo validation

## OOP Module Structure
- `core/domain` - business entities (no DB logic)
- `core/services` - business rules and workflow logic
- `core/repositories` - data access and ORM queries
- `core/workflows` - workflow abstractions and strategies
- `security` - policy guards (branding and compliance checks)
- `app/api` - HTTP controllers only

## Run locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Documentation
- `docs/architecture.md`
- `docs/api-endpoints.md`
- `docs/mysql-schema.sql`
