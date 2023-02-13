from django.shortcuts import render
import time
import os

def ping_page(request):
    # with open(".\reservationip_list.txt") as file:
    #     park = file.read()
    #     park = park.splitlines()
    #     print(" {park}  \n")
        # ping for each ip in the file
    while True:
        response = os.popen(f"ping 104.160.143.212  ").read()
        # Pinging each IP address 4 times
        print(response)
        #saving some ping output details to output file

        # print output file to screen
    # with open("ip_output.txt") as file:
    #     output = file.read()
    #     f.close()
    #     print(output)
    # with open("ip_output.txt","w") as file:    
    #     pass
        time.sleep(10)

    
        return render (request, "network/index.html" )