# lab
just a lab space to test things 

## five VMs can be build using this Vagrantfile
1. Ubuntu 18.04 server (will be a desktop in the future)
1. CentOS 7 server
1. Ubuntu 18.04 server
1. Amazon Linux 2 server
1. Amazon Linux 2 server

## the following are all valid vagrant commands to start VMs in virtualbox:

(1) two VMs will start
```
vagrant up desktop server3
```
(2) three VMs will start
```
vagrant up desktop server1 server3
```
(3) all five VMs will start
```
vagrant up
```

## using vagrant ssh

the following have been tested
```
vagrant ssh desktop
```
```
vagrant ssh server1
```
```
vagrant ssh server2
```
```
vagrant ssh server3
```
```
vagrant ssh server4
```

## test shell scripts

use the following shell scripts to test ansible functionality
```
runWithAllParametersAndWrongAnsibleVersion.sh
```
```
runWithAllParametersAndWrongAnsibleVersion.sh
```



## shared directory
a directory is shared with the VMs and host at /vagrant
