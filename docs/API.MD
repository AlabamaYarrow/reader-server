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
To make request authenticated, add Authentication header with value "Token [token]".    
Authentication: Token 71678f82c1dd34...  
  
  
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

#### Get books by genre    
URL: /api/v1/books/list  
Method: GET  
Parameters:  
genre=[string]   
Example:  /api/v1/books/?genre=detective  

#### Add book to list  
Method: POST    
```javascript  
{  
    book: 11  
}  
```

#### Mark book as read   
TODO  


### User  

#### Get user's books  
TODO  
