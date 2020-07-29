# https://www.kernel.org/doc/Documentation/thermal/sysfs-api.txt

def readCPUThermalZoneTemperature(CPUthermalZoneNumber):
  try:
    with open("/sys/class/thermal/thermal_zone%d/temp" % CPUthermalZoneNumber) as f:
      temperatureMilliCelsius = int(f.read())
      if temperatureMilliCelsius==0:
        temperatureMilliCelsius = None # an existing thermal_zone directory with a non implemented sensor returns a reading of 0, don't ask me why
  except FileNotFoundError:
    temperatureMilliCelsius = None
    return temperatureMilliCelsius

  return temperatureMilliCelsius

for CPUthermalZoneNumber in range(0,20):
    temperatureMilliCelsius = readCPUThermalZoneTemperature(CPUthermalZoneNumber)
    if temperatureMilliCelsius:
      print("Current temperature of CPU thermal_zone %d : %4.1f °C" % (CPUthermalZoneNumber,temperatureMilliCelsius/1000))
    else:
      #print("No valid Reading for thermal_zone %d" % i)
      pass