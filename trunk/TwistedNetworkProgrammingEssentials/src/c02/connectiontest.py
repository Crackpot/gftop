'''
>>> dir(defer)
['AlreadyCalledError', 'AlreadyTryingToLockError', 'DebugInfo', 'Deferred', 'DeferredFilesystemLock', 'DeferredList', 'DeferredLock', 'DeferredQueue', 'DeferredSemaphore', 'FAILURE', 'FirstError', 'QueueOverflow', 'QueueUnderflow', 'SUCCESS', 'TimeoutError', '_ConcurrencyPrimitive', '_DefGen_Return', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '_deferGenerator', '_inlineCallbacks', '_nothing', '_parseDListResult', 'deferredGenerator', 'execute', 'fail', 'failure', 'gatherResults', 'generators', 'getDebugging', 'inlineCallbacks', 'lockfile', 'log', 'logError', 'maybeDeferred', 'mergeFunctionMetadata', 'nested_scopes', 'passthru', 'returnValue', 'setDebugging', 'succeed','timeout', 'traceback', 'unsignedID', 'waitForDeferred', 'warnings']

'''
from twisted.internet import reactor,defer,protocol

class CallbackAndDisconnectProtocol(protocol.Protocol):
    def connectionMade(self):
        self.factory.deferred.callback("Connected.")
        self.transport.loseConnection()