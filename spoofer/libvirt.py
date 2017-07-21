import os

import libvirt


class Libvirt(object):
    '''Libvirt contains functionality to instantiate
    a new connection to the hypervisor and extract
    data about each active and non-active kvm
    machine.
    It will try to instantiate a new local user
    session if no hypervisor URI was specified.
    '''
    def __init__(
        self,
        hypervisor_URI='',
        hypervisor_user='',
        hypervisor_password='',
    ):
        self._domain_list = []
        # NOTE: qemu+ssh://root@localhost/system
        # TODO: need to differentiate between user local session, remote user
        # sessions, local /system and remote /system.
        if hypervisor_URI == '':
            self._URI = None
        else:
            self._URI = 'qemu+ssh://{}'

        self._client = self.instantiate_client()

    def instantiate_client(self):
        self._new_client = libvirt.openReadOnly(self._URI)
        if self._new_client == None:
            raise ExceptionHypervisorConnect

    def _set_domain_list(self):
        pass

    def _get_ip_addresses(self):
        pass

    def set_domain_spoofing(self):
        pass

class ExceptionHypervisorConnect(Exception):
    def __init__(self, URI):
        pass
