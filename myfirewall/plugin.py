__author__ = 'stack'


from neutron.extensions.myfirewall import MyFirewallPluginBase
from neutron.openstack.common import log as logging

LOG = logging.getLogger(__name__)


class MyPlugin(MyFirewallPluginBase):
    supported_extension_aliases = ['myfirewall']

    def __init__(self):
        pass

    def create_myfirewall(self, context, myfirewall):
        LOG.debug("POST called.")

    def get_myfirewall(self, context, fwid, fields=None):
        LOG.debug("GET called.")

    def update_myfirewall(self, context, fwid, myfirewall):
        LOG.debug("PUT called.")

    def get_myfirewalls(self, context, filters=None, fields=None):
        LOG.debug("LIST called.")

    def delete_myfirewall(self, context, fwid):
        LOG.debug("DELETE called.")



