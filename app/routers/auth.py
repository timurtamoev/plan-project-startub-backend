from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/")
def get_auth() -> dict[str, str]:
    """
    Get auth endpoint.

    Parameters:
        None

    Returns:
        dict[str, str]: Success message indicating the endpoint is operational.
    """
    return {"message": "Auth endpoint is operational"}
