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
module: cisco_exec_commands
short_description: Execute all lines from a file in a Cisco IOS router
description:
    - Execute all lines from a file in a Cisco IOS router.
    - If a line execution return an error, the module will fail.
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
  commandFile:
    description:
      - File that contains all Cisco commands
    required: true
'''

EXAMPLES = '''
- cisco_exec_commands: hostname=10.1.1.100 username=admin password=123456 enable=987654 commandFile="/path/to/file/commandFile"
'''


import sys
import string

from netlib.conn_type import SSH
from ansible.module_utils.basic import *


errmsg = ""

def executeCommand( ssh, command ):
  global errmsg
  prevLine = ""
  returnValue = string.split(ssh.command(command),'\n')
  for singleLine in returnValue:
    if singleLine[:2] == "% ":
      return False
    errmsg = prevLine
    prevLine = singleLine

  return True


def executeCommandList( ssh, commandFile ):
  with open(commandFile) as f:
    commandList = f.readlines()

  for command in commandList:
    if not executeCommand(ssh,command):
      return False

  return True


def main():

  module = AnsibleModule(
    argument_spec=dict(
      hostname=dict(required=True),
      username=dict(required=True),
      password=dict(required=True),
      enable=dict(required=True),
      commandFile=dict(required=True)
      )
  )


  hostname = module.params['hostname']
  username = module.params['username']
  password = module.params['password']
  enable = module.params['enable']
  commandFile = module.params['commandFile']
  changed = False
  commandResult = False
  msg = ""

  ssh = SSH(hostname, username, password)
  ssh.connect()
  ssh.set_enable(enable)

  commandResult=executeCommandList(ssh, commandFile)

  ssh.command("end")
  ssh.close()


  if not commandResult:
     module.fail_json(msg="Command error: \"" + errmsg + "\"")
  else:
    changed = True
    module.exit_json(changed=changed, msg=msg, username=username, password=password, enable=enable)


main()
