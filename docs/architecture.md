# MSWDO Laguna OOP Architecture

## Layered OOP Design
- **Domain layer** (`core/domain`): pure business objects (`User`, `Role`, `Branch`, `Service`, `Application`, `WorkflowStep`, `Announcement`, `LedgerEntry`, `CitizenCharter`, `Form`, `DocumentUpload`).
- **Service layer** (`core/services`): encapsulated business rules (`ApplicationService`, `WorkflowService`, `LedgerService`, `AnnouncementService`, `CitizenCharterService`, `ChatbotService`, `ThemeService`).
- **Repository layer** (`core/repositories`): isolated ORM queries, one repository per entity group.
- **Controller/API layer** (`app/api`): HTTP transport only; no SQL and minimal/no business rules.
- **Security policy layer** (`security/branding_policy.py`): DSWD branding compliance checks and logo validation rules.

## Enforced OOP Principles
- **Encapsulation**: transition/disbursement logic is inside service classes.
- **Inheritance**: shared repository base class and workflow strategy hierarchy.
- **Polymorphism**: service-specific workflow strategies (`DefaultWorkflow`, `AICSWorkflow`) behind common interface.
- **Abstraction**: workflow behavior exposed through abstract `WorkflowStrategy`.

## DSWD Branding Compliance Controls
- Official colors are locked through centralized settings and theme service (`#2e3192`, `#ee1c25`, `#fef200`).
- Typography is restricted to Arial for headings, forms, and table content.
- Logo uploads are admin-only with file type, size, and aspect-ratio validation.
- UI is text-first and table/form-driven, using neutral supporting colors for formal government presentation.

## Compliance/Security Alignment
- JWT auth + role-based permissions.
- Auditable models include `created_at`, `updated_at`, `created_by`, `branch_id`.
- Relational schema designed for 3NF-ready normalization, FK-driven references, and explicit audit logs.
- AI assistant is limited to structured information guidance and workflow/help responses.
