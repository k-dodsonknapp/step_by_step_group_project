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

    
    db.session.commit()

def undo_supplies():
    db.session.execute('TRUNCATE supplies RESTART IDENTITY CASCADE;')
    db.session.commit()