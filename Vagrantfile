# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "rockylinux/9"
  config.vm.box_version = "5.0.0"

  # Servidor Bastión (DNS, DHCP y adm)
  config.vm.define "bastion", primary: true do |bastion|
    bastion.vm.hostname = "bastion"
    bastion.vm.network "private_network", ip: "192.168.10.10", virtualbox__intnet: "lab_net"

    bastion.vm.provider "virtualbox" do |vb|
      vb.name = "bastion"
      vb.memory = "1024"
      vb.cpus = 1
    end
  end

  # Nodo Master (Control Plane)
  config.vm.define "master" do |master|
    master.vm.hostname = "master"
    master.vm.network "private_network", type: "dhcp", virtualbox__intnet: "lab_net", mac: "080027112233"

    master.vm.provider "virtualbox" do |vb|
      vb.name = "master"
      vb.memory = "2048"
      vb.cpus = 2
    end
  end

  # Nodo Worker (Cargas de trabajo)
  config.vm.define "worker" do |worker|
    worker.vm.hostname = "worker"
    worker.vm.network "private_network", type: "dhcp", virtualbox__intnet: "lab_net", mac: "080027112244"

    worker.vm.provider "virtualbox" do |vb|
      vb.name = "worker"
      vb.memory = "2048"
      vb.cpus = 1
    end

    # Provisionamiento automático con Ansible al terminar de levantar las máquinas
    worker.vm.provision "ansible" do |ansible|
      ansible.playbook = "site.yml"
      ansible.limit = "all"
      ansible.groups = {
        "infra_servers" => ["bastion"],
        "kubernetes_master" => ["master"],
        "kubernetes_worker" => ["worker"],
        "kubernetes_cluster" => ["master", "worker"]
      }
    end
  end
end
