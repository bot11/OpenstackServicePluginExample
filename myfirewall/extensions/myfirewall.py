__author__ = 'stack'

import abc
from neutron.api import extensions
from neutron import manager
from neutron import quota
from neutron.api.v2 import base
from neutron.services.service_base import ServicePluginBase
from neutron.openstack.common import log as logging

LOG = logging.getLogger(__name__)

RESOURCE_ATTRIBUTE_MAP = {
    'myfirewall': {
        'fwid': {'allow_post': True, 'allow_put': True, 'is_visible': True},
        'name': {'allow_post': True, 'allow_put': True, 'is_visible': True},
        'source': {'allow_post': True, 'allow_put': True, 'is_visible': True},
        'destination': {'allow_post': True, 'allow_put': True, 'is_visible': True},
        'tenant_id': {'allow_post': True, 'allow_put': False, 'required_by_policy': True,
                      'validate': {'type:string': None}, 'is_visible': True}
    }

}


class Myfirewall(extensions.ExtensionDescriptor):

    @classmethod
    def get_name(cls):
        return "Firewall service"

    @classmethod
    def get_alias(cls):
        return "myfirewall"

    @classmethod
    def get_description(cls):
        return "sample firewall service"

    @classmethod
    def get_namespace(cls):
        """Returns Extended Resource Namespace."""
        return "http://myfirewall.org"

    @classmethod
    def get_updated(cls):
        """Returns Extended Resource Update Time."""
        return "2014-05-14T13:25:27-06:00"

    @classmethod
    def get_resources(cls):
        """Returns Extended Resources."""
        resource_name = "myfirewall"
        collection_name = resource_name + "s"
        LOG.debug("Available plugins=> %r" % [r for r in manager.NeutronManager.get_service_plugins()])
        # plugin = manager.NeutronManager.get_plugin()
        plugin = manager.NeutronManager.get_service_plugins()['myfirewall']
        params = RESOURCE_ATTRIBUTE_MAP.get(collection_name, dict())
        quota.QUOTAS.register_resource_by_name(resource_name)
        controller = base.create_resource(collection_name,
                                          resource_name,
                                          plugin, params)
        return [extensions.ResourceExtension(collection_name,
                                             controller,
                path_prefix="/",
                attr_map=params)]

    @classmethod
    def get_plugin_interface(cls):
        return MyFirewallPluginBase

    def update_attributes_map(self, attributes):
        super(Myfirewall, self).update_attributes_map(
            attributes, extension_attrs_map=RESOURCE_ATTRIBUTE_MAP)

    def get_extended_resources(self, version):
        if version == "2.0":
            return RESOURCE_ATTRIBUTE_MAP
        else:
            return {}

class MyFirewallPluginBase(ServicePluginBase):
    __metaclass__ = abc.ABCMeta

    def get_plugin_name(self):
        return "myfirewall"

    def get_plugin_type(self):
        return "myfirewall"

    def get_plugin_description(self):
        return 'Myfirewall service plugin'

    @abc.abstractmethod
    def get_myfirewalls(self, context, filters=None, fields=None):
        pass

    @abc.abstractmethod
    def get_myfirewall(self, context, fwid, fields=None):
        pass

    @abc.abstractmethod
    def create_myfirewall(self, context, myfirewall):
        pass

    @abc.abstractmethod
    def update_myfirewall(self, context, fwid, myfirewall):
        pass

    @abc.abstractmethod
    def delete_myfirewall(self, context, fwid):
        pass
