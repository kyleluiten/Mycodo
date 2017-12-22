# -*- coding: utf-8 -*-
#
# forms_misc.py - Miscellaneous Flask Forms
#

from flask_babel import lazy_gettext
from flask_wtf import FlaskForm
from wtforms import DecimalField
from wtforms import FileField
from wtforms import HiddenField
from wtforms import IntegerField
from wtforms import StringField
from wtforms import SubmitField
from wtforms import validators
from wtforms import widgets


#
# Camera Use
#

class Camera(FlaskForm):
    camera_id = IntegerField('Camera ID', widget=widgets.HiddenInput())
    capture_still = SubmitField(lazy_gettext('Capture Still'))
    start_timelapse = SubmitField(lazy_gettext('Start Timelapse'))
    pause_timelapse = SubmitField(lazy_gettext('Pause Timelapse'))
    resume_timelapse = SubmitField(lazy_gettext('Resume Timelapse'))
    stop_timelapse = SubmitField(lazy_gettext('Stop Timelapse'))
    timelapse_interval = DecimalField(
        lazy_gettext('Interval (seconds)'),
        validators=[validators.NumberRange(
            min=0,
            message=lazy_gettext('Photo Interval must be a positive value')
        )]
    )
    timelapse_runtime_sec = DecimalField(
        lazy_gettext('Run Time (seconds)'),
        validators=[validators.NumberRange(
            min=0,
            message=lazy_gettext('Total Run Time must be a positive value')
        )]
    )
    start_stream = SubmitField(lazy_gettext('Start Stream'))
    stop_stream = SubmitField(lazy_gettext('Stop Stream'))


#
# Daemon Control
#

class DaemonControl(FlaskForm):
    stop = SubmitField(lazy_gettext('Stop Daemon'))
    start = SubmitField(lazy_gettext('Start Daemon'))
    restart = SubmitField(lazy_gettext('Restart Daemon'))


#
# Export/Import Options
#

class ExportMeasurements(FlaskForm):
    measurement = StringField(lazy_gettext('Measurement to Export'))
    date_range = StringField(lazy_gettext('Time Range DD/MM/YYYY HH:MM'))
    export_data_csv = SubmitField(lazy_gettext('Export Data as CSV'))

class ExportSettings(FlaskForm):
    export_settings_zip = SubmitField(lazy_gettext('Export Settings'))

class ImportSettings(FlaskForm):
    settings_import_file = FileField('Upload')
    settings_import_upload = SubmitField(lazy_gettext('Import Settings'))

class ExportInfluxdb(FlaskForm):
    export_influxdb_zip = SubmitField(lazy_gettext('Export Influxdb'))

class ImportInfluxdb(FlaskForm):
    influxdb_import_file = FileField('Upload')
    influxdb_import_upload = SubmitField(lazy_gettext('Import Influxdb'))




#
# Log viewer
#

class LogView(FlaskForm):
    lines = IntegerField(
        lazy_gettext('Number of Lines'),
        render_kw={'placeholder': lazy_gettext('Lines')},
        validators=[validators.NumberRange(
            min=1,
            message=lazy_gettext('Number of lines should be greater than 0')
        )]
    )
    loglogin = SubmitField(lazy_gettext('Login Log'))
    loghttp_access = SubmitField(lazy_gettext('HTTP Access'))
    loghttp_error = SubmitField(lazy_gettext('HTTP Error'))
    logdaemon = SubmitField(lazy_gettext('Daemon Log'))
    logbackup = SubmitField(lazy_gettext('Backup Log'))
    logkeepup = SubmitField(lazy_gettext('KeepUp Log'))
    logupgrade = SubmitField(lazy_gettext('Upgrade Log'))
    logrestore = SubmitField(lazy_gettext('Restore Log'))


#
# Upgrade
#

class Upgrade(FlaskForm):
    upgrade = SubmitField(lazy_gettext('Upgrade Mycodo'))


#
# Backup/Restore
#

class Backup(FlaskForm):
    backup = SubmitField(lazy_gettext('Create Backup'))
    restore = SubmitField(lazy_gettext('Restore Backup'))
    delete = SubmitField(lazy_gettext('Delete Backup'))
    full_path = HiddenField()
    selected_dir = HiddenField()
