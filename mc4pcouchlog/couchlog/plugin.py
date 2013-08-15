'''
Created on Aug 13, 2013

@author: Paulson McIntyre (GpMidi) <paul@gpmidi.net>
'''
import logging
log = logging.getLogger('couchlog.plugin')

import datetime
import os, os.path
import sys

from mc4p.plugins import MC4Plugin
from mc4p.messages import cli_msgs, srv_msgs

from couchlog.models import *


class CouchLogPlugin(MC4Plugin):
    IGNORE = {
              'msgtype':True,
              'raw_bytes':True,
              }
    
    def default_handler(self, msg, source):
        try:
            e = RawEvent()
            if source == 'server':
                e.direction = 's2c'
                msgs = srv_msgs
            elif source == 'client':
                e.direction = 'c2s'
                msgs = cli_msgs
            else:
                e.direction = 'other'

            e.eventType = msg['msgtype']
            try:
                et = msgs[msg['msgtype']]
                e.eventTypeName = et.name
            except ValueError, e:
                e.eventTypeName = None

            e.rawBytes = msg['raw_bytes']
            e.occured = datetime.datetime.utcnow()

            try:
                for k, v in msg.iteritems():
                    try:
                        if k not in self.IGNORE:
                            e.otherAttrs[k] = v
                    except Exception, e:
                        log.exception("Error while setting other args %r:%r", k, v)
            except Exception, e:
                log.exception("Error while gathering args from %r/%r", msg, source)

            e.save()
        finally:
            return True
