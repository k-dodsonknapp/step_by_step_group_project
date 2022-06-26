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
        photoUrl="https://contentgrid.homedepot-static.com/hdus/en_US/DTCCOMNEW/Articles/how-to-build-a-birdhouse-2022-step-2.jpg", 
        videoUrl="Video of the action"
    )

    bird_project4= Instruction(
        projectId=1,
        stepOrder=4,
        stepTitle="Add Roof",
        instructions="Add roof", 
        photoUrl="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTb1Cs0ZEUIVryhtLQf6wFiU9lawobBwLCSCg&usqp=CAU", 
        videoUrl="Video of the action"
    )

    bird_project5= Instruction(
        projectId=1,
        stepOrder=5,
        stepTitle="Add Shingles",
        instructions="Add shingles to roof", 
        photoUrl="https://i.ytimg.com/vi/g2xk0lSqm2k/maxresdefault.jpg", 
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
        projectId=3,
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
        projectId=3,
        stepOrder=2,
        stepTitle="Cut Out",
        instructions="""
                        Start by drilling a hole in the center of the mug. Cut out inside first. Then cut outside ring.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FWV/6KID/KZBA1FUV/FWV6KIDKZBA1FUV.jpg?auto=webp&frame=1&width=634&height=1024&fit=bounds&md=7cd60a18426ba1dd890929772d970a4d",
    )

    one_board_mug3=Instruction(
        projectId=3,
        stepOrder=3,
        stepTitle="Glue Together",
        instructions="""
                        Glue all pieces together and clamp. (Do not add bottom of mug yet)

                        If you do not have any clamps you can simply stack something heavy on top such as a weight or rocks.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FWV/6KID/KZBA1FUV/FWV6KIDKZBA1FUV.jpg?auto=webp&frame=1&width=634&height=1024&fit=bounds&md=7cd60a18426ba1dd890929772d970a4d",
    )

    one_board_mug4=Instruction(
        projectId=3,
        stepOrder=4,
        stepTitle="Begin to Sand",
        instructions="""
                        You can use any sanding method. Some work faster than others. Sand with a low grit 60/80 to shape the mug. Use a large spindle sander for inside of a dremel.
                    """,
    )

    one_board_mug5=Instruction(
        projectId=3,
        stepOrder=5,
        stepTitle="Add Bottom",
        instructions="""
                        Once sanded to your likening, trace the bottom of mug on remaining wood. Cut out with Scroll saw and glue to mug. Once dry, sand again.
                    """,
    )

    one_board_mug6=Instruction(
        projectId=3,
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
        projectId=3,
        stepOrder=7,
        stepTitle="Finish Handle",
        instructions="""
                        Sand handle once dry.

                        I like to use strips of sand paper used with a lathe. This helps develop a more rounded look.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FY7/RL1L/KZBA1FV1/FY7RL1LKZBA1FV1.jpg?auto=webp&frame=1&fit=bounds&md=58ca0d08649fea49699de4b7e5f1508c",
    )

    one_board_mug8=Instruction(
        projectId=3,
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
        projectId=3,
        stepOrder=9,
        stepTitle="Allow Any Finishes to Cure",
        instructions="""
                        Allow the cure per instructions on product used.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FIC/RO72/KZBA1FWK/FICRO72KZBA1FWK.jpg?auto=webp&frame=1&fit=bounds&md=ef5c95a65c5263252bb3002ab3fa9fb1",
    )

    one_board_mug10=Instruction(
        projectId=3,
        stepOrder=10,
        stepTitle="Use Remaining Pieces of Wood",
        instructions="""
                        Just so we have no waste, you can use the inner circles you cut out and make a smaller mug. A shot glass or juice glass. Follow the same steps!! Then enjoy!!!
                    """,
        photoUrl="https://content.instructables.com/ORIG/FM1/8EYX/KZBA1FVG/FM18EYXKZBA1FVG.jpg?auto=webp&frame=1&width=628&height=1024&fit=bounds&md=2b3645e2db53a0024796989cee81dc7f",
    )

    skillet_burger1=Instruction(
        projectId=4,
        stepOrder=1,
        stepTitle="Fry Up the Bacon",
        instructions="""
                        In a large saute pan over medium-high heat, add bacon. Cook until crispy and remove to a paper towel covered plate. Reserve bacon grease.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FG7/M0DL/KYK4NWC1/FG7M0DLKYK4NWC1.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=727e24ebd9fc48457c55b2e452da9220",
    )

    skillet_burger2=Instruction(
        projectId=4,
        stepOrder=2,
        stepTitle="Get the Onions Going",
        instructions="""
                        Add sliced onions to bacon grease and cook for 3 minutes stirring occasionally.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FG7/M0DL/KYK4NWC1/FG7M0DLKYK4NWC1.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=727e24ebd9fc48457c55b2e452da9220",
    )

    skillet_burger3=Instruction(
        projectId=4,
        stepOrder=3,
        stepTitle="Make the Patties",
        instructions="""
                        Add patty ingredients to a mixing bowl and combine. Form into 6 patties. Add to saute pan with onions. Reduce heat to medium. Cover pan and cook for 8 minutes.

                        Flip each burger and recover for 8 minutes more.

                        Remove lid and lay a slice of cheese on each burger. Let sit for a minute then remove burgers. Remove onions from heat.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FYD/WV95/KYK4NWBZ/FYDWV95KYK4NWBZ.jpg?auto=webp&frame=1&width=800&height=1024&fit=bounds&md=f8d508e203d652b1b506abc1d36d999b",
    )

    skillet_burger4=Instruction(
        projectId=4,
        stepOrder=4,
        stepTitle="Make the Sauce",
        instructions="""
                        Combine sauce ingredients in a small bowl and set aside.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FHE/ACCO/KYK4NWBT/FHEACCOKYK4NWBT.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=2c457488b792655c263a91f32ad45dc8",
    )

    skillet_burger5=Instruction(
        projectId=4,
        stepOrder=5,
        stepTitle="Build the Burger",
        instructions="""
                        Build the burger: smear bun with sauce. Add pickles and bacon. Top with a cheeseburger and cooked onions. Add top bun and enjoy!
                    """,
        photoUrl="https://content.instructables.com/ORIG/FEA/B667/KYK4NWBY/FEAB667KYK4NWBY.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=c184318d11bd6c0378b95837fbd25fb4",
    )

    james_webb1=Instruction(
        projectId=5,
        stepOrder=1,
        stepTitle="Layout and Outline the Golden Hexagons",
        instructions="""
                        The first step is to lay the golden hexagon stickers out in the pattern shown in the image to resemble the telescope's mirror. Do not stick the hexagons to the wood, simply lay them on there.

                        Using the pencil you then need to draw an outline around the stickers.

                        Once this outline is done you then need to draw another outline 2cm larger than the one you just did. I did this by using the ruler to make a small mark 2cm out from each flat edge and then draw a straight line parallel to the previous outline
                    """,
        photoUrl="https://content.instructables.com/ORIG/FOA/PHZ3/KYK4QAOS/FOAPHZ3KYK4QAOS.jpg?auto=webp&frame=1&width=719&fit=bounds&md=b8dde0a898fad98e8dae2b7df4785fec",
    )

    james_webb2=Instruction(
        projectId=5,
        stepOrder=2,
        stepTitle="Cut, Sand and Paint the MDF",
        instructions="""
                        First, cut around the outer line you have drawn on the wood with the pencil using a Jigsaw (other tools may be better but a Jigsaw is what I had to hand). Then drill a hole in the center circle that was drawn for the clock and use the jigsaw to cut the circle out. When cutting the hole make sure you stay on the inside of the line so the clock fits snug into the hole without any glue. You should end up with the shape shown in the picture.

                        Once the MDF has been cut, take the sandpaper (i used P120 but that may not be the optimal grit size) and sand all the edges of the MDF and the middle. As you are sanding the middle circle, make sure the clock fits tightly in the hole as you go, that way you will get a good fit won't need any glue when fitting the clock.

                        Once all the edges have been sanded, brush off any unwanted sawdust and place it in the paint area.

                        The paint area doesn't need to be indoors however protection from weather may be necessary as the paint takes an hour or so to dry properly. I painted mine on bin bags placed on the lawn as it was a sunny winter's day when I painted it.

                        Make sure you keep the spray can at least 25cm away from the MDF when spraying to prevent drips from forming.

                        Also, remember to spray the edges of the MDF as these will be visible when it is hanging on the wall. There is no need to do the backside of the MDF unless you want to.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FZ3/67BZ/KYVK6ZK4/FZ367BZKYVK6ZK4.jpg?auto=webp&frame=1&width=746&height=1024&fit=bounds&md=f328dbec2577deea8d055990585adfdc",
    )

    james_webb3=Instruction(
        projectId=5,
        stepOrder=3,
        stepTitle="Stick the Hexagons on the MDF and Fit the Clock",
        instructions="""
                        Sticking the Hexagons Down
                        Sticking the hexagon panels on the MDF is as simple as peeling the sticky side cover off and applying to the painted side of the MDF.

                        To get the alignment right (as all the hexagons will be slightly different in size) i suggest arranging the hexagons where they are going to be stuck down before sticking them, that way you can make sure they align correctly before committing. This can be cumbersome as the panels slide easily on the wood but it is worth spending the time on.

                        Once they are all aligned, work your way from bottom to top or top to bottom sticking one panel down at a time.

                        The panels can be removed once stuck down and won't peel the paint off (at least in my experience) but you will need a knife to get them off.

                        Once all panels have been stuck down, peel the protective film off the shiny side to reveal the golden majesty :)

                        Fitting the Clock
                        If you have cut and sanded the hole to a snug size you should just be able to push the clock enclosure into the hole without any glue. If the hole is too big then you may need some sort of glue to hold it in place.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FNC/JKOF/KYVK71DG/FNCJKOFKYVK71DG.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=83de509cec2e66f4e86e07ae4a6fd110",
    )

    james_webb4=Instruction(
        projectId=5,
        stepOrder=4,
        stepTitle="Mounting",
        instructions="""
                        If you bought the suggested clock, the clock mechanism itself has a hook for hanging the clock. Providing that you made the clock fit tightly into the hole, you can use the hook with a nail or a standard picture hook.

                        The other option is to use hanging strips. It is important to use the velcro(esk) ones to make the clock sit slightly off the wall as the MDF might bend slightly and therefore fail to stick (see suggested hanging methods in the Supplies section.

                        THAT'S IT!!

                        Hope you enjoy your new James Webb Space TeleClock
                    """,
        photoUrl="https://content.instructables.com/ORIG/F2D/W1UN/KYVK737V/F2DW1UNKYVK737V.jpg?auto=webp&frame=1&width=924&height=1024&fit=bounds&md=cf297c9c91d3ecf32bee622b0f5bff2f",
    )

    slowmo_bird1=Instruction(
        projectId=6,
        stepOrder=1,
        stepTitle="The Set-up",
        instructions="""
                        This project involves carefully planning of the arrangement of objects in space. First, you need a bird feeder. You may already have one, but make sure it is placed in an optimal location, typically near a large window of your dwelling. Place a perch 8 to 10 feet away from the feeder, opposite the direction of the house and somewhat off to the side. This plan takes advantage of the fact that birds like to land near a feeder and check it out before flying to it and consuming the seed. Photograph the bird when it flies from the perch to the feeder.

                        The type of feeder doesn't matter much. I use only sunflower seed in my feeder, as most birds really don't care for the other seeds in mixed bird feed. I also use a suet feeder, which is a great way to attract woodpeckers.

                        It's best to use a natural stick, such as one that's fallen from a tree. You can jam it into the ground or use a support like an umbrella stand to hold it up. The top of it should be about the same height as the bird feeder. By using a natural stick rather than a human-made object, you can get natural-looking photos of a perching bird if you want them. You may need to move it around to find the spot that the birds prefer. It's also better if there are not competing objects that can be used as perches nearby. Finally, try to use a location that will result in photographs with a pleasing background.

                        Inside the house, place your camera on a tripod as close to the window as is practical. Ideally, the sun should be behind the camera, which may affect which window you choose to use for this project. If the sun is directly behind the bird, you will get only silhouettes of birds, which are not very gratifying. The window should be thoroughly cleaned inside and out. Make sure there are no reflections in the area of the window through which you are shooting. If the end of the lens is very close to the window, there should not be any reflections in the images. Adjust room lighting if necessary. Even double-paned windows should have little noticeable effect on image quality.
                    """,
        photoUrl="https://content.instructables.com/ORIG/F1V/1SRU/KY8P62DF/F1V1SRUKY8P62DF.jpg?auto=webp&frame=1&width=790&fit=bounds&md=074ac899fc620af930e3b9d8c36e2332",
    )

    slowmo_bird2=Instruction(
        projectId=6,
        stepOrder=2,
        stepTitle="The Photography",
        instructions="""
                        Equipment

                        The camera must have some degree of manual controls. Almost any DSLR will do, and many superzoom point-and-shoot cameras will also work (my equipment is detailed in a photo above). The length of the lens required depends on how far the feeder is from the window. If the feeder is far away, a longer, presumably more expensive lens will be needed. The tripod doesn't need to be fancy, as long as it holds the camera firmly.

                        Settings

                        The camera should have Av mode, or Aperture Priority. Set the camera on this mode and adjust the aperture to F/8, or about two stops above the lowest F-stop. This setting will provide adequate depth of field and minimal aberrations. Set ISO to the lowest natural level of your camera. For example, my Canon 7D can be set as low as ISO 100, but its true minimum is 160. You should shoot on a sunny day, otherwise higher ISO will be needed and the images will become more grainy. White balance should be set on automatic or full sun. These settings work in your favor in that the camera will automatically choose the highest shutter speed that can produce a properly exposed image, resulting in freezing the motion of the bird's wings. If you have the equipment and know-how, you could set up a remote flash and probably get more consistent results, but that's beyond the scope of this Instructable.

                        Place an object halfway between the perch and the feeder and prefocus your camera on it using manual focus. Leave the camera on manual focus and try not to bump it. Set the lens at a zoom level that is reasonably wide. If you zoom it too tightly, you'll cut off bits of the birds in every frame. It's better to have the entire bird in the frame and crop it later.

                        Shooting

                        If you have one, connect a remote shutter to the camera to minimize camera shake. Set your camera on burst mode if available, and wait for a bird to land on the perch. Now place your finger on the shutter button (or remote button). As soon as the bird moves to fly, hold down the button to take a rapid series of photos (a burst). Let off the button when the bird reaches the feeder. At some point during the bird's flight, it should be in focus and in frame for at least one image. Delete the rest. It will likely require some experimentation and adjustment to get the best results. Some photographers prefer not to use burst mode, instead using their own natural skill and timing to capture a single ideal image of such a natural moment. This strategy takes considerable skill. Birds are fast!

                        Post-processing

                        It almost goes without saying that you should crop the photo and make some global lighting adjustments to make the best image you can. You may capture birds in some interesting positions. I provide a couple of examples here.
                    """,
        photoUrl="https://content.instructables.com/ORIG/F1R/96CG/KY2ZEWJP/F1R96CGKY2ZEWJP.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=f6448db5cc082560d4f9f2019b4dc9c5",
    )

    dragonfly1=Instruction(
        projectId=7,
        stepOrder=1,
        stepTitle="Sketch and Inspiration",
        instructions="""
                        I sketched up the general idea of the bamboo dragonfly, which is exactly like the actual insect--dragonfly. I needed to model a pole for hands to hold, spin, and model a long blade as the propeller in flight. To look like a funny dragonfly, I would add a tiny head with tentacles on the top of the blade. The whole thing with all the parts assembled will be a very fantastic toy for kids.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FLY/5AIN/KSN80T48/FLY5AINKSN80T48.jpg?auto=webp&frame=1&width=860&height=1024&fit=bounds&md=bd0bbda6f38e6d64bb1c0ba4b3dc2e3d",
    )

    dragonfly2=Instruction(
        projectId=7,
        stepOrder=2,
        stepTitle="Model With Tinkercad and 3D Print",
        instructions="""
                      I used a knife to ground the blade's edges to be round and glued the tiny head to the center of the blade, which looks straight and perfect. Then I use a metal color spray to paint the whole product blue. After that, I needed to paint details of the dragonfly's eyes, stripes of its body, and the pattern of the wings with Acrylic paint. Now a vivid dragonfly comes, and it will fly in the air pushed by my hands.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FI6/SOT1/KSN80TL9/FI6SOT1KSN80TL9.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=0f94cc925b4c772cae91e777494d5583",
    )

    dragonfly3=Instruction(
        projectId=7,
        stepOrder=3,
        stepTitle="Assemble, Polish and Paint",
        instructions="""
                       I modeled the bamboo dragonfly by Autodesk Tinkercad, then export the model file with the dragonfly.STL. I opened Creality Slicer to import the Dragonfly.STL and exported to the 3D printer with file Dragonfly.gcode. So the bamboo dragonfly becomes an actual product.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FI6/SOT1/KSN80TL9/FI6SOT1KSN80TL9.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=0f94cc925b4c772cae91e777494d5583",
    )


    dragonfly4=Instruction(
        projectId=7,
        stepOrder=4,
        stepTitle="Let the Drangonfly Fly High in the Air",
        instructions="""
                       It's time to let it fly! Please watch my video.
                    """,
        photoUrl="https://content.instructables.com/ORIG/FD5/S83I/KSN80UDF/FD5S83IKSN80UDF.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=09be231e428443e47937f1e5cabcf7fe",
        videoUrl="https://www.youtube.com/watch?v=pjgGGpcfTYQ"
    )

    arcade_stick1=Instruction(
        projectId= 8,
        stepOrder= 1,
        stepTitle= 'Cut Control Panel to Size and Drill Holes',
        instructions= """
        After cutting the butcher block to my desired size for the control panel, I printed out my preferred panel layout (grabbed from Slagcoin) and taped it to the top. I went with a Sega-style layout that had extra space between the joystick and buttons. I then used my drill press and a 1 1/8” hole saw ( about 29mm) to drill the holes for the buttons and a 7/8” (about 22mm) hole saw for the joystick.
        """,
        photoUrl="https://content.instructables.com/ORIG/F24/J26L/L1C5JWFA/F24J26LL1C5JWFA.jpg?auto=webp&frame=1&width=588&fit=bounds&md=d363415de2a3e526c8ddecaa37676260",
        videoUrl="",
    )

    arcade_stick2=Instruction(
        projectId= 8,
        stepOrder= 2,
        stepTitle= 'Route the Inside of the Control Panel',
        instructions= """
        I then used my router to thin out the 1 1/8” thick butcher block to the desired 3/8” thickness inside to allow for the proper range of motion for the joystick. Usually it’s recommended that the distance between the bottom of the joystick ball and the top of the control panel is about 9/10” (23mm). Doing this also gave me more space inside for all the required components.
        """,
        photoUrl="https://content.instructables.com/ORIG/F72/FE72/L1C5JWFB/F72FE72L1C5JWFB.jpg?auto=webp&frame=1&width=1009&fit=bounds&md=bee81bc88c813f089ac8e76c56b641df",
        videoUrl="",
    )

    arcade_stick3=Instruction(
        projectId= 8,
        stepOrder= 3,
        stepTitle= 'Test Fit the Buttons and Joystick',
        instructions= """
        After routing the inside of the control panel, I propped it up on some blocks of wood and test fit the buttons to make sure they fit in securely but weren't too tight. My holes ended up being the perfect size didn't require any sanding. I also made sure the joystick fit correctly and checked the spacing between the joystick ball and control panel.
        """,
        photoUrl="https://content.instructables.com/ORIG/F24/SYEZ/L1C5JX62/F24SYEZL1C5JX62.jpg?auto=webp&frame=1&width=933&fit=bounds&md=a9bed55cb63bdc199816f3bb69ecf371",
        videoUrl="",
    )

    arcade_stick4=Instruction(
        projectId= 8,
        stepOrder= 4,
        stepTitle= 'Assemble Panel Support Box',
        instructions= """
        I assembled a small box out of an extra 3/4" scrape wood and drilled the necessary holes for the three front buttons I wanted (Start, Select and Special), as well as the USB port. I didn’t have the necessary 24mm diameter bit for the USB port so I used my 7/8” (22mm) hole saw and used a smaller drill bit to increase the diameter to fit. I then glued the box to the the control panel top, clamped it up and let it dry for 24 hours.
        """,
        photoUrl="https://content.instructables.com/ORIG/F1Y/P0GI/L1C5JX63/F1YP0GIL1C5JX63.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=9c79edc75cf0ba44cdbe8d9497a54e27",
        videoUrl="",
    )

    arcade_stick5=Instruction(
        projectId= 8,
        stepOrder= 5,
        stepTitle= 'Apply Coats of Mineral Oil',
        instructions= """
        Using a rag, I applied a few coats of mineral oil to the control panel top and to the sides to bring out the natural color of the wood and prevent any drying or cracking. It made a huge difference!
        """,
        photoUrl="https://content.instructables.com/ORIG/F0R/SISZ/L1C5JX64/F0RSISZL1C5JX64.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=bf0f8e50c6b6115783ad05568fcecaa6",
        videoUrl="",
    )

    arcade_stick6=Instruction(
        projectId= 8,
        stepOrder= 6,
        stepTitle= 'Attach Buttons and Wire Them to USB Encoder',
        instructions= """
        I then assembled all the components inside the box. It was a little tricky to securely mount the joystick into the 3/8” top but I managed to do it using some small screws and extra washers. This gives it a nice clean look without screws showing on the top of the control panel (something I see on a lot of other DIY arcade sticks).

        I then glued the USB encoder to the side of the box to keep it secure and also glued some small blocks to the inside edges of the box so that I had something for the feet to screw into. Lastly, I attached the ribbon cable from going between the Joystick and USB encoder and wired up all the buttons to the USB encoder. As long as you hook up the buttons to the button slots, the actual order doesn't matter as you can easily remap these in RetroPie.
        """,
        photoUrl="https://content.instructables.com/ORIG/FXK/9RZI/L1C5JWFC/FXK9RZIL1C5JWFC.jpg?auto=webp&frame=1&width=1009&fit=bounds&md=039ebbf73a0800d382e966ee7af24dc7",
        videoUrl="",
    )

    arcade_stick7=Instruction(
        projectId= 8,
        stepOrder= 7,
        stepTitle= 'Cut and Attach Bottom Panel With Rubber Feet',
        instructions= """
        I cut a small piece of 1/8” MDF for the bottom cover. This way I could use the feet to hold the cover on so it’s easily removable if I ever need to mess with any of the components.
        """,
        photoUrl="https://content.instructables.com/ORIG/F65/7448/L1C5JWFD/F657448L1C5JWFD.jpg?auto=webp&frame=1&width=525&fit=bounds&md=0e5dc314d2be6f4a9d36e5fb357fd9c8",
        videoUrl="",
    )

    arcade_stick8=Instruction(
        projectId= 8,
        stepOrder= 8,
        stepTitle= 'Play Some Games',
        instructions= """
        I plugged it into my RetroPie machine and it was instantly recognized as a game controller. I quickly mapped the controls and jumped into playing one of my favorite games. I love the experience of playing old arcade games with it.
        """,
        photoUrl="https://content.instructables.com/ORIG/FKO/1V4V/L1C5JWFE/FKO1V4VL1C5JWFE.jpg?auto=webp&frame=1&width=933&fit=bounds&md=86e835969f64c7ee7cca8315646a48c8",
        videoUrl="",
    )


    minecraft_torch1=Instruction(
        projectId= 9,
        stepOrder= 1,
        stepTitle= 'Print the Templates',
        instructions= """
        We've included a PDF file with templates for these torches as well as six other Minecraft-Inspired projects!
        Each project is meant to be printed double-sided so you can build the circuit on the inside and see the art on the outside.
        You'll also find black & white versions that you can color yourself.
        """,
        photoUrl="https://content.instructables.com/ORIG/FUG/DPDX/L1AQ22XS/FUGDPDXL1AQ22XS.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=83df7cabf13b7695d6fbfcc29691c4cd",
        videoUrl="",
    )

    minecraft_torch2=Instruction(
        projectId= 9,
        stepOrder= 2,
        stepTitle= 'Cut the Templates',
        instructions= """
        After you print the templates you'll need to cut them.
        Always cut on the outside just in case your printer doesn't line things up perfectly.
        If the inside is not perfectly aligned, that's okay! Just use it as a rough guide.
        Tip: If you can't print double-sided easily just print out each page separately and use the diagram for reference when you build your circuit.
        """,
        photoUrl="https://content.instructables.com/ORIG/FZD/KGYW/L1AQ22XT/FZDKGYWL1AQ22XT.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=12419342e9a0454ecaea7455f6d63820",
        videoUrl="",
    )

    minecraft_torch3=Instruction(
        projectId= 9,
        stepOrder= 3,
        stepTitle= 'Fold Templates',
        instructions= """
        Fold each piece as indicated using the lines on the outside as a guide.
        """,
        photoUrl="https://content.instructables.com/ORIG/F3T/XII7/L1AQ22XX/F3TXII7L1AQ22XX.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=c1144af8a6702f1789aac832802d33bd",
        videoUrl="",
    )


    minecraft_torch4=Instruction(
        projectId= 9,
        stepOrder= 4,
        stepTitle= 'Build the Circuit',
        instructions= """
        Grab your CR2032 Battery, a White Jumbo 10mm LED, and some Maker Tape...
        Build your circuit as shown on template you printed out.
        Note that we'll use a "Tape Loop" (a small loop of Maker Tape) beneath the battery to stick it down.
        Maker Tape is conductive all the way through so it can secure our battery and allow current to flow. (Most copper tapes is not conductive on both sides so a tape loop will not work.)
        """,
        photoUrl="https://content.instructables.com/ORIG/FUW/M3HV/L1AQ244V/FUWM3HVL1AQ244V.png?auto=webp&frame=1&width=565&height=1024&fit=bounds&md=ab9e7bd91d165c157fd0959537e2bb05",
        videoUrl="",
    )

    minecraft_torch5=Instruction(
        projectId= 9,
        stepOrder= 5,
        stepTitle= 'Assemble Pieces',
        instructions= """
        Once you've got your circuit working you can assemble each piece.
        Fold the edges together and use tape to attach them.
        Once you've got both pieces assembled you can stick them together!
        """,
        photoUrl="https://content.instructables.com/ORIG/FH9/MEMM/L1AQ22YT/FH9MEMML1AQ22YT.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=a3af1b4d8fc083801d06c50f5f8182ff",
        videoUrl="",
    )

    minecraft_torch6=Instruction(
        projectId= 9,
        stepOrder= 6,
        stepTitle= 'Enjoy Your Torch!',
        instructions= """
        You've now got a Light-up MINECRAFT-Inspired Torch!
        Have Fun!
        """,
        photoUrl="https://content.instructables.com/ORIG/FP0/24BW/L1AQ22ZO/FP024BWL1AQ22ZO.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=2b53e5298f202b22c84e8ed2e8044728",
        videoUrl="",
    )

    minecraft_torch7=Instruction(
        projectId= 9,
        stepOrder= 7,
        stepTitle= 'Check Out the Other Projects',
        instructions= """
        If you've already downloaded the PDF you may have seen the other project templates.
        Try building these as well. (The assembly techniques are all pretty similar.)
        A few of them use a vibrating motor instead of an LED and will move around instead of lighting up!
        """,
        photoUrl="https://content.instructables.com/ORIG/F4Y/BMJD/L1AQ24KM/F4YBMJDL1AQ24KM.jpg?auto=webp&frame=1&crop=3:2&width=800&height=1024&fit=bounds&md=ccb022a3073c05b57df028ebe30400e0",
        videoUrl="",
    )

    giant_matches1=Instruction(
        projectId=10,
        stepOrder=1,
        stepTitle="The Match Sticks", 
        instructions="""
        Measure out a desirable length of balsa wood and cut it to get the base for our giant match. I'm using balsa because it is super easy to cut and shape later, and it also burns better than ordinary wood.

        For the cutting, I used a tiny saw to get a very clean edge.
        """,
        photoUrl="https://content.instructables.com/ORIG/FTB/XTNI/L4LBOHR2/FTBXTNIL4LBOHR2.jpg?auto=webp&frame=1&crop=3:2&width=300&height=1024&fit=bounds&md=879e974f05832f418801e15aa714928a",
        videoUrl="",
    )

    giant_matches2=Instruction(
        projectId=10,
        stepOrder=2,
        stepTitle="Shaping the Head of the Match", 
        instructions="""
        When you look closely at a real match, you'll see that the head of the match is a lot larger than the stick. To make your matches look like the real deal, you can use some thin balsa wood and glue it around the end of the matchstick. Then, using a sharp cutter, round off the edges so that the match head looks like a sphere - don't worry about the surface finish as it will be covered up.
        """,
        photoUrl="https://content.instructables.com/ORIG/FZX/15EN/L4LBOHZ2/FZX15ENL4LBOHZ2.jpg?auto=webp&frame=1&crop=3:2&width=600&height=1024&fit=bounds&md=1b2c51ee786618707f65f6f347f38bd8",
        videoUrl="",
    )

    giant_matches3=Instruction(
        projectId=10,
        stepOrder=3,
        stepTitle="The Fuel", 
        instructions="""
        Commercial matches are made essentially out of potassium chlorate and sulfur. To save ourselves from the hustle of resourcing those hard-to-find and hazardous components, let's utilize some real matches for this project.

        Use a knife to scrape away the hard material from the match heads. In my case, I needed the fuel of one box of matches (60 matches inside) for one giant match.

        Once the matches are scraped, pour all the pieces of match head in a mortar and grind them until you get a granular dust.
        """,
        photoUrl="https://content.instructables.com/ORIG/F7Y/P59O/L4LBOHVY/F7YP59OL4LBOHVY.jpg?auto=webp&frame=1&crop=3:2&width=300&height=1024&fit=bounds&md=49ea398e2a7e4a022c46c132b0219cf0",
        videoUrl="",
    )

    giant_matches4=Instruction(
        projectId=10,
        stepOrder=4,
        stepTitle="Coloring", 
        instructions="""
        To make the end result more uniform, use a marker to color the match head.
        """,
        photoUrl="https://content.instructables.com/ORIG/FF0/CWWM/L4LBOI6T/FF0CWWML4LBOI6T.jpg?auto=webp&frame=1&crop=3:2&width=800&height=1024&fit=bounds&md=0162ef1586c9a4e62b7e44e536bab33d",
        videoUrl="",
    )

    giant_matches5=Instruction(
        projectId=10,
        stepOrder=5,
        stepTitle="Gluing", 
        instructions="""
        Apply superglue on the end of your matchstick and sprinkle the match fuel on top of it. Make multiple passes to make sure all the sides are covered.

        That's it, the giant match is now done and ready for use! Repeat the same steps for the rest of the matches.
        """,
        photoUrl="https://content.instructables.com/ORIG/F2K/82MM/L4LBOID1/F2K82MML4LBOID1.jpg?auto=webp&frame=1&crop=3:2&width=900&height=1024&fit=bounds&md=172eb6a1e6bd331454605f9f9e3276d4",
        videoUrl="",
    )

    giant_matches6=Instruction(
        projectId=10,
        stepOrder=6,
        stepTitle="The Matchbox", 
        instructions="""
        For the box, I used some 1/16-inch cardboard. The designing procedure is fairly straightforward, and you can use a commercial matchbox as a reference.

        Essentially you will have first a box that has no cover, that will fit into a slightly larger box that misses two side pieces. To be exact, the larger box is 1/8 inch larger and 1/8 taller than the smaller one (but those numbers vary on the thickness of the cardboard you're using).

        To glue the cardboard, superglue works remarkably well, but hot glue is also good - though it's messier.
        """,
        photoUrl="https://content.instructables.com/ORIG/FX4/NDK5/L4LBOIME/FX4NDK5L4LBOIME.jpg?auto=webp&frame=1&crop=3:2&width=300&height=1024&fit=bounds&md=65f28e49ef732f218b43d9b9b1b16dc6",
        videoUrl="",
    )

    giant_matches7=Instruction(
        projectId=10,
        stepOrder=7,
        stepTitle="The Label", 
        instructions="""
        As a final touch, I designed a quick label using Autocad, as it allows me to use precise dimensions that I can set to be printed out with a 1:1 scale - the PDF file for my box is in the attachments. If you don't fancy using a computer to design your label, feel free to use a ruler or whatever old-school technology you're comfortable with.

        I cut out parts of my label and placed a sheet of yellow paper behind it, as I don't have a color printer.

        Finally, I salvaged the striking surfaces from the boxes of matches that were used in previous steps, and glued them to the side of the giant matchbox.
        """,
        photoUrl="https://content.instructables.com/ORIG/FVE/XNF3/L4LBOISM/FVEXNF3L4LBOISM.jpg?auto=webp&frame=1&crop=3:2&width=900&height=1024&fit=bounds&md=3f931c52b2b6d853281fbe0d4b234105",
        videoUrl="",
    )

    giant_matches8=Instruction(
        projectId=10,
        stepOrder=8,
        stepTitle="Done!", 
        instructions="""
        And here it is! A very big box for some giant matches. Only one more thing to find out: will those matches actually burn?

        Surprisingly, they work really good. They can be lit up with just one stroke, and once they produce a spark, they turn into a big ball of fire. However, the matchstick won't light up quickly enough to be of any use, so if you want to make a camping fire in the forest, you better be quick once you have lit your match.

        All in all, I'm pretty happy with how this project turned out. It's the first time I made a XXL version out of a small everyday item, and it was such a fun challenge that I will probably do it again in the future.

        Thank you for reading and have a nice day! :)
        """,
        photoUrl="https://content.instructables.com/ORIG/FQF/2B7L/L4LBOOR6/FQF2B7LL4LBOOR6.jpg?auto=webp&frame=1&crop=3:2&width=900&height=1024&fit=bounds&md=5ec91b742bb8da7c51ce0822980b328d",
        videoUrl="",
    )

    bike_lamp1=Instruction(
        projectId=11,
        stepOrder= 1,
        stepTitle="Bike Lamp Design, the Main Lamp Body", 
        instructions="""
        This Lamp doesn't need to be anything fancy design wise, the LED's soldered PCB is square shaped as is the Battery holder albeit smaller in diameter, so this design will be a simple oblong square shape.

        Using Fusion 360, and using the Top plane, I create a square of 46mm then offset this outwards by 2mm this will be the wall thickness, I want to slot a piece of Acrylic into the oblong to protect the Led's so I make another centre square at 38mm this will create a lip when we drop the piece of Acrylic in, or clear plastic sheet off cut, whatever I have available.

        To Extrude I highlight the inner lip first and extrude this to 2mm, then clicking on sketches again, I select the 2mm wall part and extrude this to 80mm, this will give us enough play internally to mess about with cables later, the LED and Battery holder overall length is approx 67mm, I apply a fillet to all 4 corners of the body of 1mm.

        I'm going to create a Push in fit base to this lamp on this there will be a connector for the Mini USB connector so I can power it from the Bikes own electrics and also a on off on switch to select between battery power or USB power.

        The lid will be secured with 2no 3mm Allen head bolts say around 5 or 6mm whatever I can find so with this mind I need to create 2 side holes @3.2mm to accept the bolts, I can project these holes onto the base part later.

        Onto creating a Base or Lid for the Lamp:
        """,
        photoUrl="https://content.instructables.com/ORIG/FAT/DZBI/L2DB2HYS/FATDZBIL2DB2HYS.png?auto=webp&frame=1&crop=3:2&width=900&height=1024&fit=bounds&md=a9e660199a36fd58015e519de18f71f1",
        videoUrl="",
    )

    bike_lamp2=Instruction(
        projectId=11,
        stepOrder=2,
        stepTitle="Creating the End Cap for the Lamp", 
        instructions="""
        After creating a new sketch and using the 2mm top of the wall to sketch to, I use project to highlight the top of the main body of the lamp, selecting the inner line of the wall, I offset this to 0.3mm inboard, this will give the end cap enough clearance for a snug fit hopefully then offset again to 2mm to create the inner wall of the lid, sounds a bit confusing? I will add plenty of screen shots for reference as always.

        Using the extrude tab, I highlight this inner wall then extrude down to 5mm creating a new Component as we go, then the main section of the end cap can be highlighted and extruded to 2mm.

        On the base I need to create a slot for the mini USB connector which will be internal and also a slot for the switch this will also be fitted from the inside.

        The slot dimensions are added to the sketch and extruded, the Mini USB adapter is on a small PSB I need to create a lip on the inner of the end cap for this to be secured to with CA or Hot glue, this is a rectangle just below the slot then extruded to 10mm.

        Update: I didn't leave enough space when fitting the end cap to the main body of the lamp, so I adjusted the end cap to leave more space, now rather than the end being inserted into the main body so its flush, it is now the same diameter as the main body with an insert which locates into the lamp, a lot better idea all round.

        This finishes the end cap.

        We can now move onto the Electrics:
        """,
        photoUrl="https://content.instructables.com/ORIG/F78/01SI/L2EQF3PT/F7801SIL2EQF3PT.jpg?auto=webp&frame=1&width=400&height=1024&fit=bounds&md=1ed37d8b34d46ed2006dd97080833f02",
        videoUrl="",
    )

    bike_lamp3=Instruction(
        projectId=11,
        stepOrder= 3,
        stepTitle="Lamp Electrics.", 
        instructions="""
        The Bike Lamp will have a dual feed, It can either be run off the inboard batteries or the Bikes own battery via the onboard USB port.

        The switch I have has 2 soldering points for the centre poles and 2 poles for each way which is handy for this purpose, I will use one of the ways from the batteries, I need to install a Buck converter to drop the 6v battery power down to 5v for the LED's so from the converter the 5v and Gnd from the batteries will go directly to the to the Buck converter IN then out of the converter, the 5v will go to one of the centre poles on the switch the ground along with the gnd from the USB pcb are soldered together and then soldered to the gnd wire from the LED and sleeved, the same applies to the 5v from the LED this will have a Switched battery feed and also a switched USB supplied feed then I can leave the lamp attached to the bike at all times and just switch it off rather than unplug the cable each time if indeed I ever have to use it.

        The Assembly:
        """,
        photoUrl="https://content.instructables.com/ORIG/F78/01SI/L2EQF3PT/F7801SIL2EQF3PT.jpg?auto=webp&frame=1&width=400&height=1024&fit=bounds&md=1ed37d8b34d46ed2006dd97080833f02",
        videoUrl="",
    )

    bike_lamp4=Instruction(
        projectId=11,
        stepOrder= 4,
        stepTitle="Assembling the Lamp and Designing and Making the Bracket.", 
        instructions="""
        I need a bracket to attach the lamp to the handlebar of the bike, I'm going to make it a more permanent feature and for this reason it needs to be more secure so I'm thinking of a clamp based design secured with Allen head 3mm bolts and washers and locknuts.

        To start with I get the diameter of the handlebar(22.5mm) then I select the top plane and sketch a rectangle of 50 x 6mm we are looking down on this bracket from a side view, the next thing to do is sketch a circle then off set it outwards until it sinks into the rectangle we created.

        We now need to make it into 2 separate components, rather than me explain the process, the screen shots can explain it a lot better, there needs to be a gap between both components so that it can clamp onto the handlebar, to achieve this we can insert more lines and use the trim tool to delete lines we no longer need to ease the extrude process then we need to make holes for for the bolts to go through, on the nut side I've used a circumscribed Polygon, this is made using half the dimension of the nuts between the flats and adding a little for clearance, we only have to do this on one side of the clamp, we can mirror using features to mirror to the other side using the centre plane.

        A few fillets are added to finish these 2 components.
        """,
        photoUrl="https://content.instructables.com/ORIG/FJB/FUCF/L2DB2KGM/FJBFUCFL2DB2KGM.png?auto=webp&frame=1&crop=3:2&width=900&height=1024&fit=bounds&md=c8bea2a3e1af90df2ef2ccbdbec5a471",
        videoUrl="",
    )

    bike_lamp5=Instruction(
        projectId=11,
        stepOrder= 5,
        stepTitle="First Test of the Lamp at Night and Assumptions", 
        instructions="""
        I wanted to test the light in the dark and compare it to my normal front bike light and I was presently surprised, the coverage right in front of you which is really what you want to see for the ever growing number of Pot holes etc was very very good, and the light does what it says on the tin, it works very well on its own battery power and switching over to the Bike battery there was no difference, the clamp works well and holds really good, the height can be adjusted to suit.

        I quite like the square lamp, it looks radical, a bit like the weapon the predator has on its shoulder, well ish! I didn't realise until I'd finished it that I also had a round 5v led lamp, I soldered the resistors and LED's as per the Instructions, and then set about designing a cylindrical lamp as well, the only difference being is that the round lamp only has 3 batteries in a holder, AAA this time, so it will have the same switch and Mini usb connector and will be wired pretty much the same but omitting the Buck converter, the design priciples are the same as the square lamp, I cut a piece of 4mm Acrylic for the Lens on the CNC machine for ease, I feared I would make a mess cutting on the band saw.

        The Lights look different that's a fact and were very enjoyable to make, and with the USB as well as battery option it could get me out of a situation, you never know, and save me getting a fine.

        I might try another lamp at some point with a 9v Battery and Buck Converter.

        Thanks for looking in!
        """,
        photoUrl="https://content.instructables.com/ORIG/FTI/EU3K/L2EQF4XR/FTIEU3KL2EQF4XR.jpg?auto=webp&frame=1&width=247&height=1024&fit=bounds&md=f9488456d3a1d6bbd20d13d0e5539991",
        videoUrl="",
    )   

    rainbow1=Instruction(
        projectId=12,
        stepOrder= 1,
        stepTitle="Designing Your 3D Print", 
        instructions="""
        Now, you could probably do this with most prints, but my recommendations is to make sure your design has a nice flat surface (this rainbow effect won't go up curved sides, only the side that is touching the build plate), and the thicker the lines, the more rainbow reflectiveness you'll get!

        I used a teardrop/raindrop shape that I imported and combined that with a Voronoi adjustable shape from the Shape Generators section of the shapes panel.
        """,
        photoUrl="https://content.instructables.com/ORIG/FGX/34KN/L4R1CQ74/FGX34KNL4R1CQ74.png?auto=webp&frame=1&crop=3:2&width=605&height=1024&fit=bounds&md=bb90f170a23d80b1d7bb9d036e2408d0",
        videoUrl="",
    )   

    rainbow2=Instruction(
        projectId=12,
        stepOrder= 2,
        stepTitle="Prep Your Printer", 
        instructions="""
        This is, obviously, the most important part for getting your rainbow prints.

        In the past articles I had seen, others had either taped down the edges of the sheet or used a sticky sheet to completely convert a printer bed into a rainbow surface. The first option is what I tried and my prints constantly curled up, and the second I just wasn't ready to attempt. So I came up with an option in between that works great for me!

        *I'm doing this on a spare spring steel sheet for my Prusa, but this is not permanent, so you should be able to do this and undo it whenever you need. It is meant to last, but not meant to last forever.

        First, start by figuring out which side is rainbow (they aren't both rainbow).

        Rub it between your fingers. One finger will catch and one will slide. The side the slides, should go up (I thought it would be the opposite but it isn't). If you print on the wrong side, your print will be shiny smooth but not rainbow reflective.

        Now time to put the sheet down.

        Start by cutting off a sheet of your diffraction grating roll.
        I've only ever seen this stuff in 6" width so if you can find a bigger sheet, that's great.
        Make sure your sheet isn't bent or wrinkled, it will wreck the finished result of the print.
        Figure out what space it will cover (likely the middle) and put glue stick down on the build plate to cover the whole area the sheet will cover.
        Carefully lay down the sheet and get as many bubbles out as you can.
        I tried to use cardboard or a squeegee type object (these didn't work for me), but be careful about scraping the glue underneath the sheet through the diffraction grating sheet as that can also wreak the finish of the finished print.
        Once it's all smoothed out, tape all edges down with blue painters tape.
        Done!
        It is very easy to take off the tape, carefully peel off the sheet, and wash both the sheet and the bed to get the glue off. I've done this a couple times already actually as the more you bend the sheet, the more it will start to pull up from the glue. I've reused the same diffraction grating sheet over and over too after carefully cleaning it.
        """,
        photoUrl="https://content.instructables.com/ORIG/F2M/REJO/L4R1CPW9/F2MREJOL4R1CPW9.jpg?auto=webp&frame=1&width=400&height=1024&fit=bounds&md=700911c679eea62a9f154d598cbfec67",
        videoUrl="",
    )  

    rainbow3=Instruction(
        projectId=12,
        stepOrder= 3,
        stepTitle="Check First Layer Height", 
        instructions="""
        My Prusa allows me to have settings for different sheets, so I did a different first layer setting for my "rainbow" sheet. It doesn't add much thickness, but it also doesn't hurt to get new settings to make sure that first layer works right. If you print too close, you could meld your print to the sheet, though this hasn't happened to me yet.
        """,
        photoUrl="https://content.instructables.com/ORIG/FNS/AOKK/L4R1CPWD/FNSAOKKL4R1CPWD.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=cee23af43a05b904a7bb6c2f32ae39ea",
        videoUrl="",
    )  

    rainbow4=Instruction(
        projectId=12,
        stepOrder= 4,
        stepTitle="Final Prints!", 
        instructions="""
        Have fun printing your designs!

        I haven't noticed needing any special settings to get these to work right.
        """,
        photoUrl="https://content.instructables.com/ORIG/F04/4BVY/L4R1CJET/F044BVYL4R1CJET.jpg?auto=webp&frame=1&width=785&height=1024&fit=bounds&md=1e8787a29659bfa80ebe688e35fe80e0",
        videoUrl="",
    )  

    frankenstein1=Instruction(
        projectId=13,
        stepOrder= 1,
        stepTitle="The Monster Hospital- Frankenstein ER", 
        instructions="""
        The first part of this activity is the monster hospital.  I have a collection of Frankenstien candy games that have been built over the years, which I intentionally break: a foil mouth that has a gap, positive and negative wires reversed, missing eyes, dead batteries, loose connections….Before,  I give each team a patient to repair, we review electrical circuits and I stress test, test, test the individual parts of the circuits.  Check the battery, check the buzzer, check the connections, check the circuit, identify the parts.  The teams then work to fix their mangled monster, once a monster head is working properly it is moved to the recovery area.  The recovery area is a resource and reference for all students.  Once a team has successfully repaired their monster, they are now considered  doctors and may build their own monster and offer advice to other teams.  I am the hospital director (always wear my lab coat for this activity) so before they ask me for help they must confer with at least two other doctors. 

        As the hospital director, my main role is safety.  I stress that I must cut any starting points for cutting.  Anyone trying to puncture the bottle with scissors or pencils will lose their hospital privileges.  I am always impressed at the ability of my students to successfully rise to the challenge and build their own monsters with only guiding questions from me.  The first time I did this activity we built the heads step by step as a group, still very fun, but the “hospital activity” is an easy assessment product.  For example, some wires on the supply table can have stripped ends, but not all or some batteries can be dead, which allows me to observe each student's problem solving and knowledge of circuits.
        """,
        photoUrl="https://content.instructables.com/ORIG/FIN/5Y7M/L3YGJH8D/FIN5Y7ML3YGJH8D.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=76331cc2fa427914bc46c395269dfadf",
        videoUrl="",
    )  

    frankenstein2=Instruction(
        projectId=13,
        stepOrder=2,
        stepTitle="The Monster’s Complexion", 
        instructions="""
        Spray paint is the quickest and best method to produce a glowing green complexion and frightful hairdo. Spray paint the bottom and about an inch of the bottle purple. Spray paint the rest green. This is the only step that I do not let students do. I have the students bring in the bottles several weeks before the project, so I can paint them. Remember, KEEP the caps. If you don’t want to spray paint, green soda bottles can be used and the hair can be colored with a black sharpie marker.
        """,
        photoUrl="https://content.instructables.com/ORIG/FLG/R7J9/L3YGJH9L/FLGR7J9L3YGJH9L.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=ce7d703d03c597fb171df9beee1fbffa",
        videoUrl="",
    ) 

    frankenstein3=Instruction(
        projectId=13,
        stepOrder=3,
        stepTitle="Snip, Snip Perfect Hair", 
        instructions="""
        Make a small slit near the bottom of the bottle with a utility knife. (Adult only) Cut all the way around the bottom of the bottle, once the slit is made kid scissors work fine. Remove and save the bottom of the bottle. Snip triangles all the way to form the hair.
        """,
        photoUrl="https://content.instructables.com/ORIG/FEE/1T29/L3YGJHAW/FEE1T29L3YGJHAW.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=68ddb3c82094c4494e6e090a73af6671",
        videoUrl="",
    ) 

    frankenstein4=Instruction(
        projectId=13,
        stepOrder=4,
        stepTitle="Open Wide- the Mouth", 
        instructions="""
        The mouth is a key feature of the monster.  It is how the candy will be accessed, too big the game is too easy, too small and the game is too frustrating. Cutting the mouth just a little bigger than a deck of cards seems to work. Cut a strip of foil about 2 inches wide and slightly longer than the perimeter of the mouth.  Fold the foil in half and glue around both the inside and outside perimeter of the mouth.

        Tip- if the mouth is cut too large, teeth can be added to make the area smaller
        """,
        photoUrl="https://content.instructables.com/ORIG/F49/MULW/L3YGJHDB/F49MULWL3YGJHDB.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=d01867427df4f2dfd6a89683fd2d5a24",
        videoUrl="",
    ) 

    frankenstein5=Instruction(
        projectId=13,
        stepOrder=5,
        stepTitle="Neck( Actually Ear) Bolts", 
        instructions="""
        All great monsters need neck bolts.  These neck bolts have several jobs; they link the mouth “switch” into the circuit, they support the lid to reduce candy snatching thru the top of the head and they are a convenient spot to hang the tweezers when the game is not being played.  Two large side bolts work the best and a row of decorative bolts across the back of the head add interest and help support the lid.  Make sure to position the bolts above the top of the mouth.
        """,
        photoUrl="https://content.instructables.com/ORIG/FBY/03PK/L3YGJHES/FBY03PKL3YGJHES.jpg?auto=webp&frame=1&width=400&height=1024&fit=bounds&md=50891352b93dc489d9579b01cd0482ba",
        videoUrl="",
    ) 

    frankenstein6=Instruction(
        projectId=13,
        stepOrder= 6,
        stepTitle="Eyes /scars", 
        instructions="""
        The eyes can be painted on with craft paint or cut out of construction paper and glued. The scars can also be either painted on with craft paint or drawn with a Sharpie marker. The final product is a monster so scrapes, scratches and nicks are great and reduce the need for a perfect product and allow the focus to be on a working circuit.
        """,
        photoUrl="https://content.instructables.com/ORIG/FSE/42UJ/L3YGJHER/FSE42UJL3YGJHER.jpg?auto=webp&frame=1&width=800&height=1024&fit=bounds&md=a5e315698afb9c4d5d057cdef225cc9e",
        videoUrl="",
    ) 

    frankenstein7=Instruction(
        projectId=13,
        stepOrder=7,
        stepTitle="The Base", 
        instructions="""
        Use a drill or nail, to make a hole in the bottle cap.  Use a wood screw, attach the cap to the base. The game's level of difficulty can be adjusted with the screw.  If the cap is secured securely the game is easier because the bottle will not wobble.  If it is loosely attached the bottle will wobble and make the game more difficult.  Attach the bottle to the base.
        """,
        photoUrl="https://content.instructables.com/ORIG/F7L/IVST/L3YGJHMS/F7LIVSTL3YGJHMS.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=d07b9ba4db8b4dc41114a4d534a470ef",
        videoUrl="",
    ) 

    frankenstein8=Instruction(
        projectId=13,
        stepOrder=8,
        stepTitle="Connecting the Circuit", 
        instructions="""
        The switch- connect the foil mouth to an ear bolt, secure with duct tape.  This connection can be either inside or outside the bottle.  Since, you are building a monster, curling wires and duct tape add to the final product.

        Test the buzzer directly to the battery.  Note that the buzzer has polarity.  It will only work if the negative lead is connected to the negative terminal. Strip the ends of about 12 inches of wire, secure  to a battery  terminal with a small piece of duct tape.  Test your connection.  Then connect the other end of the wire to the ear bolt that is connected to the mouth.

        Add another wire to the other battery terminal, connect to one wire of the buzzer. Remember polarity. Check connection

        Connect a wire to the tweezers.  A wire with alligators clips is a nice option, because this connection is pulled and yanked as the game is played.  Due to expense, I only give each student one wire with alligator clips.  The connection can be made without alligator clips, just make sure the connection is taped well.  Connect the other end of the wire to the buzzer. To test connection, touch the ear bolt connected to the battery.  Then test the mouth connection, by touching the tweezers to all parts of the mouth.

        Use Velcro dots to secure the battery and buzzer to the base and your monster is ready to guard your candy
        """,
        photoUrl="https://content.instructables.com/ORIG/FJU/25NV/L3YGJKQN/FJU25NVL3YGJKQN.jpg?auto=webp&frame=1&width=800&height=1024&fit=bounds&md=e2f4dc19cd1a30bf426ba9dc9673bf9f",
        videoUrl="",
    ) 

    frankenstein9=Instruction(
        projectId=13,
        stepOrder=9,
        stepTitle="Frankenstein Fun", 
        instructions="""
        A candy snatch game makes learning about circuits fun.  It also creates a product that students are able to share and explain to their families and friends, which is the point of learning.
        """,
        photoUrl="https://content.instructables.com/ORIG/FBP/HOVD/L3YGJKRK/FBPHOVDL3YGJKRK.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=44b4a891add7b2f157b0d8baf7f96a50",
        videoUrl="",
    ) 

    ice_cream1=Instruction(
        projectId=14,
        stepOrder=1,
        stepTitle="Make the Chocolate Fudge", 
        instructions="""
        In a small microwave-safe bowl add oil and chocolate chips. Next heat the mixture for one minute. Mix it well so it isn't too thick.
        """,
        photoUrl="https://content.instructables.com/ORIG/FXK/9TLJ/L4LBMVUJ/FXK9TLJL4LBMVUJ.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=d4da1f5077bac7c00a94eef314a0a581",
        videoUrl="",
    )

    ice_cream2=Instruction(
        projectId=14,
        stepOrder=2,
        stepTitle="Scoop ice cream into cone", 
        instructions="""
        Put the ice cream in the cone and get ready to dip it.
        """,
        photoUrl="https://content.instructables.com/ORIG/FOG/7WQZ/L4LBMV6E/FOG7WQZL4LBMV6E.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=528c24f6c076cfb020faa1a109f0a3cc",
        videoUrl="",
    )

    ice_cream3=Instruction(
        projectId=14,
        stepOrder=3,
        stepTitle="Add the Fudge Mixture", 
        instructions="""
        Dip the ice cream in the fudge mixture.
        """,
        photoUrl="https://content.instructables.com/ORIG/FUU/N0C4/L4LBMWQO/FUUN0C4L4LBMWQO.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=54376b5f0d2c5f28ff158bb954ca2301",
        videoUrl="",
    )

    ice_cream4=Instruction(
        projectId=14,
        stepOrder=4,
        stepTitle="", 
        instructions="""
        Quickly and softly roll the ice cream over the peanuts
        """,
        photoUrl="https://content.instructables.com/ORIG/FQR/UBSN/L4LBMZK1/FQRUBSNL4LBMZK1.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=922869171129c40572fcefbb9e5e289b",
        videoUrl="",
    )

    ice_cream5=Instruction(
        projectId=14,
        stepOrder=5,
        stepTitle="The End", 
        instructions="""
        Now you can finally dig in.
        """,
        photoUrl="https://content.instructables.com/ORIG/FYJ/7848/L4LBNCVX/FYJ7848L4LBNCVX.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=75e25aab8c28a7b171929c0ce79f5d72",
        videoUrl="",
    )

    hot_chocolate1=Instruction(
        projectId=15,
        stepOrder=1,
        stepTitle="Flavoring", 
        instructions="""
        To begin put milk, cream, powdered sugar, cinnamon and nutmeg over medium heat. Then stir it all together.
        """,
        photoUrl="https://content.instructables.com/ORIG/FR8/355M/KZ9UM21K/FR8355MKZ9UM21K.jpg?auto=webp&frame=1&crop=3:2&width=400&height=1024&fit=bounds&md=cb38e6a6a223aa66182978c228718e1d",
        videoUrl="",
    )

    hot_chocolate2=Instruction(
        projectId=15,
        stepOrder=2,
        stepTitle="Adding Chocolate", 
        instructions="""
        Once your milk mixture is almost boiling remove it from heat and add chocolate chips. Stir them in until completely melted. Then leave it on low to stay warm.
        """,
        photoUrl="https://content.instructables.com/ORIG/FDU/LJJ0/KZ9UM3U0/FDULJJ0KZ9UM3U0.jpg?auto=webp&frame=1&crop=3:2&width=600&height=1024&fit=bounds&md=bcdc3883c5833c04c6401e855c4f841f",
        videoUrl="",
    )

    hot_chocolate3=Instruction(
        projectId=15,
        stepOrder=3,
        stepTitle="Whipped Cream", 
        instructions="""
        While you Hot Chocolate is staying warm on low you can make some whipped cream! To do this put your heaving whipping cream into your kitchen aid and stir it at six. then mix for about five minutes or until desired consistency.
        """,
        photoUrl="https://content.instructables.com/ORIG/F1G/RA2D/KZ9UM3UQ/F1GRA2DKZ9UM3UQ.jpg?auto=webp&frame=1&crop=3:2&width=400&height=1024&fit=bounds&md=7e0b1ccce7ffb52286a0f0237edc9b00",
        videoUrl="",
    )

    hot_chocolate4=Instruction(
        projectId=15,
        stepOrder=4,
        stepTitle="Topping It Off", 
        instructions="""
        Now you can have as much fun as you want making your Hot Chocolate look appetizing! Once I put the whipped cream on top I sprinkled on some cinnamon this had a delicious looking affect!
        """,
        photoUrl="https://content.instructables.com/ORIG/FN8/TBD6/KZ9UMDIO/FN8TBD6KZ9UMDIO.jpg?auto=webp&frame=1&width=481&height=1024&fit=bounds&md=054cc03050fbc605a7f9d58faec07483",
        videoUrl="",
    )

    hot_chocolate5=Instruction(
        projectId=15,
        stepOrder=5,
        stepTitle="Enjoy!", 
        instructions="""
        To fully enjoy your French Hot Chocolate follow the four S's. First sniff the amazing aroma, then sip slowly, next savor it and let it soak into your taste buds, then swallow.
        """,
        photoUrl="https://content.instructables.com/ORIG/F93/LQGK/KZ9UMFIT/F93LQGKKZ9UMFIT.jpg?auto=webp&frame=1&width=499&height=1024&fit=bounds&md=4ce9a4cbe94ab8332dc66f13d72ffa5c",
        videoUrl="",
    )

    cocoa_bomb1=Instruction(
        projectId=16,
        stepOrder=1,
        stepTitle="Coco Bombs", 
        instructions="""
        To start out, put 3 TBSP of maple syrup in a small bowl then slowly mix in 2/3 cup Hershey's cocoa powder. This may take a while to get all the cocoa powder into the syrup, but it ends up resembling cookie dough. If it is not molding correctly you can add a little bit more syrup to bond it.
        """,
        photoUrl="https://content.instructables.com/ORIG/FCQ/KAXZ/KV3TDYV4/FCQKAXZKV3TDYV4.jpg?auto=webp&frame=1&width=932&height=1024&fit=bounds&md=a5d634e618f60df8791473400b9fe683",
        videoUrl="",
    )

    cocoa_bomb2=Instruction(
        projectId=16,
        stepOrder=2,
        stepTitle="Shaping", 
        instructions="""
        Shape your cocoa mixture into teaspoon-sized balls.
        """,
        photoUrl="https://content.instructables.com/ORIG/F33/CVUG/KV3TDYYT/F33CVUGKV3TDYYT.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=7caf422754ba0449cbf5d4abe9b01643",
        videoUrl="",
    )

    cocoa_bomb3=Instruction(
        projectId=16,
        stepOrder=3,
        stepTitle="More Shaping", 
        instructions="""
        Shape out more bombs for future use!
        """,
        photoUrl="https://content.instructables.com/ORIG/FV7/DQVX/KV3TDZ1G/FV7DQVXKV3TDZ1G.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=6f50a0da8c92425ae23341dc02cd1bbf",
        videoUrl="",
    )

    cocoa_bomb4=Instruction(
        projectId=16,
        stepOrder=4,
        stepTitle="Hot Coco", 
        instructions="""
        Microwave 2/3 cups milk for 2 minutes or until foaming then add in one or two cocoa bombs and stir until fully melted then enjoy. you can add more syrup or sweetener of your choice so it is sweeter. I added a little bit of cinnamon for a kick of spice
        """,
        photoUrl="https://content.instructables.com/ORIG/FN6/AVJM/KV3TDZK6/FN6AVJMKV3TDZK6.png?auto=webp&frame=1&width=515&fit=bounds&md=64070c3a44149b9f4cf40a28328c0dd3",
        videoUrl="",
    )

    blossom1=Instruction(
        projectId=17,
        stepOrder=1,
        stepTitle="Applying Paint to the Candle Jar", 
        instructions="""
        Start with taking your candle jar and applying your acrylic paint. I combined both colors when I applied it onto my candle jar. Be sure to allow your paint to dry between coats. I used a blow dryer to help with drying. I applied around three coats of paint.
        """,
        photoUrl="https://content.instructables.com/ORIG/F9B/ZPBB/L4PLX75S/F9BZPBBL4PLX75S.png?auto=webp&frame=1&width=600&fit=bounds&md=bd904319753cb33a1ce501f7cdc82b6c",
        videoUrl="",
    )

    blossom2=Instruction(
        projectId=17,
        stepOrder=2,
        stepTitle="Cutting Foam Block to Size", 
        instructions="""
        Next, take your scissors, or if you have a craft knife, use it to split your foam block in half. Depending on the size of your candle jar, be sure you cut it to a size that will work with your jar. Take your foam block, and add it into your glass jar.
        """,
        photoUrl="https://content.instructables.com/ORIG/FSH/TPNB/L4PLX77T/FSHTPNBL4PLX77T.png?auto=webp&frame=1&width=600&fit=bounds&md=1ab3e917b8f43815b39b892296a68bae",
        videoUrl="",
    )

    blossom3=Instruction(
        projectId=17,
        stepOrder=3,
        stepTitle="Inserting Your Branch", 
        instructions="""
        After, take your branch and insert it into the middle of your foam block. I decided to use a branch I cut when my husband and I were doing our spring clean up in our yard. We had a few trees that we had to trim, and I thought it would be perfect to use a few of the branches for projects.
        """,
        photoUrl="https://content.instructables.com/ORIG/FJQ/WJPE/L4PLX79P/FJQWJPEL4PLX79P.png?auto=webp&frame=1&width=600&fit=bounds&md=8a8579d2b3a57dc11d819bf29e54766e",
        videoUrl="",
    )

    blossom4=Instruction(
        projectId=17,
        stepOrder=4,
        stepTitle="Preparing Your Floral", 
        instructions="""
        Using your floral snips, begin to cut the tops of your faux floral. You can also cut some of the greenery as well. 

        Take your hot glue, and apply it onto each floral piece, and add your floral onto your branches.

        Next, take your greenery, and use your hot glue to apply it onto the top section of your foam block. I did this to cover any areas that my foam block was visible. 
        """,
        photoUrl="https://content.instructables.com/ORIG/FS0/GF6P/L4PLX7CI/FS0GF6PL4PLX7CI.png?auto=webp&frame=1&width=600&fit=bounds&md=defd87ba7484d23e88944a94a1fa7f33",
        videoUrl="",
    )

    blossom5=Instruction(
        projectId=17,
        stepOrder=5,
        stepTitle="Your Blossom Design Is Complete", 
        instructions="""
        You're all done! Your blossom branch arrangement is all done. I love how simple this was to create, and I love that I had all of my materials on hand. I hope that you enjoyed this simple creation. Thank you so much for stopping by, and creating with me! I'll see you soon.
        """,
        photoUrl="https://content.instructables.com/ORIG/FOZ/9Z06/L4PLX7EZ/FOZ9Z06L4PLX7EZ.png?auto=webp&frame=1&width=777&fit=bounds&md=055f53fc1842898f121fa483ecfe9611",
        videoUrl="",
    )

    torus1=Instruction(
        projectId=18,
        stepOrder=1,
        stepTitle="Finding the Correct Template", 
        instructions="""
        You can go off of this Torotaller.pdf template but then you would have to use a different material. Card board is too chunky and it would be hell to construct with such bulky material if you are attempting to build a small torus. If you were to make a smaller torus I would recommend using a much more flexible material similar to the one show cased in the YouTube video that I will share with you guys on 
        """,
        photoUrl="https://content.instructables.com/ORIG/FYN/Z5K9/L42QVJIX/FYNZ5K9L42QVJIX.jpg?auto=webp&frame=1&crop=2:3&width=467&height=1024&fit=bounds&md=69b0f18fabdf67e0d928cb0ebc55329d",
        videoUrl="",
    )

    torus2=Instruction(
        projectId=18,
        stepOrder=2,
        stepTitle="Decide on What Size You Want Your Torus to Be", 
        instructions="""
        The one that I used for the Mouquet (the one that I am holding in my hand) I used a illustration board which is not really recommend unless if you size up the template. You can see how there was a tiny bit of struggle in the smallest torus with the illustration board but as a I progressed to larger sizes it was much easier to manipulate the illustration board resulting in a much cleaner finish.
        """,
        photoUrl="https://content.instructables.com/ORIG/FN6/5BMU/L42QVJUR/FN65BMUL42QVJUR.jpg?auto=webp&frame=1&width=280&height=1024&fit=bounds&md=5d0d119c7cdbcbf0ec4a6b579f52735b",
        videoUrl="",
    )

    torus3=Instruction(
        projectId=18,
        stepOrder=3,
        stepTitle="How to Construct Your Torus", 
        instructions="""
        For this step I will share with you guys a YouTube video in which this person does a great job of explains how to contrast the torus.
        https://www.youtube.com/watch?v=rft4EJkVZ9Y
        """,
        photoUrl="https://content.instructables.com/ORIG/FEU/QSK9/L42QVP8H/FEUQSK9L42QVP8H.jpg?auto=webp&frame=1&width=686&height=1024&fit=bounds&md=6118c43c5e12637c72c0731ad7e78587",
        videoUrl="",
    )


    torus4=Instruction(
        projectId=18,
        stepOrder=4,
        stepTitle="Scale Up Your Torus Template", 
        instructions="""
        In order for me to scale up on this project I used this app on my iPad called the Grid#. This will allow you to grid off one piece of the torus template. Once you gridded the torus template you have to save the image on to photos and go back to your photo library to clearly section off the gridded image in order to change the size of the torus template. Once everything is sectioned off you would then have to send you sectioned off images into a google docs to change the size of the sectioned off template. The size of the sectioned off template should not be a size to where google docs would cut your image off. I'd say when you go to image options the maximum size you could scale up to is about 8 inches. This way when you print out the sectioned off template when it prints out nothing is cut off. Once you have your torus shape at a desired shape then next you would have to print it out. After printing it out you will then have to piece together the sectioned off template so you can create and get your own customized torus stencil. I recommend piecing these together with a clear tape or semi transparent masking tape. after you have finished creating you r template it is then time to repeat that same process with the opposite side of the torus piece you were working with. Once that is complete you can start stenciling the template on to your cardboard. You will have to make 12 for each side(Toro 1 =12 Toro 2 =12).
        """,
        photoUrl="https://content.instructables.com/ORIG/FOH/1NBF/L42QVQQ5/FOH1NBFL42QVQQ5.png?auto=webp&frame=1&width=360&fit=bounds&md=b92535e4085234de6565cd2212bcce3b",
        videoUrl="",
    )

    torus5=Instruction(
        projectId=18,
        stepOrder=5,
        stepTitle="Coloring Your Torus", 
        instructions="""
        It is recommended to paint all of the templates before assembling your torus.
        """,
        photoUrl="https://content.instructables.com/ORIG/FLE/AR6N/L42QVPM8/FLEAR6NL42QVPM8.jpg?auto=webp&frame=1&width=700&height=1024&fit=bounds&md=14546db57011071f6fc957e1995ca905",
        videoUrl="",
    )

    torus6=Instruction(
        projectId=18,
        stepOrder=6,
        stepTitle="Enjoy your Torus", 
        instructions="""
        Enjoy all your hardwork!
        """,
        photoUrl="https://content.instructables.com/ORIG/FNX/531A/L42QV88N/FNX531AL42QV88N.jpg?auto=webp&frame=1&width=350&height=1024&fit=bounds&md=457cba7cf3f20e8775c0ab2408523fbb",
        videoUrl="",
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
    db.session.add(casino_clock8)
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
    db.session.add(skillet_burger1)
    db.session.add(skillet_burger2)
    db.session.add(skillet_burger3)
    db.session.add(skillet_burger4)
    db.session.add(skillet_burger5)
    db.session.add(james_webb1)
    db.session.add(james_webb2)
    db.session.add(james_webb3)
    db.session.add(james_webb4)
    db.session.add(slowmo_bird1)
    db.session.add(slowmo_bird2)
    db.session.add(dragonfly1)
    db.session.add(dragonfly2)
    db.session.add(dragonfly3)
    db.session.add(dragonfly4)
    db.session.add(arcade_stick1)
    db.session.add(arcade_stick2)
    db.session.add(arcade_stick3)
    db.session.add(arcade_stick4)
    db.session.add(arcade_stick5)
    db.session.add(arcade_stick6)
    db.session.add(arcade_stick7)
    db.session.add(arcade_stick8)
    db.session.add(minecraft_torch1)
    db.session.add(minecraft_torch2)
    db.session.add(minecraft_torch3)
    db.session.add(minecraft_torch4)
    db.session.add(minecraft_torch5)
    db.session.add(minecraft_torch6)
    
    db.session.add(minecraft_torch7)

    db.session.add(giant_matches1)
    db.session.add(giant_matches2)
    db.session.add(giant_matches3)
    db.session.add(giant_matches4)
    db.session.add(giant_matches5)
    db.session.add(giant_matches6)
    db.session.add(giant_matches7)
    db.session.add(giant_matches8)
    db.session.add(bike_lamp1)
    db.session.add(bike_lamp2)
    db.session.add(bike_lamp3)
    db.session.add(bike_lamp4)
    db.session.add(bike_lamp5)
    db.session.add(rainbow1)
    db.session.add(rainbow2)
    db.session.add(rainbow3)
    db.session.add(rainbow4)
    db.session.add(frankenstein1)
    db.session.add(frankenstein2)
    db.session.add(frankenstein3)
    db.session.add(frankenstein4)
    db.session.add(frankenstein5)
    db.session.add(frankenstein6)
    db.session.add(frankenstein7)
    db.session.add(frankenstein8)
    db.session.add(frankenstein9)
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
    db.session.add(cocoa_bomb1)
    db.session.add(cocoa_bomb2)
    db.session.add(cocoa_bomb3)
    db.session.add(cocoa_bomb4)
    db.session.add(blossom1)
    db.session.add(blossom2)
    db.session.add(blossom3)
    db.session.add(blossom4)
    db.session.add(blossom5)
    db.session.add(torus1)
    db.session.add(torus2)
    db.session.add(torus3)
    db.session.add(torus4)
    db.session.add(torus5)
    db.session.add(torus6)
    
    db.session.commit()


def undo_instructions():
    db.session.execute('TRUNCATE instructions RESTART IDENTITY CASCADE;')
    db.session.commit()