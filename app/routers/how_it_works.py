from fastapi import APIRouter

router = APIRouter(prefix="/how-it-works", tags=["how-it-works"])


@router.get("/")
def get_how_it_works() -> dict[str, str]:
    """
    Get how it works endpoint.

    Parameters:
        None

    Returns:
        dict[str, str]: Success message indicating the endpoint is operational.
    """
    return {"message": "How it works endpoint is operational"}
