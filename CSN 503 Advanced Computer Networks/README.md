


Simulation and Detection of SYN Flood Attack
============================================

This project is done as part of the course CSN 503 Advanced Computer Networks. We tried to simulate SYN Flood attack on a PC(Target Machine) from another PC acting as an Attacker Machine.


## Tools Used:

#### 1. hping3 - A pentesing tool
#### 2. Wireshark - Packet sniffing tool


Assume *Machine_1* as attacker's machine and *Machine_2* as target machine. Since the wired network in our institute is protected with firewall we simulated the attack by connecting the *Machine_1* to wifi-hotspot of *Machine_2*. Here both the machines used are Ubuntu systems.


## Simulation:

#### 1. Execute socketListen.py in the *Machine_2* to bring a socket to listening state

#### 2. Connect *Machine_1* to *Machine_2*'s hotspot

#### 3. Start capturing the packets in *Machine_1* using wireshark

#### 4. Execute the following command in the terminal of *Machine_1* by replacing "targerIPAddress" with the IP address of *Machine_2* that can be figured out by running 'ifconfig' command in terminal

```
hping3 -V -c 100 -d 120 -S -p 80 --flood ​targerIPAddress
```

#### 5. If one wants to hide the IP address of *Machine_1* by randomizing the source IP addresses, use the following command

```
hping3 -V -c 100 -d 120 -S -p 80 --flood --rand-source ​targerIPAddress
```

#### 6. From the statistics of the packets captured by wireshark one can detect a SYN Flood attack


Please refer the report attached for clearer description of the project.