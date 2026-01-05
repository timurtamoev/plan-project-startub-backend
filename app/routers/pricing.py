from fastapi import APIRouter

router = APIRouter(prefix="/pricing", tags=["pricing"])


@router.get("/")
def get_pricing() -> dict[str, str]:
    """
    Get pricing endpoint.

    Parameters:
        None

    Returns:
        dict[str, str]: Success message indicating the endpoint is operational.
    """
    return {"message": "Pricing endpoint is operational"}
