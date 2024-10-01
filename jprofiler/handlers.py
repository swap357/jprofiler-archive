import json
from jupyter_server.extension.handler import ExtensionHandlerMixin
from jupyter_server.base.handlers import APIHandler
import tornado
from scalene import scalene_profiler

class PingHandler(ExtensionHandlerMixin, APIHandler):
    # The following decorator should be present on all verb methods (head, get, post,
    # patch, put, delete, options) to ensure only authorized user can request the
    # Jupyter server
    @property
    def ping_response(self):
        return self.settings["ping_response"]

    @tornado.web.authenticated
    def get(self):
        self.finish(json.dumps({
            "ping_response": self.ping_response
        }))

class ProfileHandler(ExtensionHandlerMixin, APIHandler):
    @tornado.web.authenticated
    async def post(self):
        data = json.loads(self.request.body)
        code = data.get('code', '')
        
        # Profile the code using Scalene
        profiler = scalene_profiler.Scalene()
        profiler.start()
        
        # Execute the code (you might want to use a safer execution method)
        exec(code)
        
        profiler.stop()
        
        # Get the profiling results
        results = profiler.output_profile()
        
        self.finish(json.dumps({
            "profile_results": results
        }))
