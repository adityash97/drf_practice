#API Details

###Register

<h5>http://localhost:8000/account/register/</h5>
<p><h4>POST</h4></p>

Request:

```json
{
  "username": "Aditya",
  "first_name": "Aditya",
  "last_name": "Anand",
  "password": "password123@",
  "password2": "password123@",
  "email": "adityash212@gmail.com"
}
```

Response:

```json
{
  "success": true,
  "user": {
    "id": 14,
    "username": "Aditya",
    "first_name": "Aditya",
    "last_name": "Anand",
    "email": "adityash212@gmail.com"
  },
  "token": "8b1f5ce1fd6f0d578a971cd26e1b8ebb083f7e81"
}
```

###Login

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
  "success": true,
  "username": "Aditya",
  "email": "adityash212@gmail.com",
  "token": "8b1f5ce1fd6f0d578a971cd26e1b8ebb083f7e81"
}
```

###Login

<h5>http://localhost:8000/account/logout/</h5>
<p><h4>POST</h4></p>

Request:

```json
Headers
{
  Authorization : Token 8b1f5ce1fd6f0d578a971cd26e1b8ebb083f7e81
}

```

Response:

```json
{
  "success": true,
  "detail": "Logged out!"
}
```
