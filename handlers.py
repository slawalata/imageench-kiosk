from abc import ABCMeta
from random import random
from typing import Any

import tornado.web
from tornado import httputil


class BaseHandler(tornado.web.RequestHandler, metaclass=ABCMeta):
    def __init__(
            self,
            application: "Application",
            request: httputil.HTTPServerRequest,
            **kwargs: Any
    ) -> None:
        super().__init__(application, request, **kwargs)


class CameraHandler(BaseHandler):
    def get(self):
        self.render("products.html")


class ImageHandler(BaseHandler):

    def get(self):
        print("halo")

    def post(self):
        print("post")
        file1 = self.request.files['webcam'][0]
        original_fname = file1['filename']

        output_file = open("uploads/" + original_fname, 'wb')
        output_file.write(file1['body'])

        self.finish("file " + original_fname + " is uploaded")
