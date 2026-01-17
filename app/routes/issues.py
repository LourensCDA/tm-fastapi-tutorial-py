from fastapi import APIRouter, HTTPException, status
from app.schemas import Issue, IssueStatus, IssuePriority, IssuePUT
from app.storage import load_data, save_data

# prefix could also be /api/v1/issues depending on your versioning strategy
router = APIRouter(prefix="/issues", tags=["issues"])


@router.get("/", response_model=list[Issue])
async def list_issues():
    """
    Endpoint to list all issues
    """
    issues = load_data()
    return issues


@router.post("/", response_model=Issue, status_code=status.HTTP_201_CREATED)
async def create_issue(payLoad: Issue):
    """
    Endpoint to create a new issue
    """
    try:
        issues = load_data()
        issues.append(payLoad.model_dump())
        save_data(issues)
    except Exception as e:
        print(e)
    return payLoad


@router.get("/{issue_id}", response_model=Issue)
async def get_issue(issue_id: str):
    """
    Endpoint to get a specific issue by ID
    """
    issues = load_data()
    for issue in issues:
        if issue["id"] == issue_id:
            return issue
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")


@router.put("/{issue_id}", response_model=Issue)
async def update_issue(issue_id: str, payLoad: IssuePUT):
    """
    Endpoint to update a specific issue by ID
    """
    issues = load_data()
    for index, issue in enumerate(issues):
        if issue["id"] == issue_id:
            issues[index] = payLoad.model_dump()
            issues[index]["id"] = issue_id  # Preserve the original ID
            save_data(issues)
            return issues[index]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")


@router.delete("/{issue_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_issue(issue_id: str):
    """
    Endpoint to delete a specific issue by ID
    """
    issues = load_data()
    for index, issue in enumerate(issues):
        if issue["id"] == issue_id:
            issues.pop(index)
            save_data(issues)
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")
