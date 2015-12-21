## Reader API description

### Authentication  
Via djoser, see https://github.com/sunscrapers/djoser  

#### Retrieve user  
URL: /api/v1/auth/me/  
Method: GET  

#### Register user  
URL: /api/v1/auth/register/  
Method: POST  
Parameters:  
username=[string]    
password=[string]  
```javascript  
{
"username": "test_user",
"password": "123"
}
```  
  
#### Login  
URL: /api/v1/auth/login/  
Method: POST  
Parameters:  
username=[string]    
password=[string]  
```javascript  
{
"username": "test_user",
"password": "123"
}
```
Response:  
```javascript
{
  "auth_token": "71678f82c1dd3470f9a3714c31c33a154511fed9"
}
```
  
#### Authenticated requests  
To make request authenticated, add Authorization header with value "Token [token]".    
Authorization: Token 71678f82c1dd34...  
  
  
### Books  
  
#### Vote for book  
Authentication required.  
URL: /api/v1/books/rate   
Method: POST  
Parameters:  
book=[integer], book ID  
vote=[integer], vote value, 0-10  
```javascript  
{  
    book: 11,  
    vote: 9  
}  
```
Response:  
```javascript
{
  "vote_value": 7,
  "user": 2,
  "book": {
    "title": "Lord of the Rings",
    "author": "J.R.R. Tolkien",
    "pic": "",
    "description": "Description",
    "rating": 7
  }
}
```
  
#### Get genres list    
URL: /api/v1/books/genres/  
Method: GET    
Example:  /api/v1/genres/  
Response:  
```javascript
[
  {
    "id": 1,
    "name": "Detective"
  },
  {
    "id": 2,
    "name": "Fantasy"
  },
  ...
]
```

#### Get books by genre    
URL: /api/v1/books/list  
Method: GET  
Parameters:  
genre=[string]   
Example:  /api/v1/books/list/?genre_name=Detective  
Response:
```javascript
[
  {
    "id": 1,
    "title": "Poirot",
    "author": "Agatha Cristie",
    "pic": "",
    "description": "Description",
    "rating": 7
  },
  {
    "id": 5,
    "title": "Miss Marple",
    "author": "Agatha Cristie",
    "pic": "",
    "description": "Description",
    "rating": 7
  },
  ...
]
```

### Reader  

#### Get user's books  
URL: /api/v1/users/books/  
Method: GET   
Parameters:   
user=[integer]  
Example:  /api/v1/books/?user=2    
Response:  
```javascript
{
  "planned_books": [],
  "completed_books": [
    {
      "id": 1,
      "title": "Poirot",
      "author": "Agatha Cristie",
      "pic": "",
      "description": "Description",
      "rating": 7
    }
  ]
}
```
  
#### Add book to planned books list  
URL: /api/v1/users/books/  
Method: POST  
```javascript   
{  
    book: 11  
}  
```
Response: None  

#### Mark book as read   
URL: /api/v1/users/books/[Book ID]     
Method: PUT   
Response: None  

#### Remove book  
URL: /api/v1/users/books/[Book ID]         
Method: DELETE  
Response: None  
