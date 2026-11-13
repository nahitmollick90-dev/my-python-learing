port = int(input("Enter Target port:"))
if port == 22 :
    print(f"[ACCESS GRANTED] SSH Service Initialized")
elif   port == 80 or port == 443 :
    print(f"[ACCESS GRANTED] Web Protocol Initialized")
else :
    print(f"[ACCESS DENIED] Unauthorized Port Blocked")