# Signup Form API

A simple FastAPI application that provides a user signup endpoint with comprehensive input validation.

## Features

- **User Signup Endpoint**: POST `/signup` for user registration
- **Input Validation**: 
  - Username: Must be alphanumeric and 3-50 characters long
  - Email: Must be a valid email format
  - Password: Must be 8-100 characters with at least one uppercase letter, lowercase letter, and digit
- **Error Handling**: Proper HTTP status codes and detailed error messages
- **Documentation**: Auto-generated API documentation with FastAPI

## API Endpoints

- `GET /` - Root endpoint with API information
- `GET /health` - Health check endpoint
- `POST /signup` - User signup endpoint

## Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd testthis
   ```

2. **Create and activate virtual environment** (if not already done):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the API

### Option 1: Using Python directly
```bash
python app.py
```

### Option 2: Using uvicorn command
```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access:
- **Interactive API documentation (Swagger UI)**: `http://localhost:8000/docs`
- **Alternative API documentation (ReDoc)**: `http://localhost:8000/redoc`

## Testing the API

### Example POST request to `/signup`:

```bash
curl -X POST "http://localhost:8000/signup" \
     -H "Content-Type: application/json" \
     -d '{
       "username": "johndoe123",
       "email": "john@example.com",
       "password": "SecurePass123"
     }'
```

### Example responses:

**Success (201 Created):**
```json
{
  "message": "User successfully registered",
  "username": "johndoe123",
  "email": "john@example.com"
}
```

**Validation Error (422 Unprocessable Entity):**
```json
{
  "error": "Validation failed",
  "details": "username: Username must contain only alphanumeric characters; password: Password must be at least 8 characters long"
}
```

**Conflict Error (409 Conflict):**
```json
{
  "detail": "Username already exists"
}
```

## Input Validation Rules

### Username
- Must contain only alphanumeric characters (a-z, A-Z, 0-9)
- Must be between 3 and 50 characters long
- Cannot be empty

### Email
- Must be a valid email format (validated using pydantic EmailStr)
- Cannot be empty

### Password
- Must be between 8 and 100 characters long
- Must contain at least one uppercase letter (A-Z)
- Must contain at least one lowercase letter (a-z)
- Must contain at least one digit (0-9)
- Cannot be empty

## Project Structure

```
testthis/
├── app.py              # Main FastAPI application
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── trift/
│   └── python.py      # Original placeholder file
└── venv/              # Virtual environment
```

## Error Handling

The API includes comprehensive error handling:
- **400 Bad Request**: Invalid input format
- **409 Conflict**: Username already exists
- **422 Unprocessable Entity**: Validation errors
- **500 Internal Server Error**: Unexpected server errors

All errors include descriptive messages to help clients understand what went wrong.