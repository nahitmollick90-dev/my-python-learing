#Port Scanner Audit (Break & continue)
 
open_ports = [80,443, 21 ,22 , 8080 , 23 , 3306]
for item in open_ports:
    if item == 21:
        print(f"[SKIP] Port 21:Insecure protacol")

        continue
    elif item == 23:
        print(f"[CRITCAL] Port 23 detected! ")
        break
    else:
        print(f"[SCANNING] Port: {item}")

        