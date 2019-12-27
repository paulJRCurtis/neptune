from __future__  import print_function
import boto3
import os, sys
from gremlin_python import statics
from gremlin_python.structure.graph import Graph
from gremlin_python.process.graph_traversal import __
from gremlin_python.process.strategies import *
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
import requests

CLUSTER_ENDPOINT = os.environ['CLUSTER_ENDPOINT']
CLUSTER_PORT = os.environ['CLUSTER_PORT']

def run_sample_gremlin_websocket():
    print('running sample gremlin websocket code')
    remoteConn = DriverRemoteConnection('ws://' + CLUSTER_ENDPOINT + ":" + CLUSTER_PORT + '/gremlin','g')
    graph = Graph()
    g = graph.traversal().withRemote(remoteConn)
    print(g.V().count().next())
    remoteConn.close()
    
def run_sample_gremlin_http():
    print('running sample gremlin http code')
    URL = 'http://' + CLUSTER_ENDPOINT + ":" + CLUSTER_PORT + '/gremlin'
    r = requests.post(URL,data='{"gremlin":"g.V().count()"}')
    print(r.text)

def lambda_handler(event, context):
    print(event)
    print('hello from lambda handler')

    ## run gremlin query
    if CLUSTER_ENDPOINT and CLUSTER_PORT:
        run_sample_gremlin_websocket()
        run_sample_gremlin_http()
    else:
        print("provide CLUSTER_ENDPOINT and CLUSTER_PORT environment varibles")

    return "done"


