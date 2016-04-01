# ansible-cisco

This is a collection of Ansible modules for cisco IOS routers. There are two modules: one to gather some usefull facts for cisco IOS routers and another to execute a list of commands from a file. The cisco_exec_commands module doesn't replace the ansible core module that do the same (http://docs.ansible.com/ansible/list_of_network_modules.html#ios), it's only another usefull module that can be run in version 1.7.0.

The facts gathered can be used as inputs to other modules or used in templates to create documentation used for inventorying, assessments, etc.

In this repository there is a playbook example that adds a VRF and some interfaces in the VRF. In order to do that, the playbook has the following tasks:
- Search in BGP Reflectors router of de network if the RD you want to configure already exists.
- Search in BRAS if exists a VRF with the same name.
- Adds the new VRF, some interfaces, and place the interfaces in the VRF.
