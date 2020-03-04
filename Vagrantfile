# -*- mode: ruby -*-
# vi: set ft=ruby :

$timeStamp             = Time.now.strftime("%Y-%m%d-%H%M")

$s1cpus                 = ENV.fetch("S1_VAGRANT_CPUS", "1")
$s2cpus                 = ENV.fetch("S2_VAGRANT_CPUS", "1")
$s3cpus                 = ENV.fetch("S3_VAGRANT_CPUS", "1")
$s4cpus                 = ENV.fetch("S4_VAGRANT_CPUS", "1")
$w1cpus                 = ENV.fetch("W1_VAGRANT_CPUS", "1")

$s1memory               = ENV.fetch("S1_VAGRANT_MEMORY", "512")
$s2memory               = ENV.fetch("S2_VAGRANT_MEMORY", "512")
$s3memory               = ENV.fetch("S3_VAGRANT_MEMORY", "512")
$s4memory               = ENV.fetch("S4_VAGRANT_MEMORY", "512")
$w1memory               = ENV.fetch("W1_VAGRANT_MEMORY", "4096")

$s1hostname             = ENV.fetch("S1_VAGRANT_HOSTNAME", "s1.plans.MacGruffins.test")
$s2hostname             = ENV.fetch("S2_VAGRANT_HOSTNAME", "s2.plans.MacGruffins.test")
$s3hostname             = ENV.fetch("S3_VAGRANT_HOSTNAME", "s3.plans.MacGruffins.test")
$s4hostname             = ENV.fetch("S4_VAGRANT_HOSTNAME", "s4.plans.MacGruffins.test")
$w1hostname             = ENV.fetch("W1_VAGRANT_HOSTNAME", "w1.plans.MacGruffins.test")

$s1virtualBoxDescription = ENV.fetch("S1_VAGRANT_VIRTUALBOXDESCRIPTION", "s1 " + $s1hostname + "\nmemory: " + $s1memory + "\ncreated: " + $timeStamp)
$s2virtualBoxDescription = ENV.fetch("S2_VAGRANT_VIRTUALBOXDESCRIPTION", "s2 " + $s2hostname + "\nmemory: " + $s2memory + "\ncreated: " + $timeStamp)
$s3virtualBoxDescription = ENV.fetch("S3_VAGRANT_VIRTUALBOXDESCRIPTION", "s3 " + $s3hostname + "\nmemory: " + $s3memory + "\ncreated: " + $timeStamp)
$s4virtualBoxDescription = ENV.fetch("S4_VAGRANT_VIRTUALBOXDESCRIPTION", "s4 " + $s4hostname + "\nmemory: " + $s4memory + "\ncreated: " + $timeStamp)
$w1virtualBoxDescription = ENV.fetch("W1_VAGRANT_VIRTUALBOXDESCRIPTION", "w1 " + $w1hostname + "\nmemory: " + $w1memory + "\ncreated: " + $timeStamp)

$s1virtualBoxName        = ENV.fetch("S1_VAGRANT_VIRTUALBOXNAME", "s1-" + $timeStamp)
$s2virtualBoxName        = ENV.fetch("S2_VAGRANT_VIRTUALBOXNAME", "s2-" + $timeStamp)
$s3virtualBoxName        = ENV.fetch("S3_VAGRANT_VIRTUALBOXNAME", "s3-" + $timeStamp)
$s4virtualBoxName        = ENV.fetch("S4_VAGRANT_VIRTUALBOXNAME", "s4-" + $timeStamp)
$w1virtualBoxName        = ENV.fetch("W1_VAGRANT_VIRTUALBOXNAME", "w1-" + $timeStamp)


