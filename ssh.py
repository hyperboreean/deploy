try:
    import paramiko
except ImportError:
    import sys
    print >> sys.stderr 'paramiko library required.'
    sys.exit(1)


__all__ = ['SSH']


class SSH(object):
    def __init__(self, server, user, password = None):
        self._server = server
        self._user = user
        self._password = password

