#Network latency moniter: checks ping speed and print connection health status based on thresholds

ping = 45
if ping <= 30 :
    print("Excallent")
elif ping <= 80:
    print("Good")
elif ping <= 150 :
    print("lagging")
else :
    print("connection lost ")