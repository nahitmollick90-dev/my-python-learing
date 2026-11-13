#Firewall traffic analyzer: filter internal IPs and classifes network requests to detect DDoS attacks

network = {
    "192.168.1.10": 25,
    "10.0.0.99":120,
    "127.0.0.1":450,
    "172.16.0.5":85,
    "192.168.0.105":300,
    "10.0.0.1":5,
}
for key , value in network.items():
    if key == "192.168.1.10":
        print(f"[INTERNAL] {key}: Local mach")
    elif value <= 50:
        print(f"[SAFE]{key}: Traffic normal")
    elif 50 < value <=200:
        print(f"[WARNING] {key}: Suapicious traffic")
    elif value >200:
        print(f"[BLOCK] {key}: Potential DDoS attacks")

