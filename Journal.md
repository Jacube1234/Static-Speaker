# Journal

I am building this custom speaker because I want to upgrade the standard Hack Club Static kit by adding an MH-M18 Bluetooth module. I want it to be a permanent Bluetooth speaker for my bedroom, but I also want to keep the actual over-the-air FM radio chip from the original kit so I can toggle between wireless streaming and local radio.

## 12 September 2026 - Dropping Parts into KiCad & Checking Layout

Today I started actually placing the main component blocks onto my KiCad schematic screen to match the original setup before modifying it for the Seeed XIAO RP2040 integration. 

I managed to place the original XIAO microcontroller block, the RDA5807 FM radio chip, the 3.5mm jack socket (which acts as our antenna), and the TDA2822 amplifier block, wiring up basic power rails and ground symbols. I’m taking it slow and double-checking pinouts against the official guide to avoid silly mistakes later. 

I ran into a bit of confusion with the capacitors because I wasn't entirely sure at first whether I needed to pick specific physical footprints or just rename the values (like sorting out the 10uF and 100uF caps). Once I figured out the footprint matching, the next step became clearing up those capacitor values and wrapping up the rest of the core schematic blocks.

![Screenshot of my early KiCad schematic progress](assets/11.9.png)

### Time Spent: 2 Hours

---

## 13 September 2026 - Setting Up GitHub

Today I worked on getting my project files properly backed up and organised online using GitHub Desktop. 

I ran into some folder structure issues at first because the desktop app tried to track unrelated temporary cache files and auto-generated editor backups. I had to set up a clean folder hierarchy (`Firmware`, `PCB`, `Production`) and filter out the clutter. Now everything is cleanly organised into folders for the KiCad project files, the Seeed XIAO code, and the future manufacturing outputs.

![Markdown writting](assets/12.9.png)

### Time Spent: 1.5 Hours

---

## 14 September 2026 - Integrating the Bluetooth Module & Audio Mixing

Today I tackled the core modification of the project: adding the MH-M18 Bluetooth audio module into my schematic so I can stream music straight from my phone.

Since the MH-M18 isn't in standard base KiCad libraries, I had to download and link a custom community symbol and footprint so it showed up correctly instead of a generic header. I wired up its 5V power and ground lines, and then tackled the tricky part—combining the audio streams. 

If you just wire two audio outputs together, they'll short each other out and cause major distortion. With some AI guidance, I designed a passive summing network: I added a 1kΩ resistor to every single audio output line coming from both the Bluetooth module and the RDA5807 FM radio chip. This merges them safely into shared `R_MIX` and `L_MIX` lines before hitting the amplifier, ensuring the two source paths don't mess each other up. Since the volume potentiometers and speakers are mounted offboard, I added clean pin headers and connector pads to route the mixed audio out to them.

![Schematic](assets/14.9_Schematic.png)

After that, I started grouping components on the layout editor. I organised them logically from left to right following the natural power and signal flow through the circuit—keeping the amplifier and its power filtering capacitors closely clustered together to minimise noise.

### Time Spent: 2 Hours

---

## 15 September 2026 - Fixing Schematic & Optimising Net Labels

![Schematic](assets/15.9_Schematic.png)

![PCB Layout](assets/15.9_PCB_Layout.png)

Today I cleaned up several power and net label issues. I changed generic VCC labels to an explicit `+5V` net to match the power input requirements and ensure the XIAO gets a clean supply. 

I also adjusted how the MH-M18 Bluetooth module sits on the edge of the board. I wanted to make sure its onboard antenna section hangs slightly off or clear of dense ground pours so the board traces don't block or interfere with the wireless Bluetooth signal.

### Time Spent: 1 Hour

---

## 16 September 2026 - PCB Routing and DRC Clearance

Today was all about refining the physical board layout and clearing errors. 

I re-laid out parts of the board so the Bluetooth module is securely mounted without awkwardly hanging off, making it much easier to design a solid mechanical enclosure around it later. This led to a bunch of Design Rule Check (DRC) errors—mostly track clearance issues and overlapping silkscreen text. Working through them one by one, I carefully routed traces around the audio lines to prevent electrical noise coupling into the amplifier. I also made extra sure the Bluetooth module's antenna region remained entirely clear of ground plane fills and copper traces to protect wireless performance.

### Time Spent: 3 Hours

---

## 17 September 2026 - 3D Viewer Validation

![3D Viewer](assets/3D_viewer.gif)

Today I ran a complete 3D View check to inspect the fully assembled board layout. 

This step is super helpful because it lets you catch physical collisions before spending money on manufacturing. I confirmed clean component seating, verified that the pin headers for the offboard potentiometers, speakers, and push button have enough physical clearance, and checked that everything lines up nicely for a future enclosure fit.

The images below show the final cleaned schematic and layout from yesterday's session that I took today.
![Schematic](assets/17.9_Schematic.png)
![PCB Layout](assets/17.9_PCB_Layout.png)

### Time Spent: 1 Hour

---

## 18 September 2026 - Gerber Exports & CAD Enclosure Modelling

Today I finished preparing the board for production and started designing the physical case. 

For the board export, I configured KiCad's plot settings to generate a clean manufacturing package consisting strictly of copper layers, solder mask, silkscreen, and the board outline (`Edge.Cuts`). 

With the PCB layout locked in, I jumped into CAD (Fusion 360). I imported the 3D model of the board and all major offboard components (speakers, volume pots, and control buttons wired through pin connectors) into a hybrid assembly so I could design a custom, snugly-fitted 3D-printable case around the hardware layout with proper screw standoffs and wire routing paths.

![CAD Model](assets/Fusion_Render.png)

### Time Spent: 1.5 Hours