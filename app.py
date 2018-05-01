#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import datetime
from flask import request, jsonify
from flask.views import MethodView

from factory import create_app
from models import Post, Comment
import config


app = create_app(config)

@app.route('/')
def hello_rest():
    return '''
    <html>
        <head>
            <meta charset="utf-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Code Service</title>
            <link href="//cdn.bootcss.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body>
            <div class="container">
                <div class="row">
                    <div class="col-md-8 col-md-offset-2">
                        <h1>Flask RESTful API Example</h1><hr>
                        <p>Welcome to Flask RESTful API Example!</p>
                    </div>
                </div>
            </div>
        </body>
    </html>
    '''

class PostListCreateView(MethodView):
    def get(self):
        posts = Post.objects.all()
        category = request.args.get('category')
        # tag = request.args.get('tag')

        if category:
            posts = posts.filter(category=category)

        # if tag:
        #     posts = posts.filter(tag=tag)

        data = [post.to_dict() for post in posts]

        return jsonify(posts=data)

    def post(self):
        '''
        Send a json data as follow will create a new blog instance:

        {
            "title": "Title 1",
            "slug": "title-1",
            "abstract": "Abstract for this article",
            "raw": "The article content",
            "author": "Gevin",
            "category": "default",
            "tags": ["tag1", "tag2"]
        }
        '''

        data = request.get_json()

        article = Post()
        article.title = data.get('title')
        # article.slug = data.get('slug')
        article.abstract = data.get('abstract')
        article.body = data.get('body')
        # article.raw = data.get('raw')
        article.author = data.get('author')
        article.category = data.get('category')
        # article.tags = data.get('tags')

        article.save()

        return jsonify(post=article.to_dict())



class PostDetailGetUpdateDeleteView(MethodView):
    """
    Originally, the unique key is the slug, now turn it into id
    """
    def get(self, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return jsonify({'error': 'post does not exist'}), 404

        return jsonify(post=post.to_dict())

    def put(self, pk):
        """
        The required cols: title, body, author
        """
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return jsonify({'error': 'post does not exist'}), 404

        data = request.get_json()

        if not data.get('title'):
            return 'title is needed in request data', 400

        # if not data.get('slug'):
        #     return 'slug is needed in request data', 400

        # if not data.get('abstract'):
        #     return 'abstract is needed in request data', 400

        if not data.get('body'):
            return 'body is needed in request data', 400

        if not data.get('author'):
            return 'author is needed in request data', 400

        # if not data.get('category'):
        #     return 'category is needed in request data', 400

        # if not data.get('tags'):
        #     return 'tags is needed in request data', 400

        

        post.title = data['title']
        # post.slug = data['slug']
        post.abstract = data.get('abstract')
        post.body = data['body']
        post.author = data['author']
        post.category = data.get('category')
        # post.tags = data['tags']

        post.save()

        return jsonify(post=post.to_dict())

    def patch(self, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return jsonify({'error': 'post does not exist'}), 404

        data = request.get_json()

        # post.title = data.get('title') or post.title 
        # post.slug = data.get('slug') or post.slug
        # post.abstract = data.get('abstract') or post.abstract
        # post.body = data.get('body') or post.body
        # post.author = data.get('author') or post.author
        # post.category = data.get('category') or post.category
        # post.tags = data.get('tags') or post.tags
        name = data.get('name')
        email = data.get('email')
        url = data.get('url')
        text = data.get('text')
        created_time = datetime.datetime.now()
        # post.comments.create(name=name, email=email, url=url, text=text, created_time=created_time)
        if url:
            post.comments.create(name=name, email=email, url=url, text=text, created_time=created_time)
        else:
            post.comments.create(name=name, email=email, text=text, created_time=created_time)
        post.save_without_update_time()

        return jsonify(post=post.to_dict())

    def delete(self, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return jsonify({'error': 'post does not exist'}), 404

        post.delete()

        return 'Succeed to delete post', 204

app.add_url_rule('/posts/', view_func=PostListCreateView.as_view('posts'))
app.add_url_rule('/posts/<pk>/', view_func=PostDetailGetUpdateDeleteView.as_view('post'))

if __name__ == '__main__':
    app.run(
        host = '0.0.0.0',
        port = 5000,
        debug = True
    )