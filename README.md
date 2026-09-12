# Static-Speaker

[![View PCB on KiCanvas](https://hack.club/pcb-badge)](https://kicanvas.org/)
<br>
View PCB on KiCanvas


<a href="">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcToaQhjbTkEk_11nHyIiwJ0Gwq1cWbHfuL8mGZ0rCmdVw&s" width="90" alt="Youtube Demo">
</a>
<br>
View video demo on YouTube
<br>
<br>
<br>
<p align="center">
  <!-- Tall Photos Row -->
  <!-- <img src="assets/Photo_1.jpg" width="35%" alt="Speaker Top Angle" /> -->
  <!-- <img src="assets/Photo_4.jpg" width="35%" alt="Speaker Base" /> -->
</p>
<p align="center">
  <!-- Wide Photos Row -->
  <!-- <img src="assets/Photo_2.jpg" width="35%" alt="Speaker Side Profile" /> -->
</p>
<br>

This is my custom radio combined with a speaker designed for the YSWS Static
I chose this project to upgrade the standard kit by replacing the original microcontroller with an Espressif ESP32, transforming it into a permanent Bluetooth speaker for my bedroom while keeping the physical over-the-air FM radio chip!

## Features:
- Bluetooth audio streaming directly from a phone
- Over-the-air local FM Radio playback
- One physical push-button to switch modes
- Dual analog potentiometers for volume control

## CAD Model:


## PCB


Schematic

![Schematic](assets/Schematic.png)

Layout

![Layout of PCB](assets/Layout.png)

PCB

![3D Viewer](assets/3D_Viewer.gif)



## Firmware Overview


## File structure

There's 3 main folders: Firmware, PCB, and Production. The PCB folder contains .kicad_pcb, .kicad_pro, and .kicad_sch. The Firmware folder contains files for the ESP32 Arduino code. The production folder will have files for the PCB printing.

## BOM (Bill of Materials):
Here should be everything you need to make this speaker
Most things should be what static sends you except the esp32.


- 1x Espressif ESP32 Development Board
- 1x RDA5807FP FM Radio Tuner Chip
- 1x TDA2822 Audio Amplifier Chip
- 2x 10kΩ Potentiometers (Volume Knobs)
- 4x 1kΩ Resistors (for audio line mixing)
- 2x PJ-3020 3.5mm Audio Jacks (Speaker outputs)
- 10uF and 100uF Capacitors
- 2x 8Ω Speakers
- 1x Momentary Push Button (Mode switch)
- PCB

## Software

- Kicad recommended to view the Gerber files or the general `.pcb` `.pro` `.sch` files
- Arduino IDE for programming the ESP32 controller

## Tools:

- Soldering Iron
- Solder

## How to build/replicate
1. Get **everything** that is on the BOM.


2. **Solder** the parts in their specified location using solder and a soldering iron.


3. 


4. 


5. 


6. 


7. 


8. 




## Extra stuff
In Hackpad style -
Hi guys

Bye guys

