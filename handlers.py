from abc import ABCMeta
from random import random
from typing import Any

import tornado
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
