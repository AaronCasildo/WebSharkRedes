# TCPDump Cheatsheet 📡

A quick reference guide for tcpdump commands and filters.

---

## Basic Commands

### 1. List Available Network Interfaces

```bash
tcpdump -D
```

### 2. Capture Packets and Save to File

**Syntax:**
```bash
tcpdump -c <packet_count> -w <output_file.pcap>
```

**Example:** Capture 100 packets and save to `capture.pcap`
```bash
tcpdump -c 100 -w capture.pcap
```

### 3. Select a Specific Interface

**Syntax:**
```bash
tcpdump -i <interface_name>
```

**Example:** Capture on `eth0`
```bash
tcpdump -i eth0
```

### 4. Capture Specific Protocol Packets

**Syntax:**
```bash
tcpdump -i <interface> <protocol>
```

**Examples:**
- TCP packets:
  ```bash
  tcpdump -i eth0 tcp
  ```
- UDP packets:
  ```bash
  tcpdump -i eth0 udp
  ```

---

## Display Options

### 5. Display Packets in ASCII Format

```bash
tcpdump -A
```

### 6. Show Timestamp with Date and Time

```bash
tcpdump -tttt
```

### 7. Count Packets in a Capture File

**Save capture:**
```bash
tcpdump -i <interface> -w <file.pcap>
```

**Count packets:**
```bash
tcpdump -r <file.pcap> | wc -l
```

---

## Filtering by IP Address


### 8. Filter by IP Address or Network Range

**Filter by source IP:**
```bash
tcpdump -i <interface> src host <IP>
```

**Filter by destination IP:**
```bash
tcpdump -i <interface> dst host <IP>
```

**Filter by either source or destination IP:**
```bash
tcpdump -i <interface> host <IP>
```

**Filter by network range:**
```bash
tcpdump -i <interface> net <network_range>
```

**Display IPs and ports in numeric format:**
```bash
tcpdump -n
```

---

## Filtering by Port

### 9. Filter by Port Number or Port Range

**Filter by specific port:**
```bash
tcpdump -i <interface> port <port>
```

**Filter by source port:**
```bash
tcpdump -i <interface> src port <port>
```

**Filter by destination port:**
```bash
tcpdump -i <interface> dst port <port>
```

**Filter by port range:**
```bash
tcpdump -i <interface> portrange <start_port>-<end_port>
```

---

## Advanced Filtering

### 10. Combine IP and Port Filters

**Syntax:**
```bash
tcpdump -i <interface> dst host <IP> and port <port>
```

**Example:** Capture traffic destined to `192.168.1.1` on port `23`
```bash
tcpdump -i eth0 dst host 192.168.1.1 and port 23
```

### 11. Filter by Multiple Ports

**Syntax:**
```bash
tcpdump -i <interface> dst host <IP> and (port 80 or port 443)
```

**Example:** Capture HTTP/HTTPS traffic to `192.168.1.1`
```bash
tcpdump -i eth0 dst host 192.168.1.1 and (port 80 or port 443)
```

### 12. Filter by Packet Size

**Capture packets greater than specified size:**
```bash
tcpdump -i <interface> greater <bytes>
```

**Example:** Packets larger than 1000 bytes
```bash
tcpdump -i eth0 greater 1000
```

**Capture packets smaller than specified size:**
```bash
tcpdump -i <interface> less <bytes>
```

---

## Control Commands

**Stop capture:** Press `Ctrl + C`
