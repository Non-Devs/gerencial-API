# Students
Supports registering, viewing, and updating studens objects.

## Register a new student

**Request**:

`POST` `/students/`

Parameters:

Name             | Type   | Required | Description
-----------------|--------|----------|------------
first_name       | string | Yes      | The first name for the new student.
last_name        | string | Yes      | The last name for the new student.
responsible_name | string | Yes      | The responsible name for the new student.
telephone        | string | Yes      | The responsible or student telephone number.
birthday         | date   | Yes      | The student's birthday.
school           | string | Yes      | The school of the new student.
grade            | choice | Yes      | The grade of the new student.
adress           | text   | Yes      | The adress of the responsible or student.
subject          | choice | Yes      | The school subject of the new student.


*Note:*

- Not Authorization Protected

**Response**:

```json
Content-Type application/json
201 Created

{
  "id":1,
  "first_name":"Joao",
  "last_name":"das Neves",
  "responsible_name":"Ned",
  "telephone":"992789954",
  "birthday":"2000-11-11",
  "school":"Stella",
  "grade":"1em",
  "adress":"Sla",
  "subject":"geo",
  "teacher":"8a34e9f2-bc76-4b82-9200-81db8dcec579"
}

```

**Example**:

```bash
curl -X POST --data "first_name=Joao&last_name=das Neves&responsible_name=Ned&telephone=992789954&birthday=2000-11-11&school=Stella&grade=1em&adress=Sla&subject=geo" http://0.0.0.0:8000/api/v1/students/ -H 'Authorization: Token 5e4968a343905bcb78e62285e8ce74cdbcb7addd'
```
Response:
```bash                                                         
{"id":1,"first_name":"Joao","last_name":"das Neves","responsible_name":"Ned",
"telephone":"992789954","birthday":"2000-11-11","school":"Stella","grade":"1em",
"adress":"Sla","subject":"geo","teacher":"8a34e9f2-bc76-4b82-9200-81db8dcec579"}
```

The `teacher` returned with this response is the user id that registered the student. It is filled automatically.


## Get a student's information

**Request**:

`GET` `/students/:id/`

Parameters:

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "id":1,
  "first_name":"Joao",
  "last_name":"das Neves",
  "responsible_name":"Ned",
  "telephone":"992789954",
  "birthday":"2000-11-11",
  "school":"Stella",
  "grade":"1em",
  "adress":"Sla",
  "subject":"geo",
  "teacher":"8a34e9f2-bc76-4b82-9200-81db8dcec579"
}

```

**Example**

```bash
curl -X GET  http://0.0.0.0:8000/api/v1/students/1/ -H 'Authorization: Token 5e4968a343905bcb78e62285e8ce74cdbcb7addd'
```

Response:

```bash
{"id":1,"first_name":"Joao","last_name":"das Neves","responsible_name":"Ned","telephone":"992789954",
"birthday":"2000-11-11","school":"Stella","grade":"1em","adress":"Sla","subject":"geo",
"teacher":"8a34e9f2-bc76-4b82-9200-81db8dcec579"}
```

## Update students's information

**Request**:

`PUT/PATCH` `/students/:id`

Parameters:

Name             | Type   | Description
-----------------|--------|------------
first_name       | string | The first name for the new student.
last_name        | string | The last name for the new student.
responsible_name | string | The responsible name for the new student.
telephone        | string | The responsible or student telephone number.
birthday         | date   | The student's birthday.
school           | string | The school of the new student.
grade            | choice | The grade of the new student.
adress           | text   | The adress of the responsible or student.
subject          | choice | The school subject of the new student.



*Note:*

- All parameters are optional
- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "id":1,
  "first_name":"Joao",
  "last_name":"das Neves",
  "responsible_name":"Ned",
  "telephone":"992789954",
  "birthday":"2000-11-11",
  "school":"Stella",
  "grade":"1em",
  "adress":"Sla",
  "subject":"geo",
  "teacher":"8a34e9f2-bc76-4b82-9200-81db8dcec579"
}
```
