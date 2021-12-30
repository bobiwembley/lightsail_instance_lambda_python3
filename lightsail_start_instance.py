import json
from sre_parse import State
import boto3

from botocore.exceptions import ClientError

client = boto3.client('lightsail')
list_k3s_server = ['k3s-manager', 'k3s-worker1', 'k3s-worker2', 'k3s-worker3']

#### List instance state  
for server in list_k3s_server:
    try:
        dic ={0 :'state',
              1 :'code',
              2 :'name'}
  
        state_server = json.dumps(client.get_instance_state(instanceName=server), indent=2, sort_keys=True, default=str)

        print(state_server)
# start instance if state is stopped
    except client.exceptions.NotFoundException:
        print (client.exceptions.NotFoundException)






