# API Endpoint Map (v1)

## Authentication
- `POST /api/v1/auth/token`

## Branches
- `POST /api/v1/branches`
- `GET /api/v1/branches`

## Services
- `POST /api/v1/services`
- `GET /api/v1/services?branch_code=`

## Applications and Workflow
- `POST /api/v1/applications`
- `PATCH /api/v1/applications/{id}/status`

## Citizen Charter
- `POST /api/v1/citizen-charter`
- `GET /api/v1/citizen-charter?branch_id=`

## Announcements
- `POST /api/v1/announcements`
- `GET /api/v1/announcements?branch_code=`

## Ledger
- `GET /api/v1/ledger?branch_code=`

## Reports
- `GET /api/v1/reports/dashboard`

## Branding
- `GET /api/v1/branding/theme` (locked official palette and typography)
- `POST /api/v1/branding/branches/{branch_id}/logo` (admin-only logo validation and upload)

## AI
- `POST /api/v1/chatbot/ask`
