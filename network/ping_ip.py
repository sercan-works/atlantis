# import ping3
# import schedule
# import time

# def ping_ip():
#     ip_address = '192.168.1.1'  # Replace with the IP address you want to ping
#     response_time = ping3.ping(ip_address)
#     print(f'Ping to {ip_address} returned {response_time} ms')

# schedule.every(1).minutes.do(ping_ip)

# while True:
#     schedule.run_pending()
#     time.sleep(1)