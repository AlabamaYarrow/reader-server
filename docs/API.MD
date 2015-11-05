## Reader API description

### Authentication

TODO

### Books

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

#### Rate book
... 
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

#### Add book to list
Method: POST  
```javascript  
{  
    book: 11  
}  
```

#### Mark book as read
Method: POST  



