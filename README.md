# Event Reminder API Documentation

## Setup and Installation Instructions

### Prerequisites
- Python 3.8 or higher
- Django 3.2 or higher
- Django REST Framework 3.12 or higher
- A database (e.g., SQLite, PostgreSQL, etc.)

### Installation Steps

### Apply Migrations

```
   python manage.py makemigrations
   python manage.py migrate
```

### Run the Development Server

```
   python manage.py runserver
```

### API Endpoint Documentation

#### Event Management Endpoints

#### 1. Create a New Event

Endpoint: POST /api/events/
Request Body:

```bash
{
  "title": "Local Football Match",
  "description": "Cheer for your favorite local team as they take on their rivals.",
  "date": "2024-11-20",
  "time": "16:30:00",
  "category": "Sports"
}
```

#### 2. Retrieve a Specific Event
Endpoint: GET /api/events/{id}/
Response:

```bash
{
  "id": 1,
  "title": "Local Football Match",
  "description": "Cheer for your favorite local team as they take on their rivals.",
  "date": "2024-11-20",
  "time": "16:30:00",
  "category": "Sports"
}
```
#### 3. Update a Specific Event
Endpoint: PUT /api/events/{id}/
Request Body

```bash
{
  "title": "Local Football Match",
  "description": "Cheer for your favorite local team as they take on their rivals.",
  "date": "2024-11-20",
  "time": "16:30:00",
  "category": "Sports"
}
```
#### 4. Delete a Specific Event
Endpoint: DELETE /api/events/{id}/

Response:
```bash
 204 No Content
```
#### Upcoming Events Endpoint

#### Retrieve Upcoming Events
Endpoint: GET /api/events/upcoming/

Response:

```bash
[
  {
    "id": 1,
    "title": "Local Football Match",
    "description": "Cheer for your favorite local team as they take on their rivals.",
    "date": "2024-11-20",
    "time": "16:30:00",
    "category": "Sports"
  }
]
```

#### Retrieve Events by Category

Endpoint: GET /api/events/category/{categoryName}/

Response:

```bash
[
  {
    "id": 1,
    "title": "Local Football Match",
    "description": "Cheer for your favorite local team as they take on their rivals.",
    "date": "2024-11-20",
    "time": "16:30:00",
    "category": "Sports"
  }
]
```



## Sample Queries

```bash
# Create Event

curl -X POST http://127.0.0.1:8000/api/events/ \
-H "Content-Type: application/json" \
-d '{
  "title": "Birthday Party",
  "description": "Celebration for my birthday",
  "date": "2024-10-15",
  "time": "18:00:00",
  "category": "Personal"
}'

# Get All Events

curl -X GET http://127.0.0.1:8000/api/events/


# Get Specific Event

curl -X GET http://127.0.0.1:8000/api/events/1/

# Update Event

curl -X PUT http://127.0.0.1:8000/api/events/1/ \
-H "Content-Type: application/json" \
-d '{
  "title": "Updated Birthday Party",
  "description": "Updated celebration details",
  "date": "2024-10-16",
  "time": "19:00:00",
  "category": "Personal"
}'

# Delete Event

curl -X DELETE http://127.0.0.1:8000/api/events/1/

# Get Upcoming Events

curl -X GET http://127.0.0.1:8000/api/events/upcoming/

# Get Events by Category

curl -X GET http://127.0.0.1:8000/api/events/category/Personal/

```

## Unit Tests

```bash
# Test Cases

-- Create Event
Test if a new event can be created successfully.

-- Retrieve All Events
Test if all events can be retrieved successfully.

--Retrieve Specific Event
Test if a specific event can be retrieved successfully by ID.

--Update Event
Test if an existing event can be updated successfully.

--Delete Event
Test if an existing event can be deleted successfully.

--Get Upcoming Events
Test if events happening in the next 24 hours are retrieved successfully.

--Get Events by Category
Test if events can be retrieved based on their category.
```

## Logging

Logging is integrated into the API to help monitor the behavior and performance of the application. Here’s an overview of the logging levels used and their purposes:

### Logging Levels

1. **DEBUG**: 
   - Used for detailed information, typically of interest only when diagnosing problems.
   - Example: Logging the input received for an event creation request.

2. **INFO**: 
   - Used to confirm that things are working as expected.
   - Example: Logging a message when an event is successfully created or retrieved.

3. **WARNING**: 
   - Indicates that something unexpected happened, or indicative of some problem in the near future (e.g., ‘disk space low’).
   - Example: Logging a warning when a user tries to create an event with a date in the past.

4. **ERROR**: 
   - Used when there is a more serious problem that prevented the application from performing a function.
   - Example: Logging an error when an event cannot be found during a retrieval attempt.

5. **CRITICAL**: 
   - A very serious error, indicating that the program itself may be unable to continue running.
   - Example: Logging a critical failure when the database connection fails.

### Usage

In the views, logging statements can be added to capture important events. For instance, you might log when an API endpoint is hit, when an event is created, or if there’s a failure in processing a request. This helps in tracking the application's usage and diagnosing issues when they arise.

**Example Logging in Views:**
```python
import logging

logger = logging.getLogger(__name__)

class EventListCreateView(generics.ListCreateAPIView):
    # ...
    
    def create(self, request, *args, **kwargs):
        logger.info("Create event request received")
