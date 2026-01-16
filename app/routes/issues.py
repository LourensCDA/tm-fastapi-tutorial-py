from fastapi import APIRouter

# prefix could also be /api/v1/issues depending on your versioning strategy
router = APIRouter(prefix="/issues", tags=["issues"])


@router.get("/")
async def list_issues():
    """
    Endpoint to list all issues
    """
    return []
