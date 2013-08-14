from django.db import models
from couchdbkit.ext.django.schema import *
import datetime

class RawEvent(Document):
    """ Something that happened """
    directions=(
                ('c2s','Client To Server'),
                ('s2c','Server To Client'),
                ('other', 'Unknown'),
                )
    direction = StringProperty(
                               required = True,
                               choices = directions,
                               verbose_name = "Message Direction",
                               )
    eventType = IntegerProperty(
                                required = True,
                                verbose_name = "Event Type ID",
                                )
    eventTypeName = StringProperty(
                                required = False,
                                verbose_name = "Event Type Name",
                                default = None,
                                )
    rawBytes = StringProperty(
                              required = True,
                              default = '',
                              verbose_name = "Raw Data",
                              )
    occured = DateTimeProperty(
                             required = True,
                             verbose_name = "Event Date/Time",
                             )
    otherAttrs = DictProperty(
                              verbose_name = "Other Props",
                              required = True,
                              default = {},
                              )
    # Entry info tracking - Pretty useless
    created = DateTimeProperty(
                             auto_now_add = True,
                             required = True,
                             verbose_name = "Created",
                             )
    modified = DateTimeProperty(
                             auto_now = True,
                             required = True,
                             verbose_name = "Last Modified",
                             )
    
