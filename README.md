# SDN_ONOS-CLI-promt-app
This application collects and views 4 different information from ONOS controller for software defined network requesting json data, taking commands as inputs-

1. When "topology" is written as a input in the prompt, the app returns the information regarding the Clusters, links and devices.
2. When "device1" or "device2" is entered, it returns the present status of the device, uptime, chassisID, vendor name, HW and SW version, serial no and protocol used
3. When "hsot1" or "host2" is entered, it returns the IP address, MAC address and VLAN ID of the perticular host
4. To collect the realtime information of the data flow, "stats_device1" and "stats_device2" commands are used. This command returns the number of packets, bytes, source and destination addresses etc. of a particular flow entry.

To get all the commands allowed, "help" or "?" can also be used.
To exit cli prompt and stop the program, use "exit".
