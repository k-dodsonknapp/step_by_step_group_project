from app.models import db, Supply

def seed_supplies():
    bird_house_supply1 = Supply(
        projectId=1,
        supply="wood",
        amount=6,
    )

    bird_house_supply2 = Supply(
        projectId=1,
        supply="wood glue",
        amount=1,
    )

    bird_house_supply3 = Supply(
        projectId=1,
        supply="shingles",
        amount=20,
    )

    casino_clock_supply1=Supply(
        projectId=2,
        supply="A deck of French-suited playing card (bridge size : around 57 x 89mm)"
    )

    casino_clock_supply2=Supply(
        projectId=2,
        supply="Three 28BYJ-48 stepper motor with driver board comes with"
    )
    casino_clock_supply3=Supply(
        projectId=2,
        supply="Micro computer with 12 or more IO ports. I used M5stamp C3"
    )

    casino_clock_supply4=Supply(
        projectId=2,
        supply="Double sided adhesive tape"
    )

    casino_clock_supply5=Supply(
        projectId=2,
        supply="Some tapping screws"
    )

    casino_clock_supply6=Supply(
        projectId=2,
        supply="zip ties"
    )

    one_board_mug1=Supply(
        projectId=3,
        supply="Pine board or any wood of your choosing."
    )

    one_board_mug2=Supply(
        projectId=3,
        supply="Scroll saw"
    )

    one_board_mug3=Supply(
        projectId=3,
        supply="Wood glue"
    )

    one_board_mug4=Supply(
        projectId=3,
        supply="Wood oil/ conditioner"
    )

    one_board_mug5=Supply(
        projectId=3,
        supply="Dowel pins (if you want to add extra support for the handle)"
    )

    skillet_burger1=Supply(
        projectId=4,
        supply="Large Saute Pan or Cast Iron Skillet with lid"
    )

    skillet_burger2=Supply(
        projectId=4,
        supply="Cutting Board"
    )

    skillet_burger3=Supply(
        projectId=4,
        supply="Knife"
    )

    skillet_burger4=Supply(
        projectId=4,
        supply="Paper Towels"
    )

    skillet_burger5=Supply(
        projectId=4,
        supply="Plate"
    )

    skillet_burger6=Supply(
        projectId=4,
        supply="Tongs"
    )

    james_webb1=Supply(
        projectId=5,
        supply="1220mmx610mmx10mm (HxWxD) MDF"
    )    
    
    james_webb2=Supply(
        projectId=5,
        supply="Golden Hexagon Stickers"
    )

    james_webb3=Supply(
        projectId=5,
        supply="Matte Black Spraypaint"
    )

    james_webb4=Supply(
        projectId=5,
        supply="Clock Mechanism and Large Hands"
    )

    james_webb5=Supply(
        projectId=5,
        supply="Nail, Picture Hook or Hanging Strips"
    )

    james_webb6=Supply(
        projectId=5,
        supply="Matte Black Spraypaint"
    )

    james_webb7=Supply(
        projectId=5,
        supply="Ruler"
    )

    james_webb8=Supply(
        projectId=5,
        supply="Pencil"
    )

    james_webb9=Supply(
        projectId=5,
        supply="Jigsaw"
    )

    james_webb10=Supply(
        projectId=5,
        supply="Power Drill"
    )

    slowmo_bird1=Supply(
        projectId=6,
        supply="Materials"
    )

    slowmo_bird2=Supply(
        projectId=6,
        supply="Bird feeder"
    )

    slowmo_bird3=Supply(
        projectId=6,
        supply="Bird seed"
    )

    slowmo_bird4=Supply(
        projectId=6,
        supply="A long stick"
    )

    slowmo_bird5=Supply(
        projectId=6,
        supply="Camera"
    )

    slowmo_bird6=Supply(
        projectId=6,
        supply="Tripod"
    )

    slowmo_bird7=Supply(
        projectId=6,
        supply="Shutter remote (optional)"
    )

    dragonfly1=Supply(
        projectId=7,
        supply="Autodesk Tinkercad"
    )

    dragonfly2=Supply(
        projectId=7,
        supply="3D printer"
    )

    dragonfly3=Supply(
        projectId=7,
        supply="Metalcast brand color coat spay"
    )

    dragonfly4=Supply(
        projectId=7,
        supply="Knife"
    )

    dragonfly5=Supply(
        projectId=7,
        supply="Acrylic paint (blue, white, black)"
    )

    arcade_stick1=Supply(
        projectId=8,
        supply="Top: 1 1/8 Inch Ikea Butcher block (leftover from another project)",
    )

    arcade_stick2=Supply(
        projectId=8,
        supply="Body: Just some scraps of 3/4-inch pine I had on hand",
    )

    arcade_stick3=Supply(
        projectId=8,
        supply="Mineral oil for treating the wood",
    )

    arcade_stick4=Supply(
        projectId=8,
        supply="Joystick: Sanwa JLF - TP - 8YT Stick 8 Way 5Pin Handle",
    )

    arcade_stick5=Supply(
        projectId=8,
        supply="Buttons: SANWA 6 Piece Original OBSF-30",
    )

    arcade_stick6=Supply(
        projectId=8,
        supply="USB Encoder: Reyann Zero Delay Arcade USB Encoder",
    )

    arcade_stick7=Supply(
        projectId=8,
        supply="USB Port: Neutrik NAUSB-W-B Reversible USB Port",
    )

    arcade_stick8=Supply(
        projectId=8,
        supply="Rubber Feet: Ace Anti-Skid Pads Black Round 1-1/2 in.",
    )

    arcade_stick9=Supply(
        projectId=8,
        supply="USB Cable: Tripp Lite Coiled 10 ft. Cable",
    )

    arcade_stick10=Supply(
        projectId=8,
        supply="Ribbon cable adapter: Female to Female JST XH Adapter",
    )

    minecraft_torch1=Supply(
        projectId=9,
        supply="Brown Dog Gadgets sells kits and supplies, but you don't need to buy anything from us to create paper circuits. (Though if you do it does help support us in creating new projects and resources for teacher and students.) The easiest way to get all of the parts you need is to pick up a Paper Circuits Kit, but if you've already got some conductive tape, coin cell batteries, and LEDs, you can make those supplies work as well.",
    )

    minecraft_torch2=Supply(
        projectId=9,
        supply="""
        PDF Templates (Included!)
        """,
    )

    minecraft_torch3=Supply(
        projectId=9,
        supply="""
        Paper
        """,
    )

    minecraft_torch4=Supply(
        projectId=9,
        supply="""
        10mm Jumbo LEDs
        """,
    )

    minecraft_torch5=Supply(
        projectId=9,
        supply="""
        10mm Jumbo LEDs
        """,
    )

    minecraft_torch6=Supply(
        projectId=9,
        supply="""
        Maker Tape (1/4" Wide)
        """,
    )

    minecraft_torch7=Supply(
        projectId=9,
        supply="""
        CR2032 Battery
        """,
    )

    minecraft_torch8=Supply(
        projectId=9,
        supply="Note: We are using Maker Tape (a nylon tape that is conductive on the top, bottom, and all the way through) because it's the easiest tape to work with when creating paper circuits. Other conductive tapes (copper foil, etc.) are often only conductive on the top surface, so they will not work for some of these techniques, including the 'Tape Loop' we use to connect the battery.",
    )

    giant_match1=Supply(
        projectId=10,
        supply="1/2 inch stick of balsa wood with a square section"
    )

    giant_match2=Supply(
        projectId=10,
        supply="1/3 inch x 1/16 inch balsa wood strips"
    )

    giant_match3=Supply(
        projectId=10,
        supply="Boxes of normally sized matches - one per giant match"
    )

    giant_match4=Supply(
        projectId=10,
        supply="A big bottle of superglue"
    )

    giant_match5=Supply(
        projectId=10,
        supply="A brown marker"
    )

    giant_match6=Supply(
        projectId=10,
        supply="1/16 inch thick cardboard"
    )

    bike_lamp1=Supply(
        projectId=11,
        supply="Kitronik 5V LED lamp kits",
    )

    bike_lamp2=Supply(
        projectId=11,
        supply="On/Off Switch",
    )

    bike_lamp3=Supply(
        projectId=11,
        supply="Micro usb connector",
    )

    bike_lamp4=Supply(
        projectId=11,
        supply="4 x AA Battery holder",
    )

    bike_lamp5=Supply(
        projectId=11,
        supply="",
    )

    bike_lamp6=Supply(
        projectId=11,
        supply="Buck Converter",
    )

    bike_lamp7=Supply(
        projectId=11,
        supply="Fusion 360",
    )

    bike_lamp8=Supply(
        projectId=11,
        supply="3D Printer",
    )

    bike_lamp9=Supply(
        projectId=11,
        supply="1.75mm PLA(Black)",
    )

    bike_lamp10=Supply(
        projectId=11,
        supply="Acrylic off cut",
    )

    bike_lamp11=Supply(
        projectId=11,
        supply="2no 3mm Allen head bolts 6mm long",
    )

    bike_lamp11=Supply(
        projectId=11,
        supply="Hot glue",
    )

    rainbow1=Supply(
        projectId=12,
        supply="Double Axis Diffraction Grating Sheet",
    )

    rainbow2=Supply(
        projectId=12,
        supply="Glue Stick",
    )

    rainbow3=Supply(
        projectId=12,
        supply="Blue Painters Tape - Always use this on your bed and no other tapes as other tapes will leave residue",
    )

    rainbow4=Supply(
        projectId=12,
        supply="Your 3D printing file",
    )

    rainbow5=Supply(
        projectId=12,
        supply="Your printer",
    )

    rainbow6=Supply(
        projectId=12,
        supply="Your printer bed or extra printer bed",
    )

    frankenstein1=Supply(
        projectId=13,
        supply="Gallon size plastic water bottle (The square bottles from the dollar tree are my favorite)",
    )

    frankenstein2=Supply(
        projectId=13,
        supply="A scrap piece of wood",
    )

    frankenstein3=Supply(
        projectId=13,
        supply="Assorted bolts",
    )

    frankenstein4=Supply(
        projectId=13,
        supply="A 6 volt buzzer",
    )

    frankenstein5=Supply(
        projectId=13,
        supply="Wire or alligators wires",
    )

    frankenstein6=Supply(
        projectId=13,
        supply="9 volt battery",
    )

    frankenstein7=Supply(
        projectId=13,
        supply="Aluminum foil",
    )

    frankenstein8=Supply(
        projectId=13,
        supply="Stick glue,Velcro dots, duct tape",
    )

    frankenstein9=Supply(
        projectId=13,
        supply="Tool bench tweezers (Dollar Tree, 4 in a package)",
    )

    frankenstein10=Supply(
        projectId=13,
        supply="Spray paint (green/purple), craft paint (black/white)",
    )

    frankenstein11=Supply(
        projectId=13,
        supply="Battery tester",
    )

    ice_cream1=Supply(
        projectId=14,
        supply="1/4 cup of oil",
    )

    ice_cream2=Supply(
        projectId=14,
        supply="1 cup of chocolate chips",
    )

    ice_cream3=Supply(
        projectId=14,
        supply="6 cones",
    )

    ice_cream4=Supply(
        projectId=14,
        supply="1/2 cup roasted and chopped peanuts",
    )

    ice_cream5=Supply(
        projectId=14,
        supply="1 pint of ice cream",
    )

    hot_chocolate1=Supply(
        projectId=15,
        supply="1 1/2 cups whole milk",
    )

    hot_chocolate2=Supply(
        projectId=15,
        supply="1/2 cup cream",
    )

    hot_chocolate3=Supply(
        projectId=15,
        supply="2 teaspoons powdered sugar",
    )

    hot_chocolate4=Supply(
        projectId=15,
        supply="1/2 teaspoon cinnamon",
    )

    hot_chocolate5=Supply(
        projectId=15,
        supply="1/4 teaspoon nutmeg",
    )

    hot_chocolate6=Supply(
        projectId=15,
        supply="1 cup chocolate chips",
    )

    hot_chocolate7=Supply(
        projectId=15,
        supply="1 cup heavy whipping cream (for serving)",
    )

    cocoa_bombs1=Supply(
        projectId=16,
        supply="2/3 cup Hershey's 100% cocoa powder",
    )

    cocoa_bombs2=Supply(
        projectId=16,
        supply="3 TBSP maple syrup",
    )

    cocoa_bombs3=Supply(
        projectId=16,
        supply="Pinch of salt",
    )

    cocoa_bombs4=Supply(
        projectId=16,
        supply="1 TBSP ground cinnamon",
    )

    cocoa_bombs5=Supply(
        projectId=16,
        supply="2/3 cups milk",
    )

    cocoa_bombs6=Supply(
        projectId=16,
        supply="1 T measuring spoon",
    )

    cocoa_bombs7=Supply(
        projectId=16,
        supply="1/3 c measuring cup",
    )

    cocoa_bombs8=Supply(
        projectId=16,
        supply="Mug",
    )

    cocoa_bombs9=Supply(
        projectId=16,
        supply="Rubber spatula",
    )

    cocoa_bombs10=Supply(
        projectId=16,
        supply="Small bowl",
    )

    blossom1=Supply(
        projectId=17,
        supply="ONE CANDLE JAR",
    )

    blossom2=Supply(
        projectId=17,
        supply="CRAFT FOAM BLOCK",
    )

    blossom3=Supply(
        projectId=17,
        supply="ACRYLIC PAINT (ANTIQUE WHITE, AND BRIGHT MAGENTA)",
    )

    blossom4=Supply(
        projectId=17,
        supply="FLORAL",
    )

    blossom5=Supply(
        projectId=17,
        supply="FLORAL SNIPS",
    )

    blossom6=Supply(
        projectId=17,
        supply="ONE TREE BRANCH",
    )

    blossom7=Supply(
        projectId=17,
        supply="ONE PAINT BRUSH",
    )

    blossom8=Supply(
        projectId=17,
        supply="HOT GLUE",
    )

    blossom9=Supply(
        projectId=17,
        supply="ONE PAINT BRUSH",
    )

    torus1=Supply(
        projectId=18,
        supply="Carboard (you can even use old carboard but news ones are recommended for smoother panting surface)",
    )

    torus2=Supply(
        projectId=18,
        supply="Acrylic paint basics(to give color to each and every peace of the cardboard)",
    )

    torus3=Supply(
        projectId=18,
        supply="Gesso (which is applied FIRST before putting down your favorite color acrylic basic)",
    )

    torus4=Supply(
        projectId=18,
        supply="iPad",
    )

    torus5=Supply(
        projectId=18,
        supply="App called Grid#",
    )

    torus6=Supply(
        projectId=18,
        supply="google docs",
    )

    torus7=Supply(
        projectId=18,
        supply="Carboard scissors",
    )

    torus8=Supply(
        projectId=18,
        supply="Retractable Utility Knife(VERY recommended)",
    )

    torus9=Supply(
        projectId=18,
        supply="Big Cutting matte or some old durable material that will endure the cuts from the Retractable Utility Knife",
    )

    torus10=Supply(
        projectId=18,
        supply="Gummed paper tape",
    )

    bike_mount1=Supply(
        projectId=19,
        supply="Band saw",
    )

    bike_mount2=Supply(
        projectId=19,
        supply="Hand saw",
    )

    bike_mount3=Supply(
        projectId=19,
        supply="Sand paper (Bench top sander is easier for some parts, but not necessary)",
    )

    bike_mount4=Supply(
        projectId=19,
        supply="Table saw",
    )

    bike_mount5=Supply(
        projectId=19,
        supply="Dowels x 12",
    )

    bike_mount6=Supply(
        projectId=19,
        supply="Glue",
    )
    
    bike_mount7=Supply(
        projectId=19,
        supply="Finish",
    )
    
    bike_mount8=Supply(
        projectId=19,
        supply="Paint",
    )
    
    bike_mount9=Supply(
        projectId=19,
        supply="2 Keyhole hangers",
    )
    
    bike_mount10=Supply(
        projectId=19,
        supply="Pocket hole jig, or something to make sure the dowels are going in straight",
    )

    data_crystals1=Supply(
        projectId=20,
        supply="Computer",
    )

    data_crystals2=Supply(
        projectId=20,
        supply="3D printer",
    )

    data_crystals3=Supply(
        projectId=20,
        supply="Power Drill",
    )

    mpcnc_controller1=Supply(
        projectId=21,
        supply='Nextion 4.3" Screen',
    )

    mpcnc_controller2=Supply(
        projectId=21,
        supply="3d printed the screen module",
    )

    mpcnc_controller3=Supply(
        projectId=21,
        supply="Transmitter",
    )

    mpcnc_controller4=Supply(
        projectId=21,
        supply="A pair of NRF24LO1 modules",
    )

    mpcnc_controller5=Supply(
        projectId=21,
        supply="Power transistor",
    )

    mpcnc_controller6=Supply(
        projectId=21,
        supply="8 pin Picaxe IC",
    )

    mpcnc_controller7=Supply(
        projectId=21,
        supply='A small 0.96" OLED',
    )

    garage_door1=Supply(
        projectId=22,
        supply="2 Servo Motor's",
    )

    garage_door2=Supply(
        projectId=22,
        supply='1 Infarred Sensor (IR)',
    )

    garage_door3=Supply(
        projectId=22,
        supply='1 Infarred Remote (IR) (any tv remote works)',
    )

    garage_door4=Supply(
        projectId=22,
        supply='2 Resistors',
    )

    garage_door5=Supply(
        projectId=22,
        supply="5-10 LED's (optional)",
    )

    garage_door6=Supply(
        projectId=22,
        supply='1 Breadboard',
    )

    garage_door7=Supply(
        projectId=22,
        supply='1 Arduino Uno',
    )

    garage_door8=Supply(
        projectId=22,
        supply='Frame (wood, 3D printed)',
    )

    garage_door9=Supply(
        projectId=22,
        supply='Construction Paper (Garage door)',
    )

    garage_door10=Supply(
        projectId=22,
        supply='1 Wire Cutter',
    )

    garage_door11=Supply(
        projectId=22,
        supply='1 Glue Gun',
    )

    garage_door12=Supply(
        projectId=22,
        supply='1 Soldering Iron',
    )

    garage_door13=Supply(
        projectId=22,
        supply='Wires',
    )

    garage_door14=Supply(
        projectId=22,
        supply='2 9v Batteries',
    )

    garage_door15=Supply(
        projectId=22,
        supply='1 battery cap (buckle connector)',
    )

    garage_door16=Supply(
        projectId=22,
        supply='1 battery cap (male DC plug)',
    )

    poop_bag1=Supply(
        projectId=23,
        supply='Leather of your choice 3 - 4 oz (1.2 - 1.6 mm is my recommendation).',
    )

    poop_bag2=Supply(
        projectId=23,
        supply='In this project i use Conceria Puccini "BISANZIO" (3 oz - 1.2 mm).',
    )

    poop_bag3=Supply(
        projectId=23,
        supply='Carabiner hook 11 x 53 mm.',
    )

    poop_bag4=Supply(
        projectId=23,
        supply='Cutter',
    )

    poop_bag5=Supply(
        projectId=23,
        supply='Ruler',
    )

    poop_bag6=Supply(
        projectId=23,
        supply='Hammer',
    )

    poop_bag7=Supply(
        projectId=23,
        supply='Round punch (1 mm)',
    )

    poop_bag8=Supply(
        projectId=23,
        supply='Round punch (3,5 mm)',
    )

    poop_bag9=Supply(
        projectId=23,
        supply='Round punch (10 mm)',
    )

    poop_bag10=Supply(
        projectId=23,
        supply='Wood slicker',
    )

    poop_bag11=Supply(
        projectId=23,
        supply='2x needles',
    )

    poop_bag12=Supply(
        projectId=23,
        supply='Sew thread',
    )

    poop_bag13=Supply(
        projectId=23,
        supply='Tokonole leather finish',
    )

    poop_bag14=Supply(
        projectId=23,
        supply='Leather balm (Protect leather and gives the leather a fresh look)',
    )

    poop_bag15=Supply(
        projectId=23,
        supply='Rotary tool (for example: Dremel) or sandpaper',
    )

    poop_bag16=Supply(
        projectId=23,
        supply='Edge beveler',
    )

    poop_bag17=Supply(
        projectId=23,
        supply='Lighter',
    )

    poop_bag18=Supply(
        projectId=23,
        supply='Snaps and handpress',
    )

    cup_carrier1=Supply(
        projectId=24,
        supply='Fusion 360, open-source Autodesk program',
    )

    cup_carrier2=Supply(
        projectId=24,
        supply='3D printer with PLA filament and its slicer (Ultimaker 2+ and Cura have been used here)',
    )

    cup_carrier3=Supply(
        projectId=24,
        supply='Pair of scissors',
    )

    cup_carrier4=Supply(
        projectId=24,
        supply='Sharp knife and green cutting mat',
    )

    cup_carrier5=Supply(
        projectId=24,
        supply='Ruler',
    )

    cup_carrier6=Supply(
        projectId=24,
        supply='2,5 x 40 cm sewing velcro loop and',
    )

    cup_carrier7=Supply(
        projectId=24,
        supply='2,5 x 15 sticky velcro hook',
    )

    cup_carrier8=Supply(
        projectId=24,
        supply='Ribbon 3 x 25 cm, we used leather look in function of solidity',
    )

    cup_carrier9=Supply(
        projectId=24,
        supply='Screw and nut: 5M x 50mm',
    )

    cup_carrier10=Supply(
        projectId=24,
        supply='Screwdriver fitting to the screw',
    )

    cup_carrier11=Supply(
        projectId=24,
        supply='Metal button as used for a jeans',
    )

    cup_carrier12=Supply(
        projectId=24,
        supply='1 sheet of Neoprene, a synthetic rubber, in a color of choice. Kalina chose green or blue.',
    )

    cardboard1=Supply(
        projectId=25,
        supply='Lots of boxes! And an industrial tape dispenser.',
    )

    zentrierwinkel1=Supply(
        projectId=26,
        supply='Werkbank mit Einspannvorrichtung',
    )

    zentrierwinkel2=Supply(
        projectId=26,
        supply='Rechteckleiste aus Kiefer (5x20x900mm)',
    )

    zentrierwinkel3=Supply(
        projectId=26,
        supply='Anschlagwinkel',
    )

    zentrierwinkel4=Supply(
        projectId=26,
        supply='spitzer Bleistift (mittlerer Härtegrad HB)',
    )

    zentrierwinkel5=Supply(
        projectId=26,
        supply='Gehrungsschneidlade',
    )

    zentrierwinkel6=Supply(
        projectId=26,
        supply='Japansäge',
    )

    zentrierwinkel7=Supply(
        projectId=26,
        supply='(Express) Holzleim',
    )

    zentrierwinkel8=Supply(
        projectId=26,
        supply='Schraubzwinge',
    )

    zentrierwinkel9=Supply(
        projectId=26,
        supply='Schleifpapier',
    )

    smores1=Supply(
        projectId=27,
        supply='2 cups heavy whipping cream',
    )

    smores2=Supply(
        projectId=27,
        supply='7.5 ounces marshmallow crème – one container',
    )

    smores3=Supply(
        projectId=27,
        supply='7 ounces sweetened condensed milk',
    )

    smores4=Supply(
        projectId=27,
        supply='½ cup mini marshmallows – toasted',
    )

    smores5=Supply(
        projectId=27,
        supply='4 sheets gram crackers crushed',
    )

    smores6=Supply(
        projectId=27,
        supply='6 pieces Chirardelli chocolate caramel squares cut into small pieces',
    )

    smores7=Supply(
        projectId=27,
        supply='1 tablespoon pure vanilla extract',
    )

    smores8=Supply(
        projectId=27,
        supply='Stand or Hand Mixer',
    )

    smores9=Supply(
        projectId=27,
        supply='Sterno or other chafing fuel can',
    )

    smores10=Supply(
        projectId=27,
        supply='wood or metal skewers',
    )
    
    gearbox1=Supply(
        projectId=28,
        supply='Confirmat Screw 6x50 mm',
    )

    gearbox2=Supply(
        projectId=28,
        supply='1 pcs D outer 15mm, D inner 3 mm (washer)',
    )

    gearbox3=Supply(
        projectId=28,
        supply='2 pcs D outer 15mm, D inner 6 mm (washer)',
    )

    gearbox4=Supply(
        projectId=28,
        supply='Nails 32 pcs D 2 mm, length at least 20mm',
    )

    gearbox5=Supply(
        projectId=28,
        supply='Long Nut M6',
    )

    gearbox6=Supply(
        projectId=28,
        supply='Plastic PLA/PETG/ABS... ~ 50g',
    )

    gearbox7=Supply(
        projectId=28,
        supply='Lubricant',
    )

    db.session.add(bird_house_supply1)
    db.session.add(bird_house_supply2)
    db.session.add(bird_house_supply3)
    db.session.add(casino_clock_supply1)
    db.session.add(casino_clock_supply2)
    db.session.add(casino_clock_supply3)
    db.session.add(casino_clock_supply4)
    db.session.add(casino_clock_supply5)
    db.session.add(casino_clock_supply6)
    db.session.add(one_board_mug1)
    db.session.add(one_board_mug2)
    db.session.add(one_board_mug3)
    db.session.add(one_board_mug4)
    db.session.add(one_board_mug5)
    db.session.add(skillet_burger1)
    db.session.add(skillet_burger2)
    db.session.add(skillet_burger3)
    db.session.add(skillet_burger4)
    db.session.add(skillet_burger5)
    db.session.add(skillet_burger6)
    db.session.add(james_webb1)
    db.session.add(james_webb2)
    db.session.add(james_webb3)
    db.session.add(james_webb4)
    db.session.add(james_webb5)
    db.session.add(james_webb6)
    db.session.add(james_webb7)
    db.session.add(james_webb8)
    db.session.add(james_webb9)
    db.session.add(james_webb10)
    db.session.add(slowmo_bird1)
    db.session.add(slowmo_bird2)
    db.session.add(slowmo_bird3)
    db.session.add(slowmo_bird4)
    db.session.add(slowmo_bird5)
    db.session.add(slowmo_bird6)
    db.session.add(slowmo_bird7)
    db.session.add(dragonfly1)
    db.session.add(dragonfly2)
    db.session.add(dragonfly3)
    db.session.add(dragonfly4)
    db.session.add(dragonfly5)
    db.session.add(arcade_stick1)
    db.session.add(arcade_stick2)
    db.session.add(arcade_stick3)
    db.session.add(arcade_stick4)
    db.session.add(arcade_stick5)
    db.session.add(arcade_stick6)
    db.session.add(arcade_stick7)
    db.session.add(arcade_stick8)
    db.session.add(arcade_stick9)
    db.session.add(arcade_stick10)
    db.session.add(minecraft_torch1)
    db.session.add(minecraft_torch2)
    db.session.add(minecraft_torch3)
    db.session.add(minecraft_torch4)
    db.session.add(minecraft_torch5)
    db.session.add(minecraft_torch6)
    db.session.add(minecraft_torch7)
    db.session.add(minecraft_torch8)
    db.session.add(giant_match1)
    db.session.add(giant_match2)
    db.session.add(giant_match3)
    db.session.add(giant_match4)
    db.session.add(giant_match5)
    db.session.add(giant_match6)
    db.session.add(bike_lamp1)
    db.session.add(bike_lamp2)
    db.session.add(bike_lamp3)
    db.session.add(bike_lamp4)
    db.session.add(bike_lamp5)
    db.session.add(bike_lamp6)
    db.session.add(bike_lamp7)
    db.session.add(bike_lamp8)
    db.session.add(bike_lamp9)
    db.session.add(bike_lamp10)
    db.session.add(bike_lamp11)
    db.session.add(rainbow1)
    db.session.add(rainbow2)
    db.session.add(rainbow3)
    db.session.add(rainbow4)
    db.session.add(rainbow5)
    db.session.add(rainbow6)
    db.session.add(frankenstein1)
    db.session.add(frankenstein2)
    db.session.add(frankenstein3)
    db.session.add(frankenstein4)
    db.session.add(frankenstein5)
    db.session.add(frankenstein6)
    db.session.add(frankenstein7)
    db.session.add(frankenstein8)
    db.session.add(frankenstein9)
    db.session.add(frankenstein10)
    db.session.add(frankenstein11)
    db.session.add(ice_cream1)
    db.session.add(ice_cream2)
    db.session.add(ice_cream3)
    db.session.add(ice_cream4)
    db.session.add(ice_cream5)
    db.session.add(hot_chocolate1)
    db.session.add(hot_chocolate2)
    db.session.add(hot_chocolate3)
    db.session.add(hot_chocolate4)
    db.session.add(hot_chocolate5)
    db.session.add(hot_chocolate6)
    db.session.add(hot_chocolate7)
    db.session.add(cocoa_bombs1)
    db.session.add(cocoa_bombs2)
    db.session.add(cocoa_bombs3)
    db.session.add(cocoa_bombs4)
    db.session.add(cocoa_bombs5)
    db.session.add(cocoa_bombs6)
    db.session.add(cocoa_bombs7)
    db.session.add(cocoa_bombs8)
    db.session.add(cocoa_bombs9)
    db.session.add(cocoa_bombs10)
    db.session.add(blossom1)
    db.session.add(blossom2)
    db.session.add(blossom3)
    db.session.add(blossom4)
    db.session.add(blossom5)
    db.session.add(blossom6)
    db.session.add(blossom7)
    db.session.add(blossom8)
    db.session.add(blossom9)
    db.session.add(torus1)
    db.session.add(torus2)
    db.session.add(torus3)
    db.session.add(torus4)
    db.session.add(torus5)
    db.session.add(torus6)
    db.session.add(torus7)
    db.session.add(torus8)
    db.session.add(torus9)
    db.session.add(torus10)
    db.session.add(bike_mount1)
    db.session.add(bike_mount2)
    db.session.add(bike_mount3)
    db.session.add(bike_mount4)
    db.session.add(bike_mount5)
    db.session.add(bike_mount6)
    db.session.add(bike_mount7)
    db.session.add(bike_mount8)
    db.session.add(bike_mount9)
    db.session.add(bike_mount10)
    db.session.add(data_crystals1)
    db.session.add(data_crystals2)
    db.session.add(data_crystals3)
    db.session.add(mpcnc_controller1)
    db.session.add(mpcnc_controller2)
    db.session.add(mpcnc_controller3)
    db.session.add(mpcnc_controller4)
    db.session.add(mpcnc_controller5)
    db.session.add(mpcnc_controller6)
    db.session.add(mpcnc_controller7)
    db.session.add(garage_door1)
    db.session.add(garage_door2)
    db.session.add(garage_door3)
    db.session.add(garage_door4)
    db.session.add(garage_door5)
    db.session.add(garage_door6)
    db.session.add(garage_door7)
    db.session.add(garage_door8)
    db.session.add(garage_door9)
    db.session.add(garage_door10)
    db.session.add(garage_door11)
    db.session.add(garage_door12)
    db.session.add(garage_door13)
    db.session.add(garage_door14)
    db.session.add(garage_door15)
    db.session.add(garage_door16)
    db.session.add(poop_bag1)
    db.session.add(poop_bag2)
    db.session.add(poop_bag3)
    db.session.add(poop_bag4)
    db.session.add(poop_bag5)
    db.session.add(poop_bag6)
    db.session.add(poop_bag7)
    db.session.add(poop_bag8)
    db.session.add(poop_bag9)
    db.session.add(poop_bag10)
    db.session.add(poop_bag11)
    db.session.add(poop_bag12)
    db.session.add(poop_bag13)
    db.session.add(poop_bag14)
    db.session.add(poop_bag15)
    db.session.add(poop_bag16)
    db.session.add(poop_bag17)
    db.session.add(poop_bag18)
    db.session.add(cup_carrier1)
    db.session.add(cup_carrier2)
    db.session.add(cup_carrier3)
    db.session.add(cup_carrier4)
    db.session.add(cup_carrier5)
    db.session.add(cup_carrier6)
    db.session.add(cup_carrier7)
    db.session.add(cup_carrier8)
    db.session.add(cup_carrier9)
    db.session.add(cup_carrier10)
    db.session.add(cup_carrier11)
    db.session.add(cup_carrier12)
    db.session.add(cardboard1)
    db.session.add(zentrierwinkel1)
    db.session.add(zentrierwinkel2)
    db.session.add(zentrierwinkel3)
    db.session.add(zentrierwinkel4)
    db.session.add(zentrierwinkel5)
    db.session.add(zentrierwinkel6)
    db.session.add(zentrierwinkel7)
    db.session.add(zentrierwinkel8)
    db.session.add(zentrierwinkel9)
    db.session.add(smores1)
    db.session.add(smores2)
    db.session.add(smores3)
    db.session.add(smores4)
    db.session.add(smores5)
    db.session.add(smores6)
    db.session.add(smores7)
    db.session.add(smores8)
    db.session.add(smores9)
    db.session.add(smores10)
    db.session.add(gearbox1)
    db.session.add(gearbox2)
    db.session.add(gearbox3)
    db.session.add(gearbox4)
    db.session.add(gearbox5)
    db.session.add(gearbox6)
    db.session.add(gearbox=7)
    
    db.session.commit()

def undo_supplies():
    db.session.execute('TRUNCATE supplies RESTART IDENTITY CASCADE;')
    db.session.commit()