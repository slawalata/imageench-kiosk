import os

import tornado.ioloop
import tornado.web
import tornado.gen

from tornado.options import define, options

from handlers import CameraHandler, ImageHandler

define("port", default=8888, help="run in tornado on xxxx port", type=int)
define("id", default=0, help="camera id", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            ('/', CameraHandler),
            ('/image', ImageHandler),
        ]

        tornado.web.Application.__init__(
            self,
            handlers,
            debug=True,
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o"
        )


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
