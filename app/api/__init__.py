from fastapi import APIRouter

from app.api import announcements, applications, auth, branches, branding, chatbot, citizen_charter, ledger, reports, services

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(auth.router)
api_router.include_router(branches.router)
api_router.include_router(services.router)
api_router.include_router(applications.router)
api_router.include_router(announcements.router)
api_router.include_router(ledger.router)
api_router.include_router(citizen_charter.router)
api_router.include_router(reports.router)
api_router.include_router(branding.router)
api_router.include_router(chatbot.router)
