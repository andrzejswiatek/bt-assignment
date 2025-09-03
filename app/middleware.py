from fastapi import FastAPI, Request
from app.container import SessionLocal, request_context

def setup_middlewares(app: FastAPI):
    @app.middleware("http")
    async def set_request_context_var(request: Request, call_next):        
        token = request_context.set(id(request))    
        try:
            response = await call_next(request)
        finally:        
            SessionLocal.remove()
            request_context.reset(token)
            
        return response