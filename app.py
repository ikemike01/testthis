"""
FastAPI Signup Form API

This module provides a simple API for user signup with validation.
The API includes endpoints for user registration with proper input validation
and error handling.
"""

from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr, field_validator
import re
from typing import Optional

# Initialize FastAPI application
app = FastAPI(
    title="Signup Form API",
    description="A simple API for user signup with validation",
    version="1.0.0"
)

# Pydantic model for signup request validation
class SignupRequest(BaseModel):
    """
    Data model for user signup request.
    
    Attributes:
        username: Alphanumeric username (required)
        email: Valid email address (required)
        password: Password with minimum security requirements (required)
    """
    username: str
    email: EmailStr
    password: str
    
    @field_validator('username')
    @classmethod
    def validate_username(cls, v):
        """
        Validate username to ensure it's alphanumeric.
        
        Args:
            v: The username value to validate
            
        Returns:
            str: The validated username
            
        Raises:
            ValueError: If username is not alphanumeric
        """
        if not v:
            raise ValueError('Username cannot be empty')
        if not re.match(r'^[a-zA-Z0-9]+$', v):
            raise ValueError('Username must contain only alphanumeric characters')
        if len(v) < 3:
            raise ValueError('Username must be at least 3 characters long')
        if len(v) > 50:
            raise ValueError('Username must be no more than 50 characters long')
        return v
    
    @field_validator('password')
    @classmethod
    def validate_password(cls, v):
        """
        Validate password to ensure it meets basic security requirements.
        
        Args:
            v: The password value to validate
            
        Returns:
            str: The validated password
            
        Raises:
            ValueError: If password doesn't meet requirements
        """
        if not v:
            raise ValueError('Password cannot be empty')
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if len(v) > 100:
            raise ValueError('Password must be no more than 100 characters long')
        
        # Check for at least one uppercase letter
        if not re.search(r'[A-Z]', v):
            raise ValueError('Password must contain at least one uppercase letter')
        
        # Check for at least one lowercase letter
        if not re.search(r'[a-z]', v):
            raise ValueError('Password must contain at least one lowercase letter')
        
        # Check for at least one digit
        if not re.search(r'\d', v):
            raise ValueError('Password must contain at least one digit')
        
        return v

# Pydantic model for successful signup response
class SignupResponse(BaseModel):
    """
    Data model for successful signup response.
    
    Attributes:
        message: Success message
        username: The registered username
        email: The registered email
    """
    message: str
    username: str
    email: str

# Pydantic model for error response
class ErrorResponse(BaseModel):
    """
    Data model for error response.
    
    Attributes:
        error: Error message
        details: Optional detailed error information
    """
    error: str
    details: Optional[str] = None

# Root endpoint
@app.get("/")
async def root():
    """
    Root endpoint that provides basic API information.
    
    Returns:
        dict: Basic API information
    """
    return {
        "message": "Welcome to the Signup Form API",
        "version": "1.0.0",
        "endpoints": {
            "signup": "/signup (POST)",
            "health": "/health (GET)"
        }
    }

# Health check endpoint
@app.get("/health")
async def health_check():
    """
    Health check endpoint to verify API is running.
    
    Returns:
        dict: Health status information
    """
    return {"status": "healthy", "message": "API is running"}

# Signup endpoint
@app.post("/signup", response_model=SignupResponse)
async def signup(request: SignupRequest):
    """
    User signup endpoint with validation.
    
    This endpoint accepts user signup details and validates them according to
    the following rules:
    - Username: Must be alphanumeric, 3-50 characters
    - Email: Must be a valid email format
    - Password: Must be 8-100 characters with at least one uppercase letter,
               one lowercase letter, and one digit
    
    Args:
        request: SignupRequest object containing user details
        
    Returns:
        SignupResponse: Success response with user details
        
    Raises:
        HTTPException: 400 for validation errors, 409 for conflicts, 500 for server errors
    """
    try:
        # In a real application, you would:
        # 1. Check if username/email already exists in database
        # 2. Hash the password before storing
        # 3. Save user to database
        # 4. Send confirmation email
        
        # For this example, we'll simulate checking for existing users
        # This would typically be a database query
        existing_usernames = ["admin", "test", "user123"]  # Simulated existing users
        
        if request.username.lower() in existing_usernames:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Username already exists"
            )
        
        # Simulate successful registration
        return SignupResponse(
            message="User successfully registered",
            username=request.username,
            email=request.email
        )
        
    except HTTPException:
        # Re-raise HTTPExceptions (like 409 Conflict)
        raise
    except Exception as e:
        # Handle any unexpected errors
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred during registration"
        )

# Custom exception handler for validation errors
@app.exception_handler(422)
async def validation_exception_handler(request, exc):
    """
    Custom exception handler for validation errors.
    
    Args:
        request: The incoming request
        exc: The validation exception
        
    Returns:
        JSONResponse: Formatted error response
    """
    errors = []
    for error in exc.detail:
        field = error.get('loc', ['unknown'])[-1]  # Get the field name
        message = error.get('msg', 'Invalid input')
        errors.append(f"{field}: {message}")
    
    return JSONResponse(
        status_code=422,
        content={
            "error": "Validation failed",
            "details": "; ".join(errors)
        }
    )

if __name__ == "__main__":
    import uvicorn
    # Run the application
    uvicorn.run(app, host="0.0.0.0", port=8000)