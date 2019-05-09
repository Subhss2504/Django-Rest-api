# Django-Rest-api
CRUD API with NoSql

Database used MongoDB

#Refer to snapshots for more details

##FOR USING DJANGO REST API BACKEND

#http://localhost:8000/rest-auth/registration/
For Registration 

#http://localhost:8000/rest-auth/login/
for login 


#http://localhost:8000/api/users/

GET Method

GET /api/users/
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "count": 9,
    "next": "http://localhost:8000/api/users/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "first_name": "James",
            "last_name": "Butt",
            "age": 70,
            "company_name": "Benton, John B Jr",
            "city": "New Orleans",
            "state": "LA",
            "zip_code": "70116",
            "email": "jbutt@gmail.com",
            "web": "http://www.bentonjohnbjr.com"
        },
        {
            "id": 2,
            "first_name": "Josephine",
            "last_name": "Darakjy",
            "age": 48,
            "company_name": "Chanay, Jeffrey A Esq",
            "city": "Brighton",
            "state": "MI",
            "zip_code": "48116",
            "email": "josephine_darakjy@darakjy.org",
            "web": "http://www.chanayjeffreyaesq.com"
        },
        {
            "id": 3,
            "first_name": "Art",
            "last_name": "Venere",
            "age": 80,
            "company_name": "Chemel, James L Cpa",
            "city": "Bridgeport",
            "state": "NJ",
            "zip_code": "80514",
            "email": "art@venere.org",
            "web": "http://www.chemeljameslcpa.com"
        },
        {
            "id": 4,
            "first_name": "Lenna",
            "last_name": "Paprocki",
            "age": 99,
            "company_name": "Feltz Printing Service",
            "city": "Anchorage",
            "state": "AK",
            "zip_code": "99501",
            "email": "lpaprocki@hotmail.com",
            "web": "http://www.feltzprintingservice.com"
        },
        {
            "id": 6,
            "first_name": "Simona",
            "last_name": "Morasca",
            "age": 44,
            "company_name": "Chapman, Ross E Esq",
            "city": "Ashland",
            "state": "OH",
            "zip_code": "44805",
            "email": "simona@morasca.com",
            "web": "http://www.chapmanrosseesq.com"
        }
    ]
}

#http://localhost:8000/api/users/create
POST Method


OPTIONS /api/users/create
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "name": "Employee Create",
    "description": "",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ],
    "actions": {
        "POST": {
            "id": {
                "type": "integer",
                "required": false,
                "read_only": true,
                "label": "ID"
            },
            "first_name": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "First name",
                "max_length": 50
            },
            "last_name": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Last name",
                "max_length": 50
            },
            "age": {
                "type": "integer",
                "required": true,
                "read_only": false,
                "label": "Age",
                "min_value": -2147483648,
                "max_value": 2147483647
            },
            "company_name": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Company name",
                "max_length": 80
            },
            "city": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "City",
                "max_length": 50
            },
            "state": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "State",
                "max_length": 50
            },
            "zip_code": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Zip code",
                "max_length": 50
            },
            "email": {
                "type": "email",
                "required": true,
                "read_only": false,
                "label": "Email",
                "max_length": 254
            },
            "web": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Web",
                "max_length": 100
            }
        }
    }
}

#http://localhost:8000/api/users/?ordering=age

GET /api/users/?ordering=age
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "count": 9,
    "next": "http://localhost:8000/api/users/?ordering=age&page=2",
    "previous": null,
    "results": [
        {
            "id": 10,
            "first_name": "Kris",
            "last_name": "Marrier",
            "age": 21,
            "company_name": "King, Christopher A Esq",
            "city": "Baltimore",
            "state": "MD",
            "zip_code": "21224",
            "email": "kris@gmail.com",
            "web": "http://www.kingchristopheraesq.com"
        },
        {
            "id": 6,
            "first_name": "Simona",
            "last_name": "Morasca",
            "age": 44,
            "company_name": "Chapman, Ross E Esq",
            "city": "Ashland",
            "state": "OH",
            "zip_code": "44805",
            "email": "simona@morasca.com",
            "web": "http://www.chapmanrosseesq.com"
        },
        {
            "id": 2,
            "first_name": "Josephine",
            "last_name": "Darakjy",
            "age": 48,
            "company_name": "Chanay, Jeffrey A Esq",
            "city": "Brighton",
            "state": "MI",
            "zip_code": "48116",
            "email": "josephine_darakjy@darakjy.org",
            "web": "http://www.chanayjeffreyaesq.com"
        },
        {
            "id": 9,
            "first_name": "Sage",
            "last_name": "Wieser",
            "age": 57,
            "company_name": "Truhlar And Truhlar Attys",
            "city": "Sioux Falls",
            "state": "SD",
            "zip_code": "57105",
            "email": "sage_wieser@cox.net",
            "web": "http://www.truhlarandtruhlarattys.com"
        },
        {
            "id": 7,
            "first_name": "Mitsue",
            "last_name": "Tollner",
            "age": 60,
            "company_name": "Morlong Associates",
            "city": "Chicago",
            "state": "IL",
            "zip_code": "60632",
            "email": "mitsue_tollner@yahoo.com",
            "web": "http://www.morlongassociates.com"
        }
    ]
}

#http://localhost:8000/api/users/?first_name=James

GET /api/users/?first_name=James
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "first_name": "James",
            "last_name": "Butt",
            "age": 70,
            "company_name": "Benton, John B Jr",
            "city": "New Orleans",
            "state": "LA",
            "zip_code": "70116",
            "email": "jbutt@gmail.com",
            "web": "http://www.bentonjohnbjr.com"
        }
    ]
}

#http://localhost:8000/api/users/3/update/

Update 

OPTIONS /api/users/3/update/
HTTP 200 OK
Allow: PUT, PATCH, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "name": "Employee Update",
    "description": "",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ],
    "actions": {
        "PUT": {
            "id": {
                "type": "integer",
                "required": false,
                "read_only": true,
                "label": "ID"
            },
            "first_name": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "First name",
                "max_length": 50
            },
            "last_name": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Last name",
                "max_length": 50
            },
            "age": {
                "type": "integer",
                "required": true,
                "read_only": false,
                "label": "Age",
                "min_value": -2147483648,
                "max_value": 2147483647
            },
            "company_name": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Company name",
                "max_length": 80
            },
            "city": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "City",
                "max_length": 50
            },
            "state": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "State",
                "max_length": 50
            },
            "zip_code": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Zip code",
                "max_length": 50
            },
            "email": {
                "type": "email",
                "required": true,
                "read_only": false,
                "label": "Email",
                "max_length": 254
            },
            "web": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Web",
                "max_length": 100
            }
        }
    }
}

#http://localhost:8000/api/users/3/delete/

DELETE

OPTIONS /api/users/3/delete/
HTTP 200 OK
Allow: DELETE, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "name": "Employee Delete",
    "description": "",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ]
}
