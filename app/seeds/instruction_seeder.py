from app.models import db, Instruction

def seed_instructions():

    bird_project1= Instruction(
        projectId=1,
        stepOrder=1,
        stepTitle="Get materials",
        instructions="Gather your materials", 
        photoUrl="https://imgprd19.hobbylobby.com/2/0e/4f/20e4f0a77628cacbbbb622fb4a01f7728b821d88/350Wx350H-116392-1019-px.jpg", 
        videoUrl="Video of materials"
    )

    bird_project2= Instruction(
        projectId=1,
        stepOrder=2,
        stepTitle="Start square",
        instructions="Take two pieces of wood and use wood glue put the two together", 
        photoUrl="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbYADPGL1BShmV9Nw9K12GCVu5SAR1pZ_0cBKV9AYyaakIoj-rZMdQF2cDIkWaM15sIGA&usqp=CAU", 
        videoUrl="Video of the action"
    )

    bird_project3= Instruction(
        projectId=1,
        stepOrder=3,
        stepTitle="Add rest of square",
        instructions="Repeat step 2 with the last two pieces of the square", 
        photoUrl="Picture of wood pieces and glue", 
        videoUrl="Video of the action"
    )

    bird_project4= Instruction(
        projectId=1,
        stepOrder=4,
        stepTitle="Add Roof",
        instructions="Add roof", 
        photoUrl="Picture of wood pieces and glue", 
        videoUrl="Video of the action"
    )

    bird_project5= Instruction(
        projectId=1,
        stepOrder=5,
        stepTitle="Add Shingles",
        instructions="Add shingles to roof", 
        photoUrl="Picture of wood pieces and glue", 
        videoUrl="Video of the action",
    )

    casino_clock1=Instruction(
        projectId=2,
        stepOrder=1,
        stepTitle="3D Print",
        instructions="""
                        3D print of parts for a single unit.
                        Print them with supplied posture.
                        Support structure is not necessary to print.
                        Print 14 copies of hinge.stl.
                        Parts for a single unit can be printed out with common 200mm x 200mm 3D printer.
                        Remove debris and blobs around the printed parts.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FZ6/C95S/KZBA6KQC/FZ6C95SKZBA6KQC.jpg?auto=webp&frame=1&width=775&height=1024&fit=bounds&md=76ba8aa9d6423ad5086e4b12e9ba2495",
        
    )

    casino_clock2=Instruction(
        projectId=2,
        stepOrder=2,
        stepTitle="Assemble the Rotor",
        instructions="""
                        The process of assembly is also illustrated in the video above.

                        Before attaching the card holder (hinge), please make sure that the card can be inserted smoothly.
                        Attach the hinge to the rotor by snap-fit manner.
                        Please note that the hinge has front and back. Please check the figure above.
                        After attaching the hinge, confirm the smoothness of the hinge. Rubbing (frequent motion of hinge with some strong force) might make it smooth.
                    """,
        photoUrl="https://content.instructables.com/ORIG/F8U/YRNB/KZBA6L77/F8UYRNBKZBA6L77.jpg?auto=webp&frame=1&crop=3:2&width=800&height=1024&fit=bounds&md=ae112a8a15850210f592c943c0233c9f",
    )

    casino_clock3=Instruction(
        projectId=2,
        stepOrder=3,
        stepTitle="Attach the Motor",
        instructions="""
                        Attach the motor with two tapping screws.
                        Cables should be drawn to backward.
                        Fix cables with zip ties.
                    """,
        photoUrl="https://content.instructables.com/ORIG/F8T/IZTV/KZBA6LRP/F8TIZTVKZBA6LRP.jpg?auto=webp&frame=1&crop=3:2&width=600&fit=bounds&md=83b58c6f9307531f255b70f949e62138",
    )

    casino_clock4=Instruction(
        projectId=2,
        stepOrder=4,
        stepTitle="Attach the Rotor to the Motor",
        instructions="""
                        Push in the axis of the motor to the hole of the rotor.
                        if they are loose, one drop of superglue from the outer hole will fix it.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FZ0/86KQ/KZBA6LZO/FZ086KQKZBA6LZO.jpg?auto=webp&frame=1&width=1024&fit=bounds&md=11f72f8d2c55555234d598a81e761b6b",
    )      

    casino_clock5=Instruction(
        projectId=2,
        stepOrder=5,
        stepTitle="Attach Cards",
        instructions="""
                        Stick double-sided adhesive tape to the short edge of the card.
                        Slide-in the card to the channel of the card holder (hinge).
                        1-2mm gap between the cards to the pillar is ideal.
                        You can arrange the cards either randomly (for fun) or ordered (less noise). Please note that the rotor rotates CW.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FAX/9GKB/KZBA6M8Q/FAX9GKBKZBA6M8Q.jpg?auto=webp&frame=1&crop=3:2&width=652&fit=bounds&md=93aa4d89772da241f5a9d7b96908a5b9",
    )  

    casino_clock6=Instruction(
        projectId=2,
        stepOrder=6,
        stepTitle="Make 3 Units Getting Together",
        instructions="""
                        Print base.stl and attach the units to the base.
                        Attach motor driver to the base.
                        (optional : cover.stl can be used in the final step. If you use Dupont connectors, the cover.stl is too small to cover them. To use this cover, direct soldering of the wires are necessary. M5stack can be attached with a M2 screw.)
                    """,
        photoUrl="https://content.instructables.com/ORIG/FJQ/ZFOH/KZBA6NQ0/FJQZFOHKZBA6NQ0.jpg?auto=webp&frame=1&width=717&height=1024&fit=bounds&md=6201514dc2ca3520295f5b8a4e1ce2cf",
    )           

    casino_clock7=Instruction(
        projectId=2,
        stepOrder=7,
        stepTitle="Connect Microcontroller",
        instructions="""
                        Selection of microcontrollers

                        You can use any micro controller with 12 or more GPIO ports to control three stepper motors.
                        The clock code with WiFi time acquisition assumes ESP8266 / ESP32 type modules.
                        I used M5stamp-C3 for this clock.

                        Connection example of M5stamp-C3

                        Connect four pins of first (1minute) motor to G4, G5, G6, G7.
                        Connect four pins of second (10minute) motor to G0, G1, G8, G10.
                        Connect four pins of third (hour) motor to G9, G18, G19, G21.
                        Connect 5V and GND to the microcontroller. (M5stamp-C3 has three 5V and GND pairs)
                    """,
        photoUrl="https://content.instructables.com/ORIG/FJQ/ZFOH/KZBA6NQ0/FJQZFOHKZBA6NQ0.jpg?auto=webp&frame=1&width=717&height=1024&fit=bounds&md=6201514dc2ca3520295f5b8a4e1ce2cf",
    )       


    casino_clock8=Instruction(
        projectId=2,
        stepOrder=8,
        stepTitle="Edit Source Code and Flash",
        instructions="""
                        Test

                        Two types of test codes are provided : for a single unit or three units.
                        Register the order of the cards to the source code.
                        If you use microcontrollers other than M5stamp, edit the port assignment.
                        Flash the code using Arduino IDE.
                        Confirm the correctness of card order by using single-unit-test.ino before using clock.ino because the clock code so too slow to check the correctness.

                        Use as clock

                        Copy the card order definition from the test code to clock.ino.
                        Flash clock.ino to the microcontroller with Arduino IDE.

                        SSID / password configuration using SmartConfig

                        You can set SSID and password of your WiFi using smartphone app.This function is named SmartConfig. The apps for setting are at

                        Android : https://play.google.com/store/apps/details?id=com.khoazero123.iot_esptouch_demo
                        iOS : https://apps.apple.com/jp/app/espressif-esptouch/id1071176700
                        Please not that your smartphone should be connected to 2.4GHz WiFi.

                        LED colors on M5stamp

                        green : initializing the rotors
                        blue : connecting WiFi stored in non-volatile memory
                        red : smartConfig mode. Please set SSID and password using smartConfig app.
                        turn off : clock operation mode
                    """,
        photoUrl="https://content.instructables.com/ORIG/FVS/QB7W/KZBA6P9G/FVSQB7WKZBA6P9G.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=0052fd3109d6441894a67cb55f5e5989",
    )    

    one_board_mug1=Instruction(
        projectId=2,
        stepOrder=1,
        stepTitle="Measure the Circles",
        instructions="""
                        Use any circular shape you wish or measure using a compass. 
                        Create an outter circle and an inner circle. 
                        Sizes can very but keep in mind this is the size of the lip of the mug you will drink from. 
                        (Also keep in mind some sanding will take place)

                        I make most mugs out of 5/6 circles with one bottom I’ll add later.
                    """,
        photoUrl="https://content.instructables.com/ORIG/F9G/3GTT/KZBA1FUQ/F9G3GTTKZBA1FUQ.jpg?auto=webp&frame=1&fit=bounds&md=7ef820df5c39c993cadfe3630dc4569f",
    )
    
    one_board_mug2=Instruction(
        projectId=2,
        stepOrder=2,
        stepTitle="Cut Out",
        instructions="""
                        Start by drilling a hole in the center of the mug. Cut out inside first. Then cut outside ring.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FWV/6KID/KZBA1FUV/FWV6KIDKZBA1FUV.jpg?auto=webp&frame=1&width=634&height=1024&fit=bounds&md=7cd60a18426ba1dd890929772d970a4d",
    )

    one_board_mug3=Instruction(
        projectId=2,
        stepOrder=3,
        stepTitle="Glue Together",
        instructions="""
                        Glue all pieces together and clamp. (Do not add bottom of mug yet)

                        If you do not have any clamps you can simply stack something heavy on top such as a weight or rocks.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FWV/6KID/KZBA1FUV/FWV6KIDKZBA1FUV.jpg?auto=webp&frame=1&width=634&height=1024&fit=bounds&md=7cd60a18426ba1dd890929772d970a4d",
    )

    one_board_mug4=Instruction(
        projectId=2,
        stepOrder=4,
        stepTitle="Begin to Sand",
        instructions="""
                        You can use any sanding method. Some work faster than others. Sand with a low grit 60/80 to shape the mug. Use a large spindle sander for inside of a dremel.
                    """,
    )

    one_board_mug5=Instruction(
        projectId=2,
        stepOrder=5,
        stepTitle="Add Bottom",
        instructions="""
                        Once sanded to your likening, trace the bottom of mug on remaining wood. Cut out with Scroll saw and glue to mug. Once dry, sand again.
                    """,
    )

    one_board_mug6=Instruction(
        projectId=2,
        stepOrder=6,
        stepTitle="Handle",
        instructions="""
                        On remaining wood, measure height of mug and draw a handle you desire. Cut out and glue to mug. Clamp or secure and allows to dry.

                        You can also use dowel pins for extra hold.

                        You may need to use dremel or hand sand a curve in the handle ends to allow a closer fit to the mug.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FI5/3OWK/KZBA1FVQ/FI53OWKKZBA1FVQ.jpg?auto=webp&frame=1&width=575&height=1024&fit=bounds&md=bf508a2da6e1a63aa99b16e9cd427258",
    )

    one_board_mug7=Instruction(
        projectId=2,
        stepOrder=7,
        stepTitle="Finish Handle",
        instructions="""
                        Sand handle once dry.

                        I like to use strips of sand paper used with a lathe. This helps develop a more rounded look.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FY7/RL1L/KZBA1FV1/FY7RL1LKZBA1FV1.jpg?auto=webp&frame=1&fit=bounds&md=58ca0d08649fea49699de4b7e5f1508c",
    )

    one_board_mug8=Instruction(
        projectId=2,
        stepOrder=8,
        stepTitle="Add Finish",
        instructions="""
                        I usually test in water at this point. If you have any leaks you can soak the wood in water and allow to dry. This helps shrink the wood.

                        You can also add a food safe epoxy to the inside to seal any leaks or to allow for both cold and hot beverages. You can even use coffee for more natural looks.

                        Before sealing add any design you wish. Torched, stained etc.

                        Add wood oil and wood conditioner to outside of mug to seal.
                    """,
        photoUrl="https://content.instructables.com/ORIG/F6Y/R6JL/KZBA1FWJ/F6YR6JLKZBA1FWJ.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=d7af5ae887c84c5cf35e99f3b9a6b359",
    )

    one_board_mug9=Instruction(
        projectId=2,
        stepOrder=9,
        stepTitle="Add Finish",
        instructions="""
                        Allow the cure per instructions on product used.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FIC/RO72/KZBA1FWK/FICRO72KZBA1FWK.jpg?auto=webp&frame=1&fit=bounds&md=ef5c95a65c5263252bb3002ab3fa9fb1",
    )

    one_board_mug10=Instruction(
        projectId=2,
        stepOrder=10,
        stepTitle="Add Finish",
        instructions="""
                        Just so we have no waste, you can use the inner circles you cut out and make a smaller mug. A shot glass or juice glass. Follow the same steps!! Then enjoy!!!
                    """,
        photoUrl="https://content.instructables.com/ORIG/FM1/8EYX/KZBA1FVG/FM18EYXKZBA1FVG.jpg?auto=webp&frame=1&width=628&height=1024&fit=bounds&md=2b3645e2db53a0024796989cee81dc7f",
    )

    db.session.add(bird_project1)
    db.session.add(bird_project2)
    db.session.add(bird_project3)
    db.session.add(bird_project4)
    db.session.add(bird_project5)
    db.session.add(casino_clock1)
    db.session.add(casino_clock2)
    db.session.add(casino_clock3)
    db.session.add(casino_clock4)
    db.session.add(casino_clock5)
    db.session.add(casino_clock6)
    db.session.add(casino_clock7)
    db.session.add(one_board_mug1)
    db.session.add(one_board_mug2)
    db.session.add(one_board_mug3)
    db.session.add(one_board_mug4)
    db.session.add(one_board_mug5)
    db.session.add(one_board_mug6)
    db.session.add(one_board_mug7)
    db.session.add(one_board_mug8)
    db.session.add(one_board_mug9)
    db.session.add(one_board_mug10)
    

    db.session.commit()


def undo_instructions():
    db.session.execute('TRUNCATE instructions RESTART IDENTITY CASCADE;')
    db.session.commit()