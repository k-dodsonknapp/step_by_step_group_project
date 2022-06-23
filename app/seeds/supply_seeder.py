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

    arcade_stick3,=Supply(
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
    
    db.session.commit()

def undo_supplies():
    db.session.execute('TRUNCATE supplies RESTART IDENTITY CASCADE;')
    db.session.commit()