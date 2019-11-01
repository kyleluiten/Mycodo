# coding=utf-8
import logging
import traceback

import flask_login
from flask_accept import accept
from flask_restplus import Namespace
from flask_restplus import Resource
from flask_restplus import abort
from flask_restplus import fields

from mycodo.mycodo_client import DaemonControl
from mycodo.mycodo_flask.utils import utils_general

logger = logging.getLogger(__name__)

ns_daemon = Namespace('daemon', description='Daemon operations')

default_responses = {
    200: 'Success',
    401: 'Invalid API Key',
    403: 'Insufficient Permissions',
    404: 'Not Found',
    422: 'Unprocessable Entity',
    429: 'Too Many Requests',
    460: 'Fail',
    500: 'Internal Server Error'
}

daemon_status_fields = ns_daemon.model('Daemon Status Fields', {
    'is_running': fields.Boolean,
    'RAM': fields.Float,
    'python_virtual_env': fields.Boolean
})

daemon_terminate_fields = ns_daemon.model('Daemon Terminate Fields', {
    'terminated': fields.Boolean
})


@ns_daemon.route('/')
@ns_daemon.doc(security='apikey', responses=default_responses)
class OutputPWM(Resource):
    """Checks information about the daemon"""

    @accept('application/vnd.mycodo.v1+json')
    @ns_daemon.marshal_with(daemon_status_fields)
    @flask_login.login_required
    def get(self):
        """Get the status of the daemon"""
        if not utils_general.user_has_permission('edit_controllers'):
            abort(403)

        try:
            control = DaemonControl()
            status = control.daemon_status()
            ram = control.ram_use()
            virtualenv = control.is_in_virtualenv()
            if status == 'alive':
                return {
                   'is_running': True,
                   'RAM': ram,
                   'python_virtual_env': virtualenv
                }, 200
        except Exception:
            return {
               'is_running': False,
               'RAM': None,
               'python_virtual_env': None
            }, 200


@ns_daemon.route('/terminate')
@ns_daemon.doc(security='apikey', responses=default_responses)
class OutputPWM(Resource):
    """Checks information about the daemon"""

    @accept('application/vnd.mycodo.v1+json')
    @ns_daemon.marshal_with(daemon_terminate_fields)
    @flask_login.login_required
    def post(self):
        """Shut down the daemon"""
        if not utils_general.user_has_permission('edit_controllers'):
            abort(403)

        try:
            control = DaemonControl()
            terminate = control.terminate_daemon()
            if terminate:
                return {'terminated': terminate}, 200
        except Exception:
            abort(500,
                  message='An exception occurred',
                  error=traceback.format_exc())
