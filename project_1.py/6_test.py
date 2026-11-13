#pin authentication with 3 attempts lockdwon (for-else & break)

correct_pin = 123456
for i in range(3):
    user = int(input("Enter password :"))
    if correct_pin == user:
        print(f"[SUCCESS] Access Granted Welcome")
        break
    else:
        print(f"[FAILED] Incorrect password try again")
else:
    print(f"[SYSTEM LOCKED] try another day")
