# iot_plant_project
By: Mathilda Moström mm224ph

# Objective
I love plants, and expecially my own. To keep my beloved friends happy and healthy I choose for my first iot project to build a system that keeps track how moist the solid is and I also want to keep track of the temperature to get an indication of how much sunlight they get. So the ide the of this project is to be able to collect data from the two sensors (soil moisture and room temperature) and then visulize the data in Ubidots. The data can then be used to get a better understanding what specific needs the different plants need.

# Material
I bought all my material from Electrokit.

| Item       | Quantity | Price |
| :----------: | :--: | :----: |
| LoPy4 and sensors bundle | 1 | 949.00 kr |
| Soil moisture sensor | 1 | 29.00 kr |
| Battery 3xAAA with switch and JST-contact | 2 | 58.00 kr |

# Computer setup
The first thing I did was to connect and install the LoPy4 and the extensionboard, connected with a mirco-USB cable. I choose to use Visual Studio Code as editor for this project, download the extension Pymakr. Then close VSC and download the Pycom Device Firmware Updater and follow the installation setup found on: ``` https://docs.pycom.io/pybytes/gettingstarted/ ```

# Putting everything together

# Platform
The data is presented in Ubidots, I choosed this alternitiv since I like the features it provides and that it's free for educational use.

# The code

boot.py is used first to initialise the connection to the LoPy4 and the wifi.

main.py is where I read the data from the sensors and send the data to Ubidots.

# Transmitting the data / connectivity

# Presenting the data

# Finalizing the design
