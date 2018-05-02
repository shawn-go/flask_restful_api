# flask_restful_api
Provide the restful api to access the mongodb  
**HTTP Methods GET, POST, PUT, PATCH, DELETE provided**

## Environment
Python Version: 3.6.5  
Deployed Cloud Server: Google App Engine

## API (Class-Based Views)
* List (多筆) - **Provide get, post method**
  * GET: Retrieve a list of posts
  * POST: New a list of posts
* Detail (單筆) - **Provide get, put, patch, and delete method**
  * GET: Retrieve a detailed post
  * PUT: Update a detailed post
  * PATCH: Update the comments of post
  * DELETE: Delete the post

## Models
* Post
  * Title
  * Abstract
  * Body(內文)
  * Author
  * Category
  * pub_time(發佈日期;auto)
  * update_time(修改日期;auto)
  * comments (EmbeddedDocumentListField)
* Comment (EmbeddedDocument)
  * name
  * email
  * url
  * text(評論內容)
  * created_time(評論時間;auto)
