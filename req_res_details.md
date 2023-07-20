API Sample Request/Response.

<h3>Register</h3>
<h5>http://localhost:8000/account/register/</h5>
<p><h4>POST</h4></p>

Request:

```json
{
  "username": "Aditya",
  "password": "password123@",
  "password2": "password123@",
  "email": "adi@xyz.com"
}
```

Response:

```json
{
  "msg": "Register Succesfully",
  "userdetails": {
    "email": "adi@xyz.com",
    "username": "Aditya",
    "is_active": false
  },
  "token": "c275ab430a987a35e2291b8de51f2fdec28de8cf"
}
```

<h3>Login</h3>
<h5>http://localhost:8000/account/login/</h5>
<p><h4>POST</h4></p>

Request:

```json
{
  "username": "Aditya",
  "password": "password123@"
}
```

Response:

```json
{
  "token": "c275ab430a987a35e2291b8de51f2fdec28de8cf"
}
```

<h3>Logout</h3>
<h5>http://localhost:8000/account/logout/</h5>
<p><h4>POST</h4></p>

Request:

<h6>Pass token in Header</h6>

Response:

```json
{
  "msg": "logged out!"
}
```

<h3>MOVIE</h3>
<h5>http://localhost:8000/</h5>
<p><h4>GET</h4></p>

Request:

```json
[
  {
    "id": 1,
    "title": "DDLJ 2",
    "description": "",
    "average_rating": 0,
    "total_review": 0,
    "released_date": null,
    "duration": null,
    "director": {
      "id": 1,
      "name": "DDLJ Director",
      "created_on": "2023-07-17T20:40:38.548140Z",
      "updated_on": "2023-07-17T20:40:38.548169Z"
    },
    "genre": [
      {
        "genre": "Adventure"
      },
      {
        "genre": "Drama"
      }
    ]
  }
]
```

<p><h4>POST</h4></p>

Request:

```json
{
  "title": "DDLJ 2",
  "director": { "id": 1 },
  "genre": [{ "id": 1 }, { "id": 2 }]
}
```

Response :

```json
{
  "id": 1,
  "title": "DDLJ 2",
  "description": "",
  "average_rating": 0,
  "total_review": 0,
  "released_date": null,
  "duration": null,
  "director": {
    "id": 1,
    "name": "DDLJ Director",
    "created_on": "2023-07-17T20:40:38.548140Z",
    "updated_on": "2023-07-17T20:40:38.548169Z"
  },
  "genre": [
    {
      "genre": "Adventure"
    },
    {
      "genre": "Drama"
    }
  ]
}
```

<p><h4>UPDATE</h4></p>
Request:

```json
{
  "title": "DDLJ 1",
  "genre": [{ "id": 1 }]
}
```

Response:

```json
{
  "id": 1,
  "title": "DDLJ 1",
  "description": "",
  "average_rating": 0,
  "total_review": 0,
  "released_date": null,
  "duration": null,
  "director": {
    "id": 1,
    "name": "DDLJ Director",
    "created_on": "2023-07-17T20:40:38.548140Z",
    "updated_on": "2023-07-17T20:40:38.548169Z"
  },
  "genre": [
    {
      "genre": "Adventure"
    }
  ]
}
```
