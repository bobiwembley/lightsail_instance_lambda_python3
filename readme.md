# boto3 light script to automate some  works on lightsail AWS infrastructure

this repository code are separated from AWS lightsail **terraform** k3s
1. because you can find quick script to adapt start/stop lightsail instances  from your local computer  or laptop
2. You can use  **lambda**  https://aws.amazon.com/fr/lambda/features/ to put this script  and automate start or shutdown some services and reduce coast computing on **AWS cloud Provider** 

To automate some works on **AWS lightsail**, like to boot-up a k3s cluster, please find two scripts to push on lambda in a python fonction.

### Cost of k3s AWS boto3 & Lambda alliance Vs cluster vs EKS cluster 
EKS (**E**lastic **K**ubernetes **S**ervices) have a minimal coast of 70 US $/month for one node. In case of infrastructure  personnal Development, you can switch on **lightsail** AWS **offers**
You can use the following  url
https://github.com/bobiwembley/lightsail-k3s-cluster

When you use lightsail, you  have a reduced and simplify infrastructure with instance from lightsail AWS offers.

### From your laptop and you just need to start instances on lightsail AWS

#### **Prerequisite**
You have to aws cli configure on you laptop, a personnal access Token and your user IAM have the right policy to access to lightsail.

````
aws configure
````
**lightsail_start_instance.py** 


````
> python3 lightsail_start_instance.py
server: k3s-manager are started
server: k3s-worker1 are started
server: k3s-worker2 are started
server: k3s-worker3 are started
````

````
> python3 lightsail_start_instance.py
server: k3s-manager are currently running or pending
server: k3s-worker1 are currently running or pending
server: k3s-worker2 are currently running or pending
server: k3s-worker3 are currently running or pending
````
**lightsail_stop_instance.py**
````
> python3 lightsail_stop_instance.py
server: k3s-manager are stopped
server: k3s-worker1 are stopped
server: k3s-worker2 are stopped
server: k3s-worker3 are stopped
````

````
> python3 lightsail_stop_instance.py
server: k3s-manager are going to stop
server: k3s-worker1 are going to stop
server: k3s-worker2 are going to stop
server: k3s-worker3 are going to stop
````

