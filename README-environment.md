# Stackstorm Environment

The purpose of this document is to provide insight into setting up a local Stackstorm environment for __Pack__ development.

This method of setup is based on [VirtualBox] (https://www.virtualbox.org/wiki/Downloads) and [Vagrant] (https://www.vagrantup.com/).  At the time of this writing, the following versions worked successfully.  _VirtualBox 5.0.20_ and _Vagrant 1.8.1_.

#### Clone the Stackstorm Vagrant repo and start it
```
git clone https://github.com/StackStorm/st2vagrant.git
cd st2vagrant
vagrant up
```

#### SSH into Stackstorm VirtualBox
After successfully creating and starting a new Stackstorm VirtualBox, you will need to SSH into it in order to run Stackstorm actions or commands.

```
vagrant ssh
```

In order to deploy your custom pack, you will need to copy your pack to _/opt/stackstorm/packs_ within the VirtualBox.

#### Load Pack
After copying the pack to _/opt/stackstorm/packs_, run the following commands to load your new pack.

```
sudo st2ctl reload --register-actions

st2 run packs.setup_virtualenv packs=teamcity
```