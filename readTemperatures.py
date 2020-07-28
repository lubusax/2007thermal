
for i in range(0,9):

  with open("/sys/class/thermal/thermal_zone"+str(i)+"/temp") as file:
    data=file.read()
    print("thermal_zone"+str(i)+" :", int(data)/1000, "°C")