from fastapi import APIRouter

router = APIRouter(prefix="/features", tags=["features"])


@router.get("/")
def get_features() -> dict[str, str]:
    """
    Get features endpoint.

    Parameters:
        None

    Returns:
        dict[str, str]: Success message indicating the endpoint is operational.
    """
    return {"message": "Features endpoint is operational"}