Vagrant.configure("2") do |config|

  config.vm.define "server1" do |subconfig|
    subconfig.vm.box = "geerlingguy/centos7"
    subconfig.vm.hostname = "s1"
    subconfig.vm.network :private_network, ip: "192.168.10.21"
    #subconfig.vm.network :public_network, bridge: 'enp0s8: Intel(R) Ethernet Connection I217-LM', ip: "10.0.2.121"
    subconfig.vm.provider "virtualbox" do |vb|
      vb.customize ["modifyvm", :id, "--memory", $s1memory]
      vb.customize ["modifyvm", :id, "--cpus", $s1cpus]
      vb.customize ["modifyvm", :id, "--description", $s1virtualBoxDescription]
      vb.customize ["modifyvm", :id, "--name", $s1virtualBoxName]
    end
  end
  config.vm.define "server2" do |subconfig|
    subconfig.vm.box = "ubuntu/bionic64"
    subconfig.vm.hostname = "s2"
    subconfig.vm.network :private_network, ip: "192.168.10.22"
    #subconfig.vm.network :public_network, ip: "10.0.2.122"
    subconfig.vm.provider "virtualbox" do |vb|
      vb.customize ["modifyvm", :id, "--memory", $s2memory]
      vb.customize ["modifyvm", :id, "--cpus", $s2cpus]
      vb.customize ["modifyvm", :id, "--description", $s2virtualBoxDescription]
      vb.customize ["modifyvm", :id, "--name", $s2virtualBoxName]
    end
  end
  config.vm.define "server3" do |subconfig|
    subconfig.vm.box = "bento/amazonlinux-2"
    subconfig.vm.hostname = "s3"
    #subconfig.vm.network :private_network, type: "dhcp"
    subconfig.vm.network :private_network, ip: "192.168.10.23"
    #subconfig.vm.network :public_network, ip: "10.0.2.123"
    subconfig.vm.provider "virtualbox" do |vb|
      vb.customize ["modifyvm", :id, "--memory", $s3memory]
      vb.customize ["modifyvm", :id, "--cpus", $s3cpus]
      vb.customize ["modifyvm", :id, "--description", $s3virtualBoxDescription]
      vb.customize ["modifyvm", :id, "--name", $s3virtualBoxName]
    end
  end
  config.vm.define "server4" do |subconfig|
    subconfig.vm.box = "bento/amazonlinux-2"
    subconfig.vm.hostname = "s4"
    subconfig.vm.network :private_network, ip: "192.168.10.24"
    subconfig.vm.provider "virtualbox" do |vb|
      vb.customize ["modifyvm", :id, "--memory", $s4memory]
      vb.customize ["modifyvm", :id, "--cpus", $s4cpus]
      vb.customize ["modifyvm", :id, "--description", $s4virtualBoxDescription]
      vb.customize ["modifyvm", :id, "--name", $s4virtualBoxName]
    end
  end
  config.vm.define "desktop" do |subconfig|
    subconfig.vm.box = "ubuntu/bionic64"
    subconfig.vm.hostname = "w1"
    subconfig.vm.network :private_network, ip: "192.168.10.20"
    #subconfig.vm.network :public_network, bridge: 'en2: Intel(R) I210 Gigabit Network Connection', ip: "10.0.2.120"
    subconfig.vm.provider "virtualbox" do |vb|
      vb.customize ["modifyvm", :id, "--memory", $w1memory]
      vb.customize ["modifyvm", :id, "--cpus", $w1cpus]
      vb.customize ["modifyvm", :id, "--description", $w1virtualBoxDescription]
      vb.customize ["modifyvm", :id, "--name", $w1virtualBoxName]
    end
    # Run Ansible from the VM named Desktop
    config.vm.provision "ansible_local" do |ansible|
      ansible.become = true
      ansible.playbook = "/vagrant/ansible/main.yaml"
    end    
    config.vm.provision "file", source: "~/amzn2/desktopScript.sh", destination: "/home/vagrant/desktopScript.sh"
    config.vm.provision "file", source: "./ansible", destination: "ansible"
    config.vm.provision "shell", path: "desktopScript.sh"
  end
end
