# SDN-DDOS Detection and Mitigation Using ML and Statistical Methods

It has been known that Software Defined Networking (SDN) is the future of networking, allowing engineers to reroute networks on the fly. However, it can become vulnerable to Distributed Denial of Service (DDoS). Therefore, I did an analysis and wrote a research paper later on for my Computer Network course final project, which uses software such as OpenFlow protocol, Mininet, Ryu controller, and machine learning models including support vector machine (SVM) and decision tree in order detect DDOS attacks in SDN.

# Configuration and Software Installation

In order to setup the whole platform, the followings are the tools and its restrictedly required versions.
- Ubuntu operating system version 20.04.1 TLS
- Python3 version
- Python2 version
- Open ow Protocol for SDN version 2.13.0
- Ryu Controller version 4.34
- Mininet version 2.2.2
- Iperf version 2.0.13
- Hping3 version

# Simulation Platform Setup

This Section involves the steps and procedure to install all the packages and software required to implement the project.

On your Ubuntu Linux terminal, make sure you hav ethe updated ubuntu OS and linux libraries with pyhton 3.8 and python 2.7 installed. Open terminal and type in the following commands:--sudo apt-get update-sudo apt-get upgrade

***However, make sure that you do not go beyond the python 3.8 version***

- sudo apt install python2
- sudo apt install python

Install Open ow protocal for SDN or OpenVswitch. In the terminal, type in the following commnad:

- sudo apt-get install openvswitch-switch

To install Ryu controller you need to install PIP of python to install python packages, as ryu is a python based controller it has to be installed using PIP. To install PIP and Ryu controller type in these commands in terminal.

- sudo apt install python3-pip
- sudo pip3 install ryu

Mininet is a network simulator and creates virtual network topology for software de ned networks.

- sudo apt-get install mininet

Hping3 is a network packet generator and tra c generator for TCP/IP protocol, mostly used for network testing.

- sudo apt-get install iperf
- sudo apt-get install hping3

Installing the additional python libraries.

- sudo pip3 install numpy
- sudo pip3 install sklearn
