#! /usr/bin/python

# Copyright 2016 Antonio Arriaga Diaz <antonio.arriaga.diaz@gmail.com >
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

DOCUMENTATION = '''
---
module: cisco_gather_facts
short_description: Get facts of a Cisco IOS router
description:
    - Get facts of a Cisco IOS router
author: Antonio Arriaga Diaz
version_added: 1.0
options:
  hostname:
    description:
      - Hostame or IP address of router.
    required: true
  username:
    description:
      - Username used to login to the router
    required: true
  password:
    description:
      - Password used to login to the router
    required: true
  enable:
    description:
      - Enable password used to enable to the router
    required: true
'''

EXAMPLES = '''
- cisco_gather_facts: hostname=10.1.1.100 username=admin password=123456 enable=987654
'''


RETURN = '''
cisco_gather_facts:
    description: Dictionary of facts
    returned: always
    type: dictionary
    sample:
      "cisco": {
        "bgp": {
          "rd": [
            "65010:100",
            "65010:101",
            "65010:102",
            "65010:103"
          ],
          "AS": "65010",
          "identifier": "172.16.16.183",
          "neighbor": {
            "10.1.1.1": {
              "AS": "65010",
              "version": "4",
              "neighbor": "10.1.1.1"
            },
            "10.1.1.2": {
              "AS": "65010",
              "version": "4",
              "neighbor": "10.1.1.2"
            }
          }
        },
        "interfaces": {
          "NVI0": {
            "status": "up/up",
            "hardware": "NVI",
            "name": "NVI0",
            "encapsulation": "UNKNOWN",
            "mtu": "1514"
          },
          "Loopback101": {
            "status": "up/up",
            "name": "Loopback101",
            "IP": "10.0.0.1",
            "mask": "255.255.255.255",
            "mtu": "1514",
            "hardware": "Loopback",
            "encapsulation": "LOOPBACK"
          },
          "GigabitEthernet0/2": {
            "status": "down/down",
            "name": "GigabitEthernet0/2",
            "mtu": "1500",
            "hardware": "BCM1250",
            "mac": "0016.9c98.3c19",
            "encapsulation": "ARPA"
          },
          "Virtual-Access2": {
            "status": "down/down",
            "hardware": "Virtual",
            "name": "Virtual-Access2",
            "encapsulation": "PPP",
            "mtu": "1500"
          },
          "Virtual-Access1": {
            "status": "up/up",
            "hardware": "Virtual",
            "name": "Virtual-Access1",
            "encapsulation": "PPP",
            "mtu": "1492"
          },
          "GigabitEthernet0/0.103": {
            "status": "up/up",
            "name": "GigabitEthernet0/0.103",
            "IP": "172.16.1.103",
            "mask": "255.255.255.0",
            "vlanid": "103",
            "mtu": "1500",
            "hardware": "BCM1250",
            "mac": "0016.9c98.3c1b",
            "encapsulation": "802.1Q Virtual LAN"
          },
          "GigabitEthernet0/1": {
            "status": "down/down",
            "name": "GigabitEthernet0/1",
            "mtu": "1500",
            "hardware": "BCM1250",
            "mac": "0016.9c98.3c1a",
            "encapsulation": "ARPA"
          },
          "GigabitEthernet0/0.100": {
            "status": "up/up",
            "name": "GigabitEthernet0/0.100",
            "IP": "172.16.1.100",
            "mask": "255.255.255.0",
            "vlanid": "100",
            "mtu": "1500",
            "hardware": "BCM1250",
            "mac": "0016.9c98.3c1b",
            "encapsulation": "802.1Q Virtual LAN"
          },
          "GigabitEthernet0/0.101": {
            "status": "up/up",
            "name": "GigabitEthernet0/0.101",
            "IP": "172.16.1.101",
            "mask": "255.255.255.0",
            "vlanid": "101",
            "mtu": "1500",
            "hardware": "BCM1250",
            "mac": "0016.9c98.3c1b",
            "encapsulation": "802.1Q Virtual LAN"
          },
          "GigabitEthernet0/0.102": {
            "status": "up/up",
            "name": "GigabitEthernet0/0.102",
            "IP": "172.16.1.102",
            "mask": "255.255.255.0",
            "vlanid": "102",
            "mtu": "1500",
            "hardware": "BCM1250",
            "mac": "0016.9c98.3c1b",
            "encapsulation": "802.1Q Virtual LAN"
          },
          "GigabitEthernet0/0": {
            "status": "up/up",
            "name": "GigabitEthernet0/0",
            "IP": "172.16.16.183",
            "mask": "255.255.255.0",
            "vlanid": "1",
            "mtu": "1500",
            "hardware": "BCM1250",
            "mac": "0016.9c98.3c1b",
            "encapsulation": "802.1Q Virtual LAN"
          },
          "Virtual-Template1": {
            "status": "down/down",
            "hardware": "Virtual",
            "name": "Virtual-Template1",
            "encapsulation": "PPP",
            "mtu": "1500"
          },
          "Loopback102": {
            "status": "up/up",
            "name": "Loopback102",
            "IP": "10.0.0.1",
            "mask": "255.255.255.255",
            "mtu": "1514",
            "hardware": "Loopback",
            "encapsulation": "LOOPBACK"
          },
          "Loopback100": {
            "status": "up/up",
            "name": "Loopback100",
            "IP": "10.0.0.1",
            "mask": "255.255.255.255",
            "mtu": "1514",
            "hardware": "Loopback",
            "encapsulation": "LOOPBACK"
          },
          "Virtual-Template2": {
            "status": "down/down",
            "hardware": "Virtual",
            "name": "Virtual-Template2",
            "encapsulation": "PPP",
            "mtu": "1500"
          },
          "Loopback0": {
            "status": "up/up",
            "name": "Loopback0",
            "IP": "10.0.0.1",
            "mask": "255.255.255.255",
            "mtu": "1514",
            "hardware": "Loopback",
            "encapsulation": "LOOPBACK"
          },
          "Loopback103": {
            "status": "up/up",
            "name": "Loopback103",
            "IP": "10.0.0.1",
            "mask": "255.255.255.255",
            "mtu": "1514",
            "hardware": "Loopback",
            "encapsulation": "LOOPBACK"
          }
        },
        "version": {
          "image": "c7301-adventerprisek9-mz.124-15.T13.bin"
        },
        "hostname": "CISCOROUTER",
        "vrf": {
          "BLUE": {
            "rd": "65010:101",
            "interfaces": [
              "Lo101",
              "Gi0/0.101"
            ],
            "name": "BLUE"
          },
          "GREEN": {
            "rd": "65010:102",
            "interfaces": [
              "Lo102",
              "Gi0/0.102"
            ],
            "name": "GREEN"
          },
          "YELLOW": {
            "rd": "65010:103",
            "interfaces": [
              "Lo103",
              "Gi0/0.103"
            ],
            "name": "YELLOW"
          },
          "RED": {
            "rd": "65010:100",
            "interfaces": [
              "Lo100",
              "Gi0/0.100"
            ],
            "name": "RED"
          }
        }
      }
'''

