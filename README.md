# iot_plant_project
By: Mathilda Moström mm224ph

# Project description
I love plants, and especially my own. To keep my beloved friends happy and healthy, I choose for my first IoT project to build a system that keeps track of how moist the solid material is. I also want to keep track of the temperature to indicate how much sunlight they get . So the idea of this project is to be able to collect data from the two sensors (soil humidity and room temperature) and then make the data visible in Ubidots. Data can then be used to gain a better understanding of the specific needs of the different plants.

Estimated time for this project is based on previous experience about 3 hours. It is installation and installation of different programs that takes time, the project itself is really beginner friendly.

# Objective
From my great interest in plants and data, it became an obvious *choice* to build something before this course that helps me keep track of my plants' needs. After looking around on different pages for different sensors and getting some inspiration from projects that were done last year, I chose to collect data on how moist the plants are and what temperature they are in. The *purpose* is to become better at taking care of the plants and that identify different needs they have, which ones can handle higher / lower temperatures, and how quickly they become dehydrated. Tracking this will give me better *insights* into how I best take care of my plants.

# Material
I bought all my material from Electrokit. 
### LoPy4 and sensors bundle (LNU-1DT305)
This is a kit which is developed for this course and which contains most of what you need to get started with similar projects, then you can buy more sensors depending on what you want to do, the kit contains:
– LoPy4 with headers
– Expansion board
– Antennae
– Micro USB cable
– Jumper wire
– Breadboard
– 10 x Resistor1 kohm
– 10 x Resistor 10 kohm
– 10 x Resistor 330 ohm
– 10 x Resistor 560 ohm
– 5 x LED red
– 5 x LED orange
– 5 x LED green
– 2 x LDR
– Tilt switch
– Temperature sensor MCP9700
– Hall-effect sensor TLV49645
– Magnet

For this project I have used the LoPy4, the expansion board, the antennae, the micro USB cable and the temperature sensor MCP9700. 

### Soil hygrometer module (41015738)
This is a sensor for measuring the moisture level in soil. The sensor works by passing a current from one leg to the other, if the resistance is high it means that the soil is dry and vice versa.


| Item       | Quantity | Price   | Link |
| :----------: | :--: | :----: | :------:|
| LoPy4 and sensors bundle | 1 | 949.00 kr | https://www.electrokit.com/produkt/lnu-1dt305-tillampad-iot-lopy4-and-sensors-bundle/ |
| Soil moisture sensor | 1 | 29.00 kr | https://www.electrokit.com/produkt/jordfuktighetssensor/ |

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
