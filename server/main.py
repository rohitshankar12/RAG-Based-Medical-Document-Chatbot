from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middlewares.exception_handlers import exception_handler
from routes.upload_pdf import router as upload_pdf_router
from routes.asked_question import router as asked_question_router


app = FastAPI(title="Medical App", description="Medical App API", version="1.0.0")

# CORS middleware
app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

# Global exception handler
app.add_exception_handler(Exception, exception_handler)

# Routers
app.include_router(upload_pdf_router)
app.include_router(asked_question_router)