Journal

I am building this custom speaker because I want to upgrade the standard Hack Club Static kit by adding a MH-M18 bluetooth module. I want it to be a Bluetooth speaker for my bedroom, but I also want to keep the actual over-the-air FM radio chip from the original kit.



## 12 September 2026 - Dropping Parts into KiCad & Checking Layout

Today I started actually placing the main component blocks onto my KiCad schematic screen to match the original setup before doing the ESP32 swap. 

I managed to place the original XIAO chip block, the RDA5807 radio chip, the headphone jack socket, and the TDA2822 amplifier block with some basic resistors and grounds connected. I'm taking it slow and trying to make sure the pins match up with what the guide shows. 

I ran into a bit of confusion with the capacitors because I though I had to literally find a 10uF capacitor not just renaming it. Next step is clearing up those capacitor values and finishing off the rest of the schematic.

![Screenshot of my early KiCad schematic progress](assets/11.9.png)

### Time Spent: 2 Hours

## 13 September 2026 - Setting Up GitHub

Today I worked on getting my project files backed up on GitHub using GitHub Desktop. 

I ran into some folder issues at first because the app was tracking unrelated programming files. Now everything is organized cleanly and saved online.

### Time Spent: 1.5 Hours

## 14 September 2026 - Integrating the Bluetooth Module & Audio Mixing

Today I worked on adding the MH-M18 Bluetooth module to my schematic to get audio from my phone.

I downloaded a custom library from GitHub so the component shows up as a proper symbol and footprint instead of just generic pins. I wired up its 5V power and ground lines, and then tackled the audio mixing circuit. 

With some AI help, I added a 1kΩ resistor to every single audio output line coming from both the Bluetooth module and the FM radio chip. This means `R_MIX` and `L_MIX` connect with any issues, preventing the 2 different paths (Bluetooth and the radio chips) from screwing each other over.

![Screenshot of my early KiCad schematic progress](assets/14.9.png)


### Time Spent: 2 Hours








