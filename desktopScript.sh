#!/bin/bash -eu

echo "192.168.10.20 w1.plans.MacGuffins.test w1" | sudo tee -a /etc/hosts
echo "192.168.10.21 s1.plans.MacGuffins.test s1" | sudo tee -a /etc/hosts
echo "192.168.10.22 s2.plans.MacGuffins.test s2" | sudo tee -a /etc/hosts
echo "192.168.10.23 s3.plans.MacGuffins.test s3" | sudo tee -a /etc/hosts
echo "192.168.10.24 s4.plans.MacGuffins.test s4" | sudo tee -a /etc/hosts
echo "185.78.197.255 RackMaster.MacGuffins.test ClassMaster.SoFree.Us RackMaster ClassMaster" | sudo tee -a /etc/hosts
ansible --version
