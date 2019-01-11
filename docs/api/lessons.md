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

## Get a lesson's list

**Request**:

`GET` `/lesson/`

Parameters:

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

[    
  {
      "id": 194,
      "student": 4,
      "hour": "12:12:00",
      "duration": 12,
      "value": 12,
      "weekdays": [
          "qui",
          "seg",
          "qua",
          "sex",
          "ter"
      ],
      "final_hour": "12:24:00"
  },
  {
      "id": 195,
      "student": 4,
      "hour": "10:00:00",
      "duration": 12,
      "value": 12,
      "weekdays": [
          "dom",
          "seg"
      ],
      "final_hour": "10:12:00"
  },
  {
      "id": 196,
      "student": 4,
      "hour": "10:00:00",
      "duration": 58,
      "value": 12,
      "weekdays": [
          "dom",
          "seg"
      ],
      "final_hour": "11:01:00"
  }
]

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

**Example**:

```bash
curl -X GET  http://0.0.0.0:8000/api/v1/lesson/ -H 'Authorization: Token 5e4968a343905bcb78e62285e8ce74cdbcb7addd'
```
Response:
```bash                                                         
[{"id":2,"student":5,"hour":"05:00:00","duration":205,"value":20,"weekdays":[],"final_hour":"10:10:10"},{"id":7,"student":6,"hour":"10:10:00","duration":1,"value":1,"weekdays":[],"final_hour":"10:10:00"},{"id":8,"student":5,"hour":"08:50:00","duration":10,"value":10,"weekdays":[],"final_hour":"05:05:00"},{"id":9,"student":6,"hour":"08:50:00","duration":10,"value":10,"weekdays":[],"final_hour":"08:50:00"},{"id":11,"student":6,"hour":"10:10:00","duration":105,"value":105,"weekdays":[],"final_hour":"10:10:00"},{"id":10,"student":6,"hour":"05:55:55","duration":55,"value":55,"weekdays":[],"final_hour":"15:24:00"},{"id":12,"student":6,"hour":"05:55:55","duration":55,"value":55,"weekdays":[],"final_hour":"05:55:55"},{"id":13,"student":6,"hour":"05:55:55","duration":55,"value":55,"weekdays":[],"final_hour":"05:55:55"},{"id":15,"student":6,"hour":"10:10:00","duration":45,"value":45,"weekdays":[],"final_hour":"10:10:00"}]
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
