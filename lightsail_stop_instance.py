import json
import boto3

from botocore.exceptions import ClientError

client = boto3.client('lightsail')
list_k3s_server = ['k3s-manager', 'k3s-worker1', 'k3s-worker2', 'k3s-worker3']

#### List instance state  
for server in list_k3s_server:
    try:
        state_server =  json.loads(json.dumps(client.get_instance_state(instanceName=server)))
        response = state_server['state']['name']
        #### starting server if are stopped
        if response == 'running':
            client.stop_instance(instanceName=server)
            print('server:' , server,'are going to stop')
        else:
           print('server:', server, 'are stopped')

    except client.exceptions.NotFoundException:
        print (client.exceptions.NotFoundException)






