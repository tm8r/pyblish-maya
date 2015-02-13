
# Dependencies
import pyblish_endpoint.service
from .version import version

from maya import utils


class MayaService(pyblish_endpoint.service.EndpointService):
    def init(self, *args, **kwargs):
        return utils.executeInMainThreadWithResult(
            super(MayaService, self).init, *args, **kwargs)

    def next(self, *args, **kwargs):
        return utils.executeInMainThreadWithResult(
            super(MayaService, self).next, *args, **kwargs)

    def versions(self):
        versions = super(MayaService, self).versions()
        versions["pyblish-maya"] = version
        return versions