import sys
import string

from netlib.conn_type import SSH
from netaddr import *
from ansible.module_utils.basic import *


class ciscoRouter(object):
  def __init__(self,
               username='admin',
               password='123',
               enable='123',
               hostname='192.168.0.1'):

    self.username = username
    self.password = password
    self.enable = enable
    self.hostname = hostname

  def interfaceBlockManipulate(self, interfaceBlock):
    interface = {}
    for line in interfaceBlock:
      if "line protocol is" in line:
        interface['name'] = line[:line.find(" ")]
        firstStatus = len(interface['name'])+4
        comma = line.find(",")
        interface['status'] = string.strip(line[firstStatus:comma] + "/" + line[comma+19:-1])
      if "Hardware is " in line:
        interface['hardware'] = line[14:line.find(" ",14)]
      if "Internet address is" in line:
        ip = IPNetwork(line[22:-1])
        interface['IP'] = str(ip.ip)
        interface['mask'] = str(ip.netmask)
      if "MTU" in line:
        interface['mtu'] = line[6:line.find(" ",6)]
      if "Internal MAC" in line:
        macBegin = line.find("address is")+11
        interface['mac'] = line[macBegin:macBegin+14]
      if "Encapsulation" in line:
        interface['encapsulation'] = line[16:line.find(",")]
      if "Vlan ID " in line:
        vlanBegin = line.find("Vlan ID")+9
        interface['vlanid'] = line[vlanBegin:line.find(".",vlanBegin)]


    return interface


  def vrfBlockManipulate(self, vrfBlock):
    vrf = {}
    vrf['name'] = vrfBlock[0][2:vrfBlock[0].find(" ",3)]
    vrf['rd'] = vrfBlock[0][35:vrfBlock[0].find(" ",35)]
    vrf['interfaces'] = []
    for line in vrfBlock:
       vrf['interfaces'].append(line[55:-1])

    return vrf


  def facts(self):

    ssh = SSH(self.hostname, self.username, self.password)
    ssh.connect()
    ssh.set_enable(self.enable)
    ssh.command("terminal length 0")


    # GET BGP Data
    bgp = {}
    bgpReport = string.split(ssh.command("show ip bgp summary"),'\n')
    bgpReport.pop()

    comma = bgpReport[1].find(",")
    bgp['identifier']=bgpReport[1][22:comma]
    bgp['AS']=bgpReport[1][comma+18:-1]
    bgp['neighbor'] = {}
    bgp['rd'] = []

    counter = 1
    numLines = len(bgpReport)
    while counter < numLines:
      line = bgpReport[counter]
      counter += 1
      if line[0:8] == "Neighbor":
        break

    while counter < numLines:
      line = bgpReport[counter]
      neighbor = {}
      neighbor['neighbor'] = line[:line.find(" ")]
      neighbor['version'] = line[16:line.find(" ",16)]
      neighbor['AS'] = line[18:line.find(" ",18)]
      bgp['neighbor'][neighbor['neighbor']] = neighbor
      counter += 1

    bgpReport = string.split(ssh.command("show ip bgp vpnv4 all | inc Route Distinguisher"),'\n')
    counter = 1
    numLines = len(bgpReport)

    while True:
      line = bgpReport[counter]
      bgp['rd'].append(line[21:line.find(" ",21)])
      counter += 1
      if counter > numLines -2:
        break

    bgpReport = []



    # GET VERSION
    version = {}
    versionReport = string.split(ssh.command("show version"),'\n')

    for line in versionReport:
      if 'System image' in line:
        version['image']=line[28:-2]

    versionReport = []


    # GET INTERFACES
    interfaces = {}
    interfacesReport = string.split(ssh.command("show interfaces"),'\n')
    interfacesReport.pop()

    counter = 1
    numLines = len(interfacesReport)

    while True:
      line = interfacesReport[counter]
      if line[0] != " ":
        interfaceBlock = []
        interfaceBlock.append(line)
        counter += 1
        while True:
          line = interfacesReport[counter]
          if line[0] == " ":
            interfaceBlock.append(line)
            counter += 1
          else:
            break
          if counter > numLines - 1:
            break
      interface = self.interfaceBlockManipulate(interfaceBlock)
      interfaces[interface['name']] = interface
      if counter > numLines - 1:
        break

    interfacesReport = []

    # GET VRF
    vrf = {}
    vrfReport = string.split(ssh.command("show ip vrf"),'\n')
    vrfReport.pop()

    counter = 2
    numLines = len(vrfReport)

    if numLines > 2:
      line = vrfReport[counter]
    while counter < numLines:
      vrfBlock = []
      vrfBlock.append(line)
      counter += 1
      if counter < numLines:
        line = vrfReport[counter]

        while line[3] == " ":
          vrfBlock.append(line)
          counter += 1
          if counter < numLines:
            line = vrfReport[counter]
          else:
            break
      singleVrf = self.vrfBlockManipulate(vrfBlock)
      vrf[singleVrf['name']] = singleVrf

    vrfReport = []


    # GET HOSTNAME
    hostname = string.split(ssh.command("show run | inc hostname"),'\n')[1][9:-1]


    ssh.command("end")
    ssh.close()

    facts = {}
    facts['version'] = version
    facts['hostname'] = hostname
    facts['interfaces'] = interfaces
    facts['bgp'] = bgp
    facts['vrf'] = vrf
    return facts



def main():

  module = AnsibleModule(
    argument_spec=dict(
      hostname=dict(required=True),
      username=dict(required=True),
      password=dict(required=True),
      enable=dict(required=True),
      )
  )


  hostname = module.params['hostname']
  username = module.params['username']
  password = module.params['password']
  enable = module.params['enable']
  changed = False
  commandResult = False
  msg = ""


  device = ciscoRouter(hostname=hostname,
                       username=username,
                       password=password,
                       enable=enable)

  facts = device.facts()

#############################################
# Dump
#############################################
#  print json.dumps(facts, indent=2)

  module.exit_json(ansible_facts=dict(cisco=facts))

main()
