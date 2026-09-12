Journal

I am building this custom speaker because I want to upgrade the standard Hack Club Static kit by replacing the XIAO RP2040 with an Espressif ESP32. I want it to be a Bluetooth speaker for my bedroom, but I also want to keep the actual over-the-air FM radio chip from the original kit.



## 12 September 2026 - Dropping Parts into KiCad & Checking Layout

Today I started actually placing the main component blocks onto my KiCad schematic screen to match the original setup before doing the ESP32 swap. 

I managed to place the original XIAO chip block, the RDA5807 radio chip, the headphone jack socket, and the TDA2822 amplifier block with some basic resistors and grounds connected. I'm taking it slow and trying to make sure the pins match up with what the guide shows. 

I ran into a bit of confusion with the capacitors because I though I had to literally find a 10uF capacitor not just renaming it.Next step is clearing up those capacitor values and swapping the XIAO block out for the ESP32.

![Screenshot of my early KiCad schematic progress](assets/11.9.png)

### Time Spent: 2 Hours






