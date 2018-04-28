#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from flask import url_for

from factory import db

class Comment(db.EmbeddedDocument):
    name = db.StringField(max_length=100)
    email = db.EmailField(max_length=255)
    url = db.URLField(blank=True)
    text = db.StringField()
    created_time = db.DateTimeField()

    def to_dict(self):
        comment_dict = {}
        
        comment_dict['name'] = self.name
        comment_dict['email'] = self.email
        comment_dict['url'] = self.url
        comment_dict['text'] = self.text
        comment_dict['created_time'] = self.created_time.strftime('%Y-%m-%d %H:%M:%S')
        return comment_dict


class Post(db.Document):
    title = db.StringField(max_length=255, required=True)
    # slug = db.StringField(max_length=255, required=True, unique=True)
    abstract = db.StringField()
    body = db.StringField(required=True)
    pub_time = db.DateTimeField()
    update_time = db.DateTimeField()
    author = db.StringField()
    category = db.StringField(max_length=64)
    # tags = db.ListField(db.StringField(max_length=30))
    comments = db.EmbeddedDocumentListField(Comment)

    def save(self, *args, **kwargs):
        now = datetime.datetime.now()
        if not self.pub_time:
            self.pub_time = now
        self.update_time = now
        
        return super(Post, self).save(*args, **kwargs)

    def save_without_update_time(self, *args, **kwargs):
        return super(Post, self).save(*args, **kwargs)

    def to_dict(self):
        post_dict = {}
        
        post_dict['title'] = self.title
        # post_dict['slug'] = self.slug
        post_dict['abstract'] = self.abstract
        post_dict['body'] = self.body
        post_dict['pub_time'] = self.pub_time.strftime('%Y-%m-%d %H:%M:%S')
        post_dict['update_time'] = self.update_time.strftime('%Y-%m-%d %H:%M:%S')
        post_dict['author'] = self.author
        post_dict['category'] = self.category
        # post_dict['tags'] = self.tags
        post_dict['pk'] = str(self.pk)
        post_dict['comments'] = [comment.to_dict() for comment in self.comments]
        return post_dict


    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    meta = {
        'allow_inheritance': True,
        'indexes': ['_id'],
        # 'indexes': ['slug'],
        'ordering': ['-pub_time']
    }




