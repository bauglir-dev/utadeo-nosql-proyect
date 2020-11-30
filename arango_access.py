# -*- coding: utf-8 -*-

!pip3 install pyarango

import json
import requests
import sys

from pyArango.connection import Connection
from pyArango.collection import Collection, Edges, Field
from pyArango.graph import Graph, EdgeDefinition
from pyArango.collection import BulkOperation as BulkOperation


con= Connection(arangoURL='https://3838e90db39f.arangodb.cloud:8529', username='root', password='j0fiXJqRTKCCb9lYZUV2')
con.getDatabasesURL()
#db= con.createDatabase('_system')
db=con['_system']
db['customers']