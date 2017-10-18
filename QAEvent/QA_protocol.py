import asyncio
from asyncio import BaseProtocol, BaseTransport

class QUANTAXIS_Transport(BaseTransport):
    
    def write(self,data):
        raise NotImplementedError
    def abort(self):
        raise NotImplementedError
    def bind(self,endpoint):
        raise NotImplementedError
    def unbind(self, endpoint):
        raise NotImplementedError
    def bindings(self):
        raise NotImplementedError
    def connect(self, endpoint):
        raise NotImplementedError
    def disconnect(self, endpoint):
        raise NotImplementedError
    def connections(self):
        raise NotImplementedError
    def subscribe(self, value):
        raise NotImplementedError
    def unsubscribe(self,value):
        raise NotImplementedError
    def subscriptions(self):
        raise NotImplementedError
    @asyncio.coroutine
    def enable_monitor(self, events=None):
        raise NotImplementedError
    def disable_monitor(self):
        raise NotImplementedError
class QUANTAXIS_Protocol(BaseProtocol):
    def msg_received(self,data):
        """Called when QUANTAXIS msg is received"""
    def event_received(self,event):
        """Called when QUANTAXIS event is received"""