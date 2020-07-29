# https://www.kernel.org/doc/Documentation/thermal/sysfs-api.txt

def readThermalZoneTemperature(x, clip=True):
  try:
    with open("/sys/class/thermal/thermal_zone%d/temp" % x) as f:
      temperatureMilliCelsius = int(f.read())
      if clip:
        temperatureMilliCelsius = max(0, temperatureMilliCelsius)
  except FileNotFoundError:
    return 0

  return temperatureMilliCelsius

for i in range(0,20):
    temperatureMilliCelsius = readThermalZoneTemperature(i)
    if temperatureMilliCelsius>0:
      print("Current temperature of thermal_zone %d : %4.1f °C" % (i,readThermalZoneTemperature(i)/1000))
    else:
      print("No valid Reading for thermal_zone %d" % i)