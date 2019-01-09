# Lessons
Supports registering, viewing, and updating lesson objects.

## Register a new student

**Request**:

`POST` `/lesson/`

Parameters:

Name       | Type   | Required | Description
-----------|--------|----------|----------------------------------------------
student    | id     | Yes      | The student of the lesson.
hour       | time   | Yes      | The hour that the lesson started.
value      | integer| Yes      | The value of the class (in hours/class).
weekdays   | list   | Yes      | The responsible or student telephone number.

*Note:*

- Not Authorization Protected
- final_hour field is filled automaticaly
- You can only post a student created by yourself. To know the students, a view with students list will be made.

**Response**:

```json
Content-Type application/json
201 Created

{
  "id": 196,
  "student": 4,
  "hour": "10:00:00",
  "duration": 58,
  "value": 12,
  "weekdays": [
      "seg",
      "dom"
  ],
  "final_hour": "10:58:00"
}

```

## Get a lesson's information

**Request**:

`GET` `/lesson/:id/`

Parameters:

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "id": 196,
  "student": 4,
  "hour": "10:00:00",
  "duration": 58,
  "value": 12,
  "weekdays": [
      "seg",
      "dom"
  ],
  "final_hour": "10:58:00"
}

```

## Update lesson's information

**Request**:

`PUT/PATCH` `/students/:id`

Parameters:

Name       | Type   | Description
-----------|--------|-----------------------------------------------
student    | id     | The student of the lesson.
hour       | time   | The hour that the lesson started.
value      | integer| The value of the class (in hours/class).
weekdays   | list   | The responsible or student telephone number.


*Note:*

- All parameters are optional
- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "id": 196,
  "student": 4,
  "hour": "10:00:00",
  "duration": 58,
  "value": 12,
  "weekdays": [
      "seg",
      "dom"
  ],
  "final_hour": "10:58:00"
}
```
