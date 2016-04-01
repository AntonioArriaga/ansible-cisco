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
module: cisco_serial
short_description: Execute all lines from a file in a Cisco IOS router via serial console
description:
    - Execute all lines from a file in a Cisco IOS router via serial console.
    - If a line execution return an error, the module will fail.
author: Antonio Arriaga Diaz
version_added: 1.0
options:
     port=dict(required=False),
     baudrate=dict(required=False),
     parity=dict(required=False),
     stopbits=dict(required=False),
     bytesize=dict(required=False),
     timeout=dict(required=False),
  port:
    description:
      - Physical serial port
    required: false
    default: "/dev/ttyS0"
  baudrate:
    description:
      - Console baud rate
    required: false
    default: 9600
  parity:
    description:
      - Console parity
    required: false
    default: "N"
  stopbits:
    description:
      - Console stop bits
    required: false
    default: 1
  bytesize:
    description:
      - Console byte syze
    required: false
    default: 8
  timeout:
    description:
      - Console timeout
    required: false
    default: 8
  command_file:
    description:
      - File that contains all Cisco commands
    required: true
'''

EXAMPLES = '''
- cisco_serial: "port="/dev/ttyS1 baudrate=18400 command_file="/path/to/file/commandFile"
'''

import serial
import time
from ansible.module_utils.basic import *


def read_output (serial_port):
  output = ""
  time.sleep(1)
  bytes_to_read = serial_port.inWaiting()

  while bytes_to_read > 0:
    output += serial_port.read(bytes_to_read)

    time.sleep(1)
    bytes_to_read = serial_port.inWaiting()

  return output


def execute_command (serial_port, command):
  return_value = [True,""]
  serial_port.write(command + "\r")
  output = read_output(serial_port)
  if "% Invalid" in output:
    return_value = [False,output]
  return return_value


def main():

  module = AnsibleModule(
   argument_spec=dict(
     port=dict(required=False),
     baudrate=dict(required=False),
     parity=dict(required=False),
     stopbits=dict(required=False),
     bytesize=dict(required=False),
     timeout=dict(required=False),
     command_file=dict(required=True)
     )
  )

  command_file = module.params['command_file']
  if module.params['port']:
    port = module.params['port']
  else:
    port = '/dev/ttyS0'
  if module.params['baudrate']:
    baudrate = module.params['baudrate']
  else:
    baudrate = 9600
  if module.params['parity']:
    parity = module.params['parity']
  else:
    parity = "N"
  if module.params['stopbits']:
    stopbits = module.params['stopbits']
  else:
    stopbits = 1
  if module.params['bytesize']:
    bytesize = module.params['bytesize']
  else:
    bytesize = 8
  if module.params['timeout']:
    timeout = module.params['timeout']
  else:
    timeout = 8

  ser = serial.Serial(port=port, baudrate=baudrate, parity=parity, stopbits=stopbits, bytesize=bytesize, timeout=timeout)

  if not ser.isOpen():
    module.fail_json(msg="Serial port cannot be opened")

# Single return for initiate the cisco console
  execute_command(ser,"")
# Entering enable mode
  execute_command(ser,"enable")
# Avoid the inconvenient "--More--" of cisco paging
  execute_command(ser,"terminal length 0")

  with open(command_file) as f:
    command_list = f.readlines()

  for command in command_list:
    output = execute_command(ser,command)
    if not output[0]:
      module.fail_json(msg=output[1])

  execute_command(ser,"exit")

  ser.close()
  module.exit_json(changed=True)

main()
