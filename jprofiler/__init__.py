"""resource profiler for jupyter notebook"""
from .extension import Extension
from .handlers import ProfileHandler
__version__ = "0.1.0"


def _jupyter_server_extension_points():
    return [{
        "module": "jprofiler",
        "app": Extension
    }]
