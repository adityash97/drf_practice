API Sample Request/Response.
<h3>MOVIE</h3>
<h5>http://localhost:8000/</h5>
<p><h4>GET</h4></p>

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
  "director": {"id":1},
  "genre": [
    {"id": 1},
    {"id": 2}
  ]
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
  "genre": [
    {"id": 1}
  ]
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



