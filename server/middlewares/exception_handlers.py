from fastapi import Request
from fastapi.responses import JSONResponse
from logger import logger


async def exception_handler(request: Request, exc: Exception):
    logger.exception("Unhandled exception occurred")

    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error"}
    )