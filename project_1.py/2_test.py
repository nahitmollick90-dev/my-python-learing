#
server_log = {
    "Auth_server":200 ,
    "Payment_Gateway":500,
    "Database":400,
    "web_Frontend":301,
    "API_service": 403,
}
for server , i in server_log.items():
    if i == 200:
        print(f"[OK] {server}:System Healthy")
    elif 300 <= i < 400:
        print(f"[REDIRECT]{server}:Resouce Moved")
    elif 400 <= i < 500:
        print(f"[CLIENT ERROR] {server}:Bad Request")
    else:
        print(f"[SERVER SLOW DWON] Critical Fail")
              
               