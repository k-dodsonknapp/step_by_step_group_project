from app.models.db import db
from app.models.instruction import Instruction
import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")

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

    bike_mount1=Instruction(
        projectId=19,
        stepOrder=1,
        stepTitle="Starting With the Hands", 
        instructions="""
        I used two chunks of wood for the hands

        Wood size: 3.5" x 3.5" X 5.5'

        -After drawing out the shape, cut the spaces between the fingers at about 5-6mm each on the bandsaw
        """,
        photoUrl="https://content.instructables.com/ORIG/F29/7U2B/JUGRSOQF/F297U2BJUGRSOQF.png?auto=webp&frame=1&width=765&height=1024&fit=bounds&md=604caf9f345d87ab68efa4da459a300d",
        videoUrl="",
    )

    bike_mount2=Instruction(
        projectId=19,
        stepOrder=2,
        stepTitle="Cut out side profile and rest of palms", 
        instructions="""
        -Cut out the side profile of the hand, make sure to measure your bike and make the area that holds the frame 1/8" - 1/4" bigger then the top bar of the bike frame.

        -The second step I missed in the video and it involves cutting away the rest of the palm besides the thumb, you can do this with a hand saw
        """,
        photoUrl="https://content.instructables.com/ORIG/F5F/OPJJ/JUGRSOFK/F5FOPJJJUGRSOFK.png?auto=webp&frame=1&crop=3:2&width=431&height=1024&fit=bounds&md=3ec00f48b21f8ae446d2395162430d2e",
        videoUrl="",
    )

    bike_mount3=Instruction(
        projectId=19,
        stepOrder=3,
        stepTitle="Finishing", 
        instructions="""
        Basically sand everything down to 220 grit and use whatever finish you like. I used a Poly Finish

        -use a thin piece of wood wrapped in sand paper to smooth out between the fingers.

        -use a rounded piece of wood to sand between the thumb and the fingers
        """,
        photoUrl="https://content.instructables.com/ORIG/FYS/MRTB/JUGRSO9T/FYSMRTBJUGRSO9T.png?auto=webp&frame=1&width=824&height=1024&fit=bounds&md=16d135a6dc24333e0053a57386c04bb4",
        videoUrl="",
    )

    bike_mount4=Instruction(
        projectId=19,
        stepOrder=4,
        stepTitle="The Wall Mount", 
        instructions="""
        The wall mount is made with wood that I had laying around.

        Back panel: 9" x 9"

        Horizontal piece: 6" x 11.5" Its important to make sure the bike is far enough away from the wall so the pedals don't hit the wall. The 6" plus the depth of the hand made the bike sit 8" off the wall.

        I used a pocket hole jig by milescraft to get the dowel holes in the right place.

        **If I were to do this again I would have made the back panel a at least a bit thicker.
        """,
        photoUrl="https://content.instructables.com/ORIG/F5E/IMCB/JUGRSO3U/F5EIMCBJUGRSO3U.png?auto=webp&frame=1&width=583&height=1024&fit=bounds&md=901383a6b8febf4524739801a19adef8",
        videoUrl="",
    )

    bike_mount5=Instruction(
        projectId=19,
        stepOrder=5,
        stepTitle="Mounting the Hands", 
        instructions="""
        Mount the hands using the pocket hole jig and dowels.

        Do some extra measurements here because the last thing you want is for the hands to be a little off.
        """,
        photoUrl="https://content.instructables.com/ORIG/FT0/6OSX/JUGRSO25/FT06OSXJUGRSO25.png?auto=webp&frame=1&width=798&height=1024&fit=bounds&md=14e7963f9c7e5469cbd7134cb95e58be",
        videoUrl="",
    )

    bike_mount6=Instruction(
        projectId=19,
        stepOrder=6,
        stepTitle="Hanging", 
        instructions="""
        I wanted the mount to lay flush against the wall so I embed two Keyhole Hangers, one on the top and one on the bottom.
        """,
        photoUrl="https://content.instructables.com/ORIG/FB8/JWWJ/JUGRSNUY/FB8JWWJJUGRSNUY.png?auto=webp&frame=1&width=1010&height=1024&fit=bounds&md=f75a5dfd3cfa6d41dbdaeaa01cccc631",
        videoUrl="",
    )

    bike_mount7=Instruction(
        projectId=19,
        stepOrder=7,
        stepTitle="Finished", 
        instructions="""
        I added a little support, just for some security.

        And we're done!
        """,
        photoUrl="https://content.instructables.com/ORIG/FD0/I9FH/JUGRSQ6A/FD0I9FHJUGRSQ6A.png?auto=webp&frame=1&crop=3:2&width=406&height=1024&fit=bounds&md=f8bff4051ac998d091f0d6d95861af9d",
        videoUrl="",
    )

    data_crystals1=Instruction(
        projectId=20,
        stepOrder=1,
        stepTitle="Find the Dataset", 
        instructions="""
        There are many types of data I would like to represent. It's easy to think of fun and useful possibilities such as: people's favorite lottery numbers,  income levels for every single household in San Francisco and every single shipwreck in history.

        However, in most cases the data that I want is simply unavailable, so instead, I work with what I can get.

        What is now becoming accessible is loads of data from city governments — San Francisco leads the way with its Open Data Portal with an API powered by Socrata. Since people have a daily relationship with their urban environment and connect to data patterns that reflect the city they live in, this municipal data can be compelling.

        For the first 3 Data Crystals, I chose from the SF Open Data site: construction permit data, incidents of crime and SF Civic Art Collection. 
        """,
        photoUrl="https://content.instructables.com/ORIG/F9N/4S7R/HTPUP3GZ/F9N4S7RHTPUP3GZ.jpg?auto=webp&frame=1&crop=3:2&width=600&fit=bounds&md=6416ed66755b7dcac9d9ed2b3d3ca2b3",
        videoUrl="",
    )

    data_crystals2=Instruction(
        projectId=20,
        stepOrder=2,
        stepTitle="Extract and Parse", 
        instructions="""
        You can download many of these SF data datasets in a CSV file format.

        I wrote utility code in Java, which goes through each dataset  and converts the CSV to a JSON format, keeping just the fields I want. At a minimum, I'm looking for some way to map (x, y, z) coordinates. These contain geo-spatial locations, which I translate to (x, y) values. The z-value is usually time.

        I can also extract a dimension value — such as the number of units in a construction permit — and hence the "size" of each datum.
        """,
        photoUrl="https://content.instructables.com/ORIG/F6G/T55E/HTQN6AXF/F6GT55EHTQN6AXF.jpg?auto=webp&frame=1&crop=2:3&width=369&fit=bounds&md=358b4809406113cfc7a30eef147e3bc6",
        videoUrl="",
    )

    data_crystals3=Instruction(
        projectId=20,
        stepOrder=3,
        stepTitle="What Does Data Look Like?", 
        instructions="""
        Remember these are 3D prints and have a physical presence and so have a material form. The question I am trying to answer is: What does data look like?

        In the case of open data, I experimented with many shapes and came up with simple cubes, aligned on the same orientation. The white ones (VeroWhite resin) seemed to resonate both in my mind and those of colleagues when I showed it to them.
        """,
        photoUrl="https://content.instructables.com/ORIG/FIL/OILG/HTQN6AXN/FILOILGHTQN6AXN.jpg?auto=webp&frame=1&width=406&height=1024&fit=bounds&md=0439dbd8648e5aea1e8a014fb6a64c7d",
        videoUrl="",
    )

    data_crystals4=Instruction(
        projectId=20,
        stepOrder=4,
        stepTitle="Map Into 3D Space", 
        instructions="""
        Using the Processing program, along with the ModelBuilder libraries by Marius Watz, I map the 3D data onto the screen, so I can see what it looks like in its "raw" state.

        The first image is the construction permit data — as you can see there is a lot of building in the southern part of the city, such as the Mission District. The lone dot is Candlestick Park, which is to be converted into housing units.

        The second one is the SF Civic Art Collection data. Many art pieces are located in the same places such as City Hall, hence the vertical columns. And that column on it's own...that's the San Francisco Airport.
        """,
        photoUrl="https://content.instructables.com/ORIG/FYJ/4LZK/HTQN6AZ4/FYJ4LZKHTQN6AZ4.jpg?auto=webp&frame=1&crop=3:2&width=600&fit=bounds&md=77275f95f9f2d9f1ee6e7557c6ee7f4d",
        videoUrl="",
    )

    data_crystals5=Instruction(
        projectId=20,
        stepOrder=5,
        stepTitle="Do Many, Many Samples", 
        instructions="""
        This took weeks and weeks of programming and printing and going back and forth before I settled on viable technique. I played with different forms. I tested clustering patterns for both looks and for structural considerations. I showed samples to friends.

        I kept returning to my central question of what does data look like as a guide and tweaked my code to give a better form to the data.
        """,
        photoUrl="https://content.instructables.com/ORIG/FO2/YML2/HTPUP3L4/FO2YML2HTPUP3L4.jpg?auto=webp&frame=1&width=908&height=1024&fit=bounds&md=0a62aa50e2aad800e9d3171920a037d0",
        videoUrl="",
    )

    data_crystals6=Instruction(
        projectId=20,
        stepOrder=6,
        stepTitle="Run Clustering Algorithms", 
        instructions="""
        Finally, once I massaged and reworked the data, I ran a clustering algorithm, which essentially bunches the cubes together into one cohesive structure.

        The cubes have to stick together. Every single one needs to be accounted for. I use a combination of a gravity attractor, a spherical searcher and a Brownian motion generator. Each "crystal" takes a different amount of time to properly cluster.

        The video depicts the construction permit data, which only takes 2 minutes. However, the crime data has something like 35,000 data points and takes about 5 hours to properly cluster.
        """,
        photoUrl="https://content.instructables.com/ORIG/FMH/PEJN/HTPUP3L0/FMHPEJNHTPUP3L0.jpg?auto=webp&frame=1&width=292&fit=bounds&md=2c705954858c045f9539c226b33d367a",
        videoUrl="",
    )

    data_crystals7=Instruction(
        projectId=20,
        stepOrder=7,
        stepTitle="Patch for Structural Integrity", 
        instructions="""
        After running the algorithms, I extract the model as an STL file and inspect it closely for structural defects.

        Using a combination of MeshLab (good for quick inspection) and 123D Design (good for adding material), I fix up any weak structural points. Usually there is no more than two spots of question, but the last thing I want is for the Data Crystal to break because it is too fragile.
        """,
        photoUrl="https://content.instructables.com/ORIG/FPX/BW8O/HTPUP3JE/FPXBW8OHTPUP3JE.jpg?auto=webp&frame=1&crop=3:2&width=600&height=1024&fit=bounds&md=d557f8ba9181d3d551d3c400fe8ddbc8",
        videoUrl="",
    )

    data_crystals8=Instruction(
        projectId=20,
        stepOrder=8,
        stepTitle="3D Print and Clean", 
        instructions="""
        I run these prints out on an Objet500 Connex3 printer, which leaves behind this form, a cocoon-like support material.

        With all the nuances and contours of the Data Crystal, there is a lot of cleaning required. I soak it in water overnight, I pick away at it with dental tools and I use a high-pressure water jet to blast out the support gunk.
        """,
        photoUrl="https://content.instructables.com/ORIG/FTO/F8OJ/HTPUP3I8/FTOF8OJHTPUP3I8.jpg?auto=webp&frame=1&width=917&height=1024&fit=bounds&md=f8ba56a59be249fc5c5a769beb8dcaf5",
        videoUrl="",
    )

    data_crystals9=Instruction(
        projectId=20,
        stepOrder=9,
        stepTitle="Mount on Wood", 
        instructions="""
        Once fully cleaned, the data sculptures are ready for finishing work. Using 1/16" stainless wire, I mounted each of the 3D prints onto an exotic hardwood stand to give it a compelling presentation.

        I carefully drilled into the base of the 3D sculpture, which has to be done by hand and then I press-fit it onto the wire. I did the holes for the base on a drill press. 
        """,
        photoUrl="https://content.instructables.com/ORIG/F2O/OO9C/HTQN8IHJ/F2OOO9CHTQN8IHJ.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=4675534ab5a92fbde710fe1d4961ab77",
        videoUrl="",
    )


    data_crystals10=Instruction(
        projectId=20,
        stepOrder=10,
        stepTitle="Done!", 
        instructions="""
        These are some of the final Data Crystals (in order of images):
        - SF Civic Art Collection
        - Development Pipeline (a.k.a. construction permits)
        - Incidents of Crime (over a 3 month period).

        I hope this was inspiring and an alternate approach to Data Visualization
        For more Data Crystals and other projects, you can find me here: @kildall or www.kildall.com/blog
        Scott Kildall
        """,
        photoUrl="https://content.instructables.com/ORIG/FWM/MGUF/HTQN6BG6/FWMMGUFHTQN6BG6.jpg?auto=webp&frame=1&width=810&fit=bounds&md=a88b2266a963a85a0fd5f61be5d2a70a",
        videoUrl="",
    )

    mpcnc_controller1=Instruction(
        projectId=21,
        stepOrder=1,
        stepTitle="Assembly", 
        instructions="""
        The receiver is mounted under the CNC. All the parts fit into the enclosures as in the images here.

        When I get 5 minutes, I will look around for the code on the transmitter and receiver and upload it.

        The graphics were all designed in Photoshop and then the individual pages for the remote designed.

        Nextion screens are fine, but their programming interface is appalling. You need to learn smart ways to work around it's issues.

        There are various screens:

        Boot screen (V1 Logo)
        Direct command page. Enter your own direct G or M codes
        Control page. Move the head around as required in increments of 0.01 to 100mm
        Setup page. Request data and checks from the CNC (such and end stop test, voltages etc)
        Data page. Shows spindle RPM, X, Y and Z position in large text
        Tap controller. Move the CNC head rapidly to any position on the CNC by tapping the screen.
        """,
        photoUrl="https://content.instructables.com/ORIG/FKZ/C7RW/L4MRAN4E/FKZC7RWL4MRAN4E.jpg?auto=webp&frame=1&width=859&height=1024&fit=bounds&md=06f3bec8513f14aa0cb25c68f3459f9f",
        videoUrl="",
    )

    mpcnc_controller2=Instruction(
        projectId=21,
        stepOrder=2,
        stepTitle="Finished Item", 
        instructions="""
        Makes life far easier, especially the tap to move controller.

        I also added a Bluetooth receiver and that enabled me to write a controller app for my Samsung S7 using MIT App inventor 2.

        Have a look at it in action.

        https://www.youtube.com/watch?v=NiKWD2kOsvA
        """,
        photoUrl="https://content.instructables.com/ORIG/FCB/ZFFI/L4MRAN4A/FCBZFFIL4MRAN4A.jpg?auto=webp&frame=1&crop=3:2&width=900&height=1024&fit=bounds&md=0ad11d24345a2ec788a28fab1c125d6d",
        videoUrl="",
    )

    garage_door1=Instruction(
        projectId=22,
        stepOrder=1,
        stepTitle="Research", 
        instructions="""
        There was a planning process before I started this project to figure out what to do. I wanted to create something unique that had never been done before, and I couldn't find anything on garage doors. So, right there, I confirmed my project idea. This section contains background information on the most important and intricate components.

        Arduino:
        Arduino is an open-source electronics platform that uses simple hardware and software to make it easy to use. Arduino boards can take inputs - such as light from a sensor, a finger on a button, or a Twitter message - and convert them to outputs - such as turning on an LED, triggering a motor, or publishing anything online. The arduino uses the format code of C++.
        Infarred Receiver (IR):
        IR(Infrared) Receiver Extender cable, which consists of an IR receiver and a plug connected by a wire, is used to conveniently receive and amplify the infrared remote controller signal. The epoxy package and shell of an infrared receiver can filter out visual interference.
        Servo Motor:
        A servomotor (or servo motor) is a rotary actuator or linear actuator that can control angular or linear position, velocity, and acceleration precisely. It consists of a suitable motor coupled to a position feedback sensor.
        Transistor (NPN):
        The NPN transistor is designed to pass electrons from the emitter to the collector (so conventional current flows from collector to emitter). The emitter "emits" electrons into the base, which controls the number of electrons the emitter emits.
        """,
        photoUrl="https://content.instructables.com/ORIG/FTZ/RD7H/L4MR0E44/FTZRD7HL4MR0E44.jpg?auto=webp&frame=1&fit=bounds&md=73583b95541f6761979ff7adcbb25cc9",
        videoUrl="",
    )

    garage_door2=Instruction(
        projectId=22,
        stepOrder=2,
        stepTitle="Wiring Part 1", 
        instructions="""
        Before Starting the wiring let me tell you what each wire color represents:

        Black = Ground

        Red = Power

        Green = Arduino Output To BredBoard

        Blue = Arduino Output To Component

        Steps:
        Connect power and ground from the arduino to the bredboard
        Connect the first servo to pin 11 on the arduino
        Connect the second servo to pin 3 on the arduino
        Note : connecting the servos to the arduino will allow it to send code straight to the servo
        """,
        photoUrl="https://content.instructables.com/ORIG/FQS/J0CI/L4IQABAZ/FQSJ0CIL4IQABAZ.png?auto=webp&frame=1&fit=bounds&md=1c151b7e18370b35f287e577215b1850",
        videoUrl="",
    )
    
    garage_door3=Instruction(
        projectId=22,
        stepOrder=3,
        stepTitle="Wiring Part 2", 
        instructions="""
        In this wiring step, we will connect the IR receiver. The IR Reciver is the most important component in this project because it connects to a controller, which sends signals to the arduino and then to the servo to tell it to move up and down when pressed.

        Steps:
        Connect the IR Reciver to pin 7 on the arduino
        connect the IR Reciver to Power and Ground
        Note : For the IR Controller you will program that in the coding section. also make sure that the IR reciver in facing in the downwards direction of the bredboard
        """,
        photoUrl="https://content.instructables.com/ORIG/FUC/SLGL/L4MR0UWI/FUCSLGLL4MR0UWI.png?auto=webp&frame=1&fit=bounds&md=cd8367ea67f475e916f1b3913dcc8a97",
        videoUrl="",
    )

    garage_door4=Instruction(
        projectId=22,
        stepOrder=4,
        stepTitle="Wiring Part 3 (optional)", 
        instructions="""
        This step is optional; it simply adds a spark to the project by turning on a light when the garage opens and off when the garage closes. Instead of just one led, I soldered eight together to make a chandalier. Looking at the diagram, the inner circle connects to ground, while the outer circle connects to power.

        Steps:
        Connect Arduino pin 4 to the transistor's base (make sure the connection is through a 1k OHM resistor)
        Connect the LED's negative side to the emitter and positive side to power from the bredboard (make sure poweris connected thorugh a 330 OHM resistor)
        Connect the transistor's collector side to ground directly.
        """,
        photoUrl="https://content.instructables.com/ORIG/FKC/1SUF/L4MR0UYP/FKC1SUFL4MR0UYP.png?auto=webp&frame=1&width=631&fit=bounds&md=b48aa4edd60824ca59f2ac53c85b345c",
        videoUrl="",
    )

    garage_door5=Instruction(
        projectId=22,
        stepOrder=5,
        stepTitle="Code", 
        instructions="""
        Simply copy and paste the code into the Arduino editor and connect your computer to the Arduino to upload it. To program your remote controller with your IR just open up the serial monitor then click the button you want to be assigned to that command e.g. if your want 1 to be forward click 1 on your remote while pointing it at the IR then look for the Hexacode that pops up and copy that into "if (results.value == 0x000000)" keep the 0x but replace the other long string of numbers and letters with your Hexacode.
        """,
        photoUrl="https://content.instructables.com/ORIG/FLW/ZSWG/L4MR0MME/FLWZSWGL4MR0MME.jpg?auto=webp&frame=1&width=400&height=1024&fit=bounds&md=7d5b767b07df733a285bf0e7fd0d7e18",
        videoUrl="",
    )

    garage_door6=Instruction(
        projectId=22,
        stepOrder=6,
        stepTitle="Frame Assembly", 
        instructions="""
        When all of the wiring and code is finished, it's time for the final assembly. I used a small immatation of a house that I had lying around for the frame. I cut a hole in one of the walls that I thought was big enough for the garage door. If you don't have the materials, don't worry; you can make a frame out of whatever you have lying around; just make sure it has a rectangular shape to which you can glue the servos.

        Steps :
        Glue the bredboard and arduino to the inner-top of the frame
        glue the servos to either side of the frame, facing eachother
        cut out a peice of construction paper that fits the dimensions of the frame and glue to the arms of the servo
        Note: if the servos are opening in the opposite directions, Flip one of them . also make sure the IR Reciver is visible and not behind something
        """,
        photoUrl="https://content.instructables.com/ORIG/FQO/PVR6/L4MR0MMD/FQOPVR6L4MR0MMD.jpg?auto=webp&frame=1&width=800&height=1024&fit=bounds&md=6affd9904377fc1325d4a1a0e5ba21e7",
        videoUrl="",
    )

    garage_door7=Instruction(
        projectId=22,
        stepOrder=7,
        stepTitle="Conclusion", 
        instructions="""
        If you followed the steps correctly, you should have a fully functional garage door. If not, go over the steps again to see where you went wrong. The video attached i what it should look like when working.
        """,
        photoUrl="https://content.instructables.com/ORIG/FN0/9F4R/L4IQAABR/FN09F4RL4IQAABR.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=873d56eaa22151a580dfd9028725cb2c",
        videoUrl="",
    )

    poop_bag1=Instruction(
        projectId=23,
        stepOrder=1,
        stepTitle="Print, Punching Holes, Tracing Out the Pattern and Cut Out the Leather Pieces", 
        instructions="""
        Download free attached pattern, print them out. Punch the holes at first and cut the pattern out. Transfer the pattern on each leather piece with the scratch awl tool. Use the ruler and cutter to cut the leather pieces out.

        You can also use the crepe tape technique or as i do use the glue dots.

        Use the following printer setting:

        Size: 100%

        Paper size European: DIN A4

        Paper size USA: US Letter
        """,
        photoUrl="https://content.instructables.com/ORIG/FDQ/2SCL/L4TW93S6/FDQ2SCLL4TW93S6.jpg?auto=webp&frame=1&width=533&height=1024&fit=bounds&md=db92861a76eaba47328dbcff58967502",
        videoUrl="",
    )

    poop_bag2=Instruction(
        projectId=23,
        stepOrder=2,
        stepTitle="Sanding, Bevel and Finishing the Edges", 
        instructions="""
        For smooth edges use sandpaper or rotary tool (for example: Dremel).

        I am using OKA Factory Edge Beveler Size No. 1 to round off the edges.

        Burnish the edges. Use tokonole leather finish and the wood slicker to burnishing the edges. You can use water as well. You can find HERE a very useful tutorial from "Corter Leather".

        NOTE: Repeat sanding and burnishing one more time for a better results. Use different types of sandpaper (First round: 400, second round: 1200).
        """,
        photoUrl="https://content.instructables.com/ORIG/FJL/E5Q5/L4TW94PZ/FJLE5Q5L4TW94PZ.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=be900367049e13260f45bc981b283167",
        videoUrl="",
    )

    poop_bag3=Instruction(
        projectId=23,
        stepOrder=3,
        stepTitle="Handpress and Sewing", 
        instructions="""
        Attach snaps first. On top i am punching the hole for the snap and attach it at the end, because i can make changes to the position of this snap.

        I am sewing the side with the carabiner hook at first. For sewing i use the saddle stitch technique WITHOUT a stitching pony. HERE you can learn from "Corter Leather" how to do that.

        There are two ways to sew the side walls:

        Method No. 1 - Sewn the side walls inwards.
        Method No. 2 - Sewn the side walls outwards.
        In this project i am using Method No. 2.
        """,
        photoUrl="https://content.instructables.com/ORIG/FPA/WG38/L4TW95WC/FPAWG38L4TW95WC.jpg?auto=webp&frame=1&width=400&height=1024&fit=bounds&md=4c19ce111684a31d3621e9959fafa657",
        videoUrl="",
    )

    poop_bag4=Instruction(
        projectId=23,
        stepOrder=4,
        stepTitle="The Finished Product", 
        instructions="""
        We are done! You made it! I would be glad to see your Leather Dog Poop Bag Holder/Dispenser :)
        """,
        photoUrl="https://content.instructables.com/ORIG/FG5/9QMB/L4TW9448/FG59QMBL4TW9448.jpg?auto=webp&frame=1&width=800&height=1024&fit=bounds&md=03ca6b1484f9217394a0655d1e46cc7f",
        videoUrl="",
    )

    cup_carrier1=Instruction(
        projectId=24,
        stepOrder=1,
        stepTitle="3D Print Components", 
        instructions="""
        Print the enclosed .stl files.

        The Coffee cup Carrier exists out of two components: a platform and a handle. The components have been sliced with Ultimaker Cura software and I have printed my copies with an Ultimaker 2+ 3D printer. I’ve printed both parts with following settings:

        Layer height: 02 mm
        Infill density: 15%
        Print speed: 60 mm/s
        Build Plate Adhesion: skirt
        To 3D print, I’ve positioned the components as shown on the pictures.
        """,
        photoUrl="https://content.instructables.com/ORIG/FNN/V8GT/L4H1A98E/FNNV8GTL4H1A98E.jpg?auto=webp&frame=1&fit=bounds&md=249b3134ed8f9e1fa958e54b1de12468",
        videoUrl="",
    )

    cup_carrier2=Instruction(
        projectId=24,
        stepOrder=2,
        stepTitle="Clean the Printed Components", 
        instructions="""
        Ones the parts have been 3D printed, remove the brim from the components. Clean up the edges with a sharp knife to remove all left over parts of the skirt or brim.
        """,
        photoUrl="https://content.instructables.com/ORIG/FM3/1V09/L4H1AADP/FM31V09L4H1AADP.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=13a259af9359db324feb4a8057d8f5d0",
        videoUrl="",
    )

    cup_carrier3=Instruction(
        projectId=24,
        stepOrder=4,
        stepTitle="The Ribbon", 
        instructions="""
        Cut the ribbon at a length of 25 cm. Decide on the position of the button and mark that point on the ribbon. I’ve opted to put it at about 1,5 cm of the ribbon edges.

        Put the ribbon through the ribbon conductor of the handle and close the loop by hammering the button through the ribbon edges as shown on the button packaging.
        """,
        photoUrl="https://content.instructables.com/ORIG/F3E/FYRG/L4H1AAGE/F3EFYRGL4H1AAGE.jpg?auto=webp&frame=1&width=400&height=1024&fit=bounds&md=5773dd214f5c1264c3ed1d68452a7a42",
        videoUrl="",
    )

    cup_carrier4=Instruction(
        projectId=24,
        stepOrder=4,
        stepTitle="The Velcro", 
        instructions="""
        Cut 4 x a piece of 3,5 cm of the sticky velcro hook. Stick a velcro hook on each of the 3 velcro conductors of the handle.

        Cut a 40 cm piece of sewing velcro loop. Attach 1 side to one of the velcro hooks placed in one of the conductors. Stick the last piece of the velcro hook on the back side of the part of the velcro loop which is stuck on the velcro hook of a conductor (see images below)
        """,
        photoUrl="https://content.instructables.com/ORIG/FGH/KPPC/L4H1AAJ5/FGHKPPCL4H1AAJ5.jpg?auto=webp&frame=1&width=800&height=1024&fit=bounds&md=4593492ea45b634d8ea9b2d6691b5493",
        videoUrl="",
    )

    cup_carrier5=Instruction(
        projectId=24,
        stepOrder=5,
        stepTitle="Screw the Components Together", 
        instructions="""
        Slide the handle in the holder of the platform and tie both components together with the screw and nut. 
        """,
        photoUrl="https://content.instructables.com/ORIG/FSF/6DQW/L4H1AANQ/FSF6DQWL4H1AANQ.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=37df953c9d985a2c4a95c5c3c7779a40",
        videoUrl="",
    )

    cup_carrier6=Instruction(
        projectId=24,
        stepOrder=6,
        stepTitle="Cut the Neoprene to Use As a Non-skid", 
        instructions="""
        Draw a circle of 11 cm in the sheet Neoprene. I started by drawing a circle of 11 cm on a piece of paper and cut it out so I could use it as a pattern. If you prefer, you could also draw a circle directly on the Neoprene. Cut the circle out with a pair of scissors.

        Put the Neoprene circle on the platform.
        """,
        photoUrl="https://content.instructables.com/ORIG/F2P/Z0ZA/L4H1AAPJ/F2PZ0ZAL4H1AAPJ.jpg?auto=webp&frame=1&width=400&height=1024&fit=bounds&md=b7e83b3d92600ce0063179a0cfcf9fad",
        videoUrl="",
    )

    cup_carrier7=Instruction(
        projectId=24,
        stepOrder=7,
        stepTitle="The End Result", 
        instructions="""
        As I’m a novice in Fusion 360, I needed a lot of help to bring this process to an end. Following video’s helped and inspired:
        """,
        photoUrl="https://content.instructables.com/ORIG/FG7/Z4LZ/L4H1AAUI/FG7Z4LZL4H1AAUI.jpg?auto=webp&frame=1&width=800&height=1024&fit=bounds&md=ea3adff0efede4d1f2d754f69d2581bd",
        videoUrl="",
    )

    cardboard1=Instruction(
        projectId=25,
        stepOrder=1,
        stepTitle="Assemble Boxes", 
        instructions="""
        The boxes were all stored flat packed, so the night before commencing the project assembled all the boxes and stored them under the patio.
        """,
        photoUrl="https://content.instructables.com/ORIG/FSS/FUDS/L41BGIYE/FSSFUDSL41BGIYE.jpg?auto=webp&frame=1&crop=3:2&width=635&height=1024&fit=bounds&md=3e677d5e5b4b91f6d473bf14983406b2",
        videoUrl="",
    )

    cardboard2=Instruction(
        projectId=25,
        stepOrder=2,
        stepTitle="Commence Construction of Outer Walls", 
        instructions="""
        Decide how large you want to go with the calculated amount of boxes you have. Then start with the outside walls. I have allowed for a door where I will be building a drawbridge a little bit later on in the project.
        """,
        photoUrl="https://content.instructables.com/ORIG/FZ3/0PX9/L41BGIYZ/FZ30PX9L41BGIYZ.jpg?auto=webp&frame=1&crop=3:2&width=400&height=1024&fit=bounds&md=9e966a6173873e38edb3756ed558b70e",
        videoUrl="",
    )

    cardboard3=Instruction(
        projectId=25,
        stepOrder=3,
        stepTitle="Continue Building Up", 
        instructions="""
        Continue building the outside walls till you teach a desired height.
        """,
        photoUrl="https://content.instructables.com/ORIG/FQR/13GZ/L41BGIZO/FQR13GZL41BGIZO.jpg?auto=webp&frame=1&crop=3:2&width=400&height=1024&fit=bounds&md=3288c3816ba8352a418ea7bc986d4fe5",
        videoUrl="",
    )

    cardboard4=Instruction(
        projectId=25,
        stepOrder=4,
        stepTitle="Securing As You Build", 
        instructions="""
        I'm using an industrial tape dispenser with over a dozen roles of tape in supply. And also used a few tent pegs to secure the bottom layer to the lawn.
        """,
        photoUrl="https://content.instructables.com/ORIG/F72/2KGW/L41BGJVI/F722KGWL41BGJVI.jpg?auto=webp&frame=1&crop=3:2&width=400&height=1024&fit=bounds&md=fb156403bfabe753311d8e9d259ba265",
        videoUrl="",
    )

    cardboard5=Instruction(
        projectId=25,
        stepOrder=5,
        stepTitle="Internal Rooms", 
        instructions="""
        With all the external walls complete it's time to use up the remaining boxes and build internal rooms to your own desire.
        """,
        photoUrl="https://content.instructables.com/ORIG/FVK/WHVD/L41BGJVX/FVKWHVDL41BGJVX.jpg?auto=webp&frame=1&crop=3:2&width=900&height=1024&fit=bounds&md=d5468400580fd3a99b00b5115f411011",
        videoUrl="",
    )

    cardboard6=Instruction(
        projectId=25,
        stepOrder=6,
        stepTitle="Slide Through Tunnel", 
        instructions="""
        I taped two fridge boxes on top of each other, to make a tower and then cut a door either side of the bottom so that as you go down the slide you slide through a 'tunnel'. I also added another smaller box at the end to make the tunnel a little longer.
        """,
        photoUrl="https://content.instructables.com/ORIG/F7G/T2HK/L41BGKTP/F7GT2HKL41BGKTP.jpg?auto=webp&frame=1&crop=3:2&width=300&height=1024&fit=bounds&md=4d1f9ab9aaae1887cab8e8a1ed30a021",
        videoUrl="",
    )

    cardboard7=Instruction(
        projectId=25,
        stepOrder=7,
        stepTitle="Functioning Drawbridge", 
        instructions="""
        Almost finished the project, with the final step of building a functioning drawbridge. I taped several pieces of cardboard together so that they were thicker and more structurally sound. And also put some reinforcing on the edges. Then used tent pegs to secure the bottom to create a hinge.
        """,
        photoUrl="https://content.instructables.com/ORIG/FYX/VLXK/L41BGLLM/FYXVLXKL41BGLLM.jpg?auto=webp&frame=1&crop=3:2&width=600&height=1024&fit=bounds&md=d16e60aaeba7e1a1df372bb335896dfb",
        videoUrl="",
    )

    cardboard8=Instruction(
        projectId=25,
        stepOrder=8,
        stepTitle="Adding Rope", 
        instructions="""
        Securely tape some cardboard rolls to underside of the entrance to allow the rope to slide through and then secure the rope at the end of the drawbridge.
        """,
        photoUrl="https://content.instructables.com/ORIG/F0B/9I7Q/L41BGMU6/F0B9I7QL41BGMU6.jpg?auto=webp&frame=1&crop=3:2&width=300&height=1024&fit=bounds&md=5b8208c15d84ebe94ce10189bf53d713",
        videoUrl="",
    )

    cardboard9=Instruction(
        projectId=25,
        stepOrder=9,
        stepTitle="Playtime!", 
        instructions="""
        Now that the kids have at it and enjoy!
        Feel free to check out the video to see more on the build process or clarification if needed!
        """,
        photoUrl="https://content.instructables.com/ORIG/FHR/SIE5/L41BGNGN/FHRSIE5L41BGNGN.jpg?auto=webp&frame=1&crop=3:2&width=600&height=1024&fit=bounds&md=2da5d248496897762b8fd896a42eaf92",
        videoUrl="",
    )

    zentrierwinkel1=Instruction(
        projectId=26,
        stepOrder=1,
        stepTitle="Längenmarkierung", 
        instructions="""
        Du brauchst vier Leistenstücke:

        1 Leistenstück (Länge = 10 cm)
        2 Leistenstücke (Länge = 12 cm)
        1 Leistenstück (Länge = 20 cm)
        Zeichne die Länge auf deiner Rechteckleiste ein und verlängere den Strich mit dem Anschlagwinkel.
        """,
        photoUrl="https://content.instructables.com/ORIG/FLG/YSNA/L3A62TBG/FLGYSNAL3A62TBG.jpg?auto=webp&frame=1&fit=bounds&md=39dcacab4d47afa793ae3e31ecc6d12f",
        videoUrl="",
    )

    zentrierwinkel2=Instruction(
        projectId=26,
        stepOrder=2,
        stepTitle="Abschneiden Der Leistenstücke", 
        instructions="""
        Spanne die Sägelade mithilfe der Einspannvorrichtung deiner Werkbank ein. Beachte: Die Oberkante der Sägelade soll mit der Werkbankplatte bündig abschließen.

        Lege die Rechteckleiste flach in die Sägelade. Die Markierung auf der Leiste muss beim Sägen genau unter den Sägezähnen der Japansäge liegen. Zieh die Säge zu dir, um dein erstes Leistenstück abzuschneiden. Gehe genau so vor, um die restlichen Stücke abzuschneiden.
        """,
        photoUrl="https://content.instructables.com/ORIG/FFA/QRLS/L3A62RUM/FFAQRLSL3A62RUM.jpg?auto=webp&frame=1&width=565&height=1024&fit=bounds&md=ef627d05f6966e6de34d5ce03b95a047",
        videoUrl="",
    )

    zentrierwinkel3=Instruction(
        projectId=26,
        stepOrder=3,
        stepTitle="Verbinden Der Beiden Mittellangen Leistenstücke", 
        instructions="""
        Verwende für diesen Schritt die beiden Leistenstücke mit der Länge von 12 cm, Holzleim und einen Anschlagwinkel.

        Gib etwas Leim auf das Ende eines Leistenstücks und lege das zweite Leistenstück im rechten Winkel darauf. Die Kanten der beiden Leistenstücke müssen bündig abschließen. Nutze den Anschlagwinkel, um den Winkel zu überprüfen!
        """,
        photoUrl="https://content.instructables.com/ORIG/F71/6UPC/L3BLHWY6/F716UPCL3BLHWY6.jpg?auto=webp&frame=1&fit=bounds&md=8fc587257bfa65524d329b9dd8df80c1",
        videoUrl="",
    )

    zentrierwinkel4=Instruction(
        projectId=26,
        stepOrder=4,
        stepTitle="Zusammenleimen Der Mittellangen Leistenstücke", 
        instructions="""
        Leime die beiden Leistenstücke zusammen. Verwende dazu eine Schraubzwinge.
        """,
        photoUrl="https://content.instructables.com/ORIG/FK5/481L/L3A62RUP/FK5481LL3A62RUP.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=409ee696bd292fec5baeec529971ce75",
        videoUrl="",
    )

    zentrierwinkel5=Instruction(
        projectId=26,
        stepOrder=5,
        stepTitle="", 
        instructions="""
        """,
        photoUrl="",
        videoUrl="",
    )

    zentrierwinkel5=Instruction(
        projectId=26,
        stepOrder=5,
        stepTitle="Anbringen Des Kurzen Leistenstücks", 
        instructions="""
        Für diesen Schritt brauchst du das kürzeste Leistenstück.

        Gib etwas Leim auf das unten liegende Leistenstück und setze das kürzeste Leistenstück darauf. Verwende zum Zusammenleimen eine Schraubzwinge.
        """,
        photoUrl="https://content.instructables.com/ORIG/FT0/L6RK/L3A62RUD/FT0L6RKL3A62RUD.jpg?auto=webp&frame=1&width=223&height=1024&fit=bounds&md=37d01737d2aa8165b9083d5b872d1a49",
        videoUrl="",
    )

    zentrierwinkel6=Instruction(
        projectId=26,
        stepOrder=6,
        stepTitle="Abschneiden Im 45°-Winkel", 
        instructions="""
        Für den nächsten Schritt brauchst du das längste Leistenstück.

        Lege das Leistenstück flach in die Sägelade. Verwende diesmal die 45°-Sägeführung. Die obere Ecke des Leistenstücks muss genau mit dem Schlitz der Sägeführung abschließen. Schneide mit der Säge ab.
        """,
        photoUrl="https://content.instructables.com/ORIG/F2T/IAXK/L3BLI6BE/F2TIAXKL3BLI6BE.jpg?auto=webp&frame=1&width=245&height=1024&fit=bounds&md=ccd1a5666a79639cd5a5b5bc1be0fab8",
        videoUrl="",
    )

    zentrierwinkel7=Instruction(
        projectId=26,
        stepOrder=7,
        stepTitle="Anbringen Des Längsten Leistenstücks", 
        instructions="""
        Verwende etwas Leim und bringe das längste Leistenstück an. Kontrolliere, ob du das Leistenstück im 45°-Winkel angebracht hast. Nimm dazu den Anschlagwinkel zu Hilfe. Auf dem letzten Bild siehst du, wie das geht.
        """,
        photoUrl="https://content.instructables.com/ORIG/FTO/MIZB/L3BLI6ZJ/FTOMIZBL3BLI6ZJ.jpg?auto=webp&frame=1&width=384&height=1024&fit=bounds&md=edcbafa0b980d7a19f7702716627c70b",
        videoUrl="",
    )

    zentrierwinkel8=Instruction(
        projectId=26,
        stepOrder=8,
        stepTitle="Schleifen", 
        instructions="""
        Verwende Schleifpapier, um unebene Kanten zu glätten.
        """,
        photoUrl="https://content.instructables.com/ORIG/F8S/6KGJ/L3EGCVON/F8S6KGJL3EGCVON.jpg?auto=webp&frame=1&width=670&fit=bounds&md=a8f3108f76b0d06097ff5d2898959f40",
        videoUrl="",
    )

    smores1=Instruction(
        projectId=27,
        stepOrder=1,
        stepTitle="Directions", 
        instructions="""
        1. Light the chaffing fuel can and toast the mini marshmallows. You can toast about 5-6 at a time. Remove from stick and place onto parchment paper to let cool.

        2. Crush the graham crackers into small pieces.

        3. Cut the chocolate squares into small pieces. Set aside. (Note: if using squares with caramel, place in the freezer for about 5 minutes. When you cut the chocolate, the caramel will stay in the chocolate).
        """,
        photoUrl="https://content.instructables.com/ORIG/FOX/0P2W/L4MR0XFL/FOX0P2WL4MR0XFL.jpg?auto=webp&frame=1&width=400&height=1024&fit=bounds&md=e2341b079378bfdfcb51cfb46b5d2b77",
        videoUrl="",
    )

    smores2=Instruction(
        projectId=27,
        stepOrder=2,
        stepTitle="Directions (cont.)", 
        instructions="""
        4. Whip the heavy cream, in stand mixer or with hand mixer until stiff peaks have formed. Add marshmallow crème, sweetened condensed milk and vanilla extract and mix well. Do Not Overmix.

        5. Fold in the toasted mini marshmallows, crushed graham crackers and chocolate pieces into the cream mixture.

        6. Transfer into a freezer safe container and freeze for about 8 hours before serving.
        """,
        photoUrl="https://content.instructables.com/ORIG/FD1/AACL/L4MR0XHZ/FD1AACLL4MR0XHZ.jpg?auto=webp&frame=1&width=242&height=1024&fit=bounds&md=957e886583aa5037e5416988b62c574d",
        videoUrl="",
    )

    smores3=Instruction(
        projectId=27,
        stepOrder=3,
        stepTitle="ENJOY!", 
        instructions="""
        Serve ice cream in a cone or bowl and enjoy this perfect summer treat!
        """,
        photoUrl="https://content.instructables.com/ORIG/FRF/3CWP/L4MR0XFK/FRF3CWPL4MR0XFK.jpg?auto=webp&frame=1&width=800&height=1024&fit=bounds&md=07949ab002f41979db051caa41cdc722",
        videoUrl="",
    )

    gearbox1=Instruction(
        projectId=28,
        stepOrder=1,
        stepTitle="Print Plastic Parts", 
        instructions="""
        Download models from https://www.thingiverse.com/thing:5414478 and print them.

        For the wheel, I would recommend specifying 3mm for walls to make it as strong as possible. The box walls should be at least 2mm (3-4 mm would be better).
        """,
        photoUrl="https://content.instructables.com/ORIG/FFT/XJIZ/L4JW6TVZ/FFTXJIZL4JW6TVZ.jpg?auto=webp&frame=1&width=839&height=1024&fit=bounds&md=01c323fef643388b2978964bb8c9b504",
        videoUrl="",
    )

    gearbox2=Instruction(
        projectId=28,
        stepOrder=2,
        stepTitle="Wheel Reinforcement (optional)", 
        instructions="""
        In order to make the wheel stronger, you can reinforce it with nails.

        Cut off 12 nail tails in 5-6 mm length and put them into special slots inside the wheel.
        """,
        photoUrl="https://content.instructables.com/ORIG/F0F/YXI5/L4JW6VLA/F0FYXI5L4JW6VLA.png?auto=webp&frame=1&width=352&fit=bounds&md=19547b4210171a6c964c7ed3aeaff77e",
        videoUrl="",
    )

    gearbox3=Instruction(
        projectId=28,
        stepOrder=3,
        stepTitle="Gear Teeth", 
        instructions="""
        Nails are used as gear teeth. Teeth hook the worm and rotate the wheel.

        Prepare 20 nail shanks in 12-13 mm without tips.

        Insert all teeth into the wheel.

        Use a file to avoid burrs on the teeth.
        """,
        photoUrl="https://content.instructables.com/ORIG/FGZ/1H18/L4JW6VW6/FGZ1H18L4JW6VW6.png?auto=webp&frame=1&width=533&height=1024&fit=bounds&md=877831499494e5ea9121c431686fa4b6",
        videoUrl="",
    )

    gearbox4=Instruction(
        projectId=28,
        stepOrder=4,
        stepTitle="Prepare the Worm", 
        instructions="""
        Confirmat screw is used as a worm. The tail of the screw has to be round (without thread) to be placed inside a washer 15x3 mm. Use a file to avoid thread on the screw tail.
        """,
        photoUrl="https://content.instructables.com/ORIG/F5V/LK8T/L4JW6XCU/F5VLK8TL4JW6XCU.png?auto=webp&frame=1&fit=bounds&md=0b7644a513a3c43531d3bc0ae293571c",
        videoUrl="",
    )

    gearbox5=Instruction(
        projectId=28,
        stepOrder=5,
        stepTitle="Assembly", 
        instructions="""
        Put washers 1 and 2 into the box
        Lubricate the wheel
        Insert the wheel
        Lubricate the confirmat screew
        Screw the confirmat in
        Put the washer 3 into the box
        """,
        photoUrl="https://content.instructables.com/ORIG/FIG/CFPG/L4LBLIUU/FIGCFPGL4LBLIUU.png?auto=webp&frame=1&width=486&fit=bounds&md=6c1df73990fff69fd35c90f371227ff3",
        videoUrl="",
    )

    gearbox6=Instruction(
        projectId=28,
        stepOrder=6,
        stepTitle="Test", 
        instructions="""
        Here you can see my test of the gearbox by my screwdriver.
        """,
        photoUrl="https://content.instructables.com/ORIG/FSP/KSV2/L4JW6S6M/FSPKSV2L4JW6S6M.png?auto=webp&frame=1&width=495&height=1024&fit=bounds&md=c5697069283e9374ca7a984c3bf3a426",
        videoUrl="",
    )

    garden_tables1=Instruction(
        projectId=29,
        stepOrder=1,
        stepTitle="Assess Your Pallets", 
        instructions="""
        Pallets vary a bit in design, but they all pretty much consist of four joists roughly the size of 2x4s, with 2 joists forming the outside "walls" of the pallet and the other two spaced evenly to create three "bays" of roughly equal widths. On these joists are nailed the planks that flesh out the pallet. You are going to eliminate the center bay by sawing through the planks right at the outside edges of the center joists, then inspect the layout of the planks on each side of the pallet to assess how to form your little square-ish tables. You can figure out the specifics after you cut out the center bays if you like, but it's good just to get a sense of the whole project before you saw.
        """,
        photoUrl="https://content.instructables.com/ORIG/FIT/45EY/L3IQW01Y/FIT45EYL3IQW01Y.jpg?auto=webp&frame=1&width=627&height=1024&fit=bounds&md=b1c04399abc3521b75bb450e8ebdd0c6",
        videoUrl="",
    )

    garden_tables2=Instruction(
        projectId=29,
        stepOrder=2,
        stepTitle="Clamp Your Straight Edge and Saw Through the Course of Planks", 
        instructions="""
        Clamp a straight edge onto your pallet so that the blade of your skill saw will cut through the course of planks just on the edge of one of the interior joists.
        """,
        photoUrl="https://content.instructables.com/ORIG/FRI/DAB0/L3IQVY0F/FRIDAB0L3IQVY0F.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=e2388363c572b5a4cbaf8265183125b1",
        videoUrl="",
    )

    garden_tables3=Instruction(
        projectId=29,
        stepOrder=3,
        stepTitle="Repeat This Process Next to the Other Interior Joist", 
        instructions="""
        Clamp your straight edge and do the same cut, leaving you with an "empty" center bay on one side.
        """,
        photoUrl="https://content.instructables.com/ORIG/FVK/Z0UH/L3IQWEBI/FVKZ0UHL3IQWEBI.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=537b1f8f10466e35ac0e9af41d3b35b5",
        videoUrl="",
    )

    garden_tables4=Instruction(
        projectId=29,
        stepOrder=4,
        stepTitle="Flip Your Pallet Over and Repeat the Process", 
        instructions="""
        Once you repeat that process, you will have two long rectangles consisting of two joists and the original course of pallets. Save the sawn out pieces! They will form the legs of your table.
        """,
        photoUrl="https://content.instructables.com/ORIG/FCF/479M/L3IQVY22/FCF479ML3IQVY22.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=6856edc666966c6ecaba9fed827f8f2a",
        videoUrl="",
    )

    garden_tables5=Instruction(
        projectId=29,
        stepOrder=5,
        stepTitle="Saw Through the End Joists to Create Your Square-ish Tables", 
        instructions="""
        Turn one of your long rectangles on its side and clamp it to sawhorses or steady it otherwise. Assess the planks on each side to determine how you can saw through the 2x4 to end up with roughly the same sized tables. On my first pallet, the planks were staggered such that I could clamp a carpenter square to the 2x4 and saw through it adjacent to the center-most planks, similar to the earlier steps when cutting through the planks. Then I flipped it over, clamped it down, and sawed through the other 2x4.

        With the second pallet, however, the planks were identical on each side, so I had to remove the center plank on each then follow the same process for sawing through the 2x4s.
        """,
        photoUrl="https://content.instructables.com/ORIG/F9S/UID1/L3IQVY23/F9SUID1L3IQVY23.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=9a3afff29f5e87724530412cdb471ac5",
        videoUrl="",
    )

    garden_tables6=Instruction(
        projectId=29,
        stepOrder=6,
        stepTitle="Add the Legs", 
        instructions="""
        Flip your square-ish pallet on its side, place one of the sawn pieces of pallet into place as a leg, and screw it down. In most cases, you will need only one screw, because you can push the leg snug up against other pallet pieces.
        """,
        photoUrl="https://content.instructables.com/ORIG/FAB/0NX5/L3IQVY3P/FAB0NX5L3IQVY3P.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=c0f026c179f12e7f9d53dc8486fc19b0",
        videoUrl="",
    )

    garden_tables7=Instruction(
        projectId=29,
        stepOrder=7,
        stepTitle="Assess the Height and Table Top", 
        instructions="""
        I found that the sawn planks as table legs provided the perfect height for a garden side-table. If you want something taller you can either add a thick table top of some kind or use other wood for the legs. You will end up with gaps in the table top. I solved this problem by dumpster diving at my local big box for broken pallets. (Most DIY centers contract to return used pallets, but if the pallets get damaged in some way they go into a dumpster to be hauled away as trash.) Once home with my dumpster treasures, I used my table saw to rip these planks to sizes that would fit neatly in the gaps.
        """,
        photoUrl="https://content.instructables.com/ORIG/FNS/M7ME/L3IQWH2C/FNSM7MEL3IQWH2C.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=28969c99ff0a862f854c7e184463ef40",
        videoUrl="",
    )

    garden_tables8=Instruction(
        projectId=29,
        stepOrder=8,
        stepTitle="Enjoy Your Free Garden Tables From Repurposed Pallets", 
        instructions="""
        You will end up with eight tables. How easy was that? And give yourself a pat on the back for keeping stuff out of the landfill!
        """,
        photoUrl="https://content.instructables.com/ORIG/FCX/51G1/L3IQVY5D/FCX51G1L3IQVY5D.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=a72780b0ff0f42bb6a2a4bb6c9b5cade",
        videoUrl="",
    )

    gummy_bears1=Instruction(
        projectId=30,
        stepOrder=1,
        stepTitle="Prep Your Muffin Tin", 
        instructions="""
        For each solid you selected add 1/3c* of water to a glass measuring cup. Heat the water so that it is warm but not boiling. This will help your solids dissolve.
        Measure out 1/3c of water for each solid and add to a muffin cup for each solid, stir in one solid per muffin cup of warm water. When mixing solids, continue adding until it no longer dissolves when stirred, I added in 1/4tbs. increments.
        Repeat with each remaining liquid you are using, if using any oils measure them last as they are the hardest to clean out of your measuring cup.
        You should now have a muffin tin with a different substance in every cup.
        *my muffin tin cups hold 1/3c comfortably, adjust to a measurement that works for your pan and leaves you a little room to add.
        """,
        photoUrl="https://content.instructables.com/ORIG/FPT/TNKI/L42QYN8T/FPTTNKIL42QYN8T.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=936f6007430903cf54881706bd658ba5",
        videoUrl="",
    )

    gummy_bears2=Instruction(
        projectId=30,
        stepOrder=2,
        stepTitle="The Bears", 
        instructions="""
        To prevent any variation due to color I sorted out all the yellow bears and found the 12 closest in size.
        This is now the time to make predictions of what will happen to each bear. (skip to the last step for some information on the science if you would like some more educated guesses)
        """,
        photoUrl="https://content.instructables.com/ORIG/FCI/RUN0/L42QYN94/FCIRUN0L42QYN94.jpg?auto=webp&frame=1&width=700&height=1024&fit=bounds&md=78e8776418a6c1a49c6ce869d075a844",
        videoUrl="",
    )

    gummy_bears3=Instruction(
        projectId=30,
        stepOrder=3,
        stepTitle="Bear Soup", 
        instructions="""
        Add one bear to each muffin cup. Watch for any changes that may happen right away, the baking powder was particularly interesting for me.
        Let sit for a few hours.
        My official end time was 6 hours but I also wanted to see how long it would take for any to fully dissolve.
        I would not plan any longer than 8 hours, as quite a few of my bears were not looking too great by then, and after 10 a couple were gone completely.
        """,
        photoUrl="https://content.instructables.com/ORIG/F67/71D4/L42QYN9G/F6771D4L42QYN9G.jpg?auto=webp&frame=1&width=700&height=1024&fit=bounds&md=7b4ab8683f901d96b869a53ac8707eed",
        videoUrl="",
    )

    gummy_bears4=Instruction(
        projectId=30,
        stepOrder=8,
        stepTitle="Observe", 
        instructions="""
        Check on your bears each hour if possible and note changes.
        """,
        photoUrl="https://content.instructables.com/ORIG/FV5/JIBP/L42QW0E4/FV5JIBPL42QW0E4.jpg?auto=webp&frame=1&width=900&height=1024&fit=bounds&md=576001811ccc91653c536c8a3a25a0b5",
        videoUrl="",
    )

    gummy_bears5=Instruction(
        projectId=30,
        stepOrder=8,
        stepTitle='The "Why" of Water', 
        instructions="""
        The short answer...Osmosis! Osmosis is "a process by which molecules of a solvent tend to pass through a semipermeable membrane from a less concentrated solution into a more concentrated one"*

        What this means is that some of our gummi bears grew because the water around them had a lower concentration of sugar, than the water inside the gummi bear. The gelatin in the gummi bears acts as our semipermeable layer, that allows the water to move in or out of the gummi bear.

        Some of our gummi bears also shrank for the same reason. The salt water bear had a lower concentration of salt inside it than the water around it, therefor all the water in the gummi bear left, in an attempt to even out the levels of salt. Since gummi bears are small and don't have much water the salt level did not even out before the bear ran out of water, leaving a pretty hard bear.
        """,
        photoUrl="https://content.instructables.com/ORIG/FU9/Q7EY/L42QYNHR/FU9Q7EYL42QYNHR.jpg?auto=webp&frame=1&width=350&height=1024&fit=bounds&md=898166f9ded5feb4dbc84dbb3932b9ab",
        videoUrl="",
    )

    gummy_bears6=Instruction(
        projectId=30,
        stepOrder=6,
        stepTitle="What About the Rest?", 
        instructions="""
        Some of our non-water cups had very different results.

        The vinegar will break apart the bear, this is because of the acidity of vinegar. Vinegar generally has a ph of 2 or 3 (acidic), while gelatin has a ph closer to 9 (slightly basic). When an acid and a base mix, they don't tend to get along. In our case, since the vinegar is much more acidic than the gelatin is basic, the vinegar will break down the gelatin in an attempt to neutralize. As the vinegar works through the gummi bear it will lose its features and become more blob shaped before eventually dissolving into the vinegar.

        Another interesting happenstance, is the canola oil. The gummi bear did not change at all in the canola oil. The oil was not able to move through the gelatin and would also not have wanted to mix with the water in the gummi bear.

        The Gatorade bear grew, much like the other water based substances but was also the only bear to undergo a large color change. Becoming fully saturated with red coloring.

        Another interesting result was the baking soda bear. This bear seemed to lose all it's color while also growing a significant amount. I am not sure the science behind the color loss but am very intrigued if anyone could comment some insight.
        """,
        photoUrl="https://content.instructables.com/ORIG/FUV/B25Z/L42QW0FP/FUVB25ZL42QW0FP.jpg?auto=webp&frame=1&width=700&height=1024&fit=bounds&md=ac8108f58ae2bb42fbfa0d7f908d1c31",
        videoUrl="",
    )

    gummy_bears7=Instruction(
        projectId=30,
        stepOrder=7,
        stepTitle="End Results", 
        instructions="""
        These are the results after around 10 hours of submersion. Two bears did dissolve completely, the water bear* and the vinegar bear. One bear gained some red color. One bear came out looking very salty. And many a bear grew to a puffy new size, with the Milk and Brown Sugar Bears seeming to grow the most.

        Looking back...

        In hind sight I should've used a ruler to measure each bear instead of only comparing to the original bear. In addition I should have placed my muffin tin further from any potential variables that could sway my results.

        *A potential cause of the water bear melting was the use of the oven, that bear sitting nearest the vent. This was unintentional but may have skewed my results. Alternatively, maybe my tap water is a bit acidic. We may never know.
        """,
        photoUrl="https://content.instructables.com/ORIG/FA1/ISNJ/L42QYNC5/FA1ISNJL42QYNC5.jpg?auto=webp&frame=1&width=700&height=1024&fit=bounds&md=ca2fdc68dd9e51d6a544143835fb5591",
        videoUrl="",
    )

    fortune_cookie1=Instruction(
        projectId=31,
        stepOrder=1,
        stepTitle="Mixing the Polymer Clay", 
        instructions="""
        Mix together orange and yellow polymer clay, which should give you a bright orange that's similar to the color of a fortune cookie. In my case, I thought the resulting shade was a wee bit too neon, so I added some beige polymer clay until the brightness of the orange was toned down slightly.

        For my earrings, the final ratio of clay was approximately 1:1:0.5, with the 0.5 being the beige. In hindsight, after seeing the earrings next to a real fortune cookie, I probably should have added a little more yellow to the mixture.
        """,
        photoUrl="https://content.instructables.com/ORIG/F5T/H5SC/L4SGSMVS/F5TH5SCL4SGSMVS.jpg?auto=webp&frame=1&width=800&height=1024&fit=bounds&md=cdb200cea7592862fff91d58a9804f82",
        videoUrl="",
    )

    fortune_cookie2=Instruction(
        projectId=31,
        stepOrder=2,
        stepTitle="Roll out Clay", 
        instructions="""
        Roll out the polymer clay so that it is 1 to 2 millimeters thick.
        """,
        photoUrl="https://content.instructables.com/ORIG/F73/UP40/L4SGSN89/F73UP40L4SGSN89.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=ec276d7d260a980addb3411eed32acaa",
        videoUrl="",
    )

    fortune_cookie3=Instruction(
        projectId=31,
        stepOrder=3,
        stepTitle="Cut the Circles", 
        instructions="""
        Cut two 2-inch circles and remove the excess clay.
        """,
        photoUrl="https://content.instructables.com/ORIG/FQJ/Q75R/L4SGSNC2/FQJQ75RL4SGSNC2.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=4e8ae0332f87765735ce728eb0f46caf",
        videoUrl="",
    )

    fortune_cookie4=Instruction(
        projectId=31,
        stepOrder=4,
        stepTitle="Fold the Fortune Cookies", 
        instructions="""
        Take one of your polymer clay circles and carefully fold it in half, but do not pinch the crease flat, just loosely hold the folded edges together with your hand.

        Gently hold the folded side of the circle in your left hand between your middle finger and thumb. As you slowly bring your middle finger and thumb together, use your index finger to push the center outwards. Try your best not to flatten the bubble as you bring the tips of the cookie together.

        Repeat the above steps to create a second fortune cookie.
        """,
        photoUrl="https://content.instructables.com/ORIG/FWN/WOLO/L4SGSNF1/FWNWOLOL4SGSNF1.jpg?auto=webp&frame=1&width=400&height=1024&fit=bounds&md=91534451d5c7dc5ccd3b120584320b7c",
        videoUrl="",
    )

    fortune_cookie5=Instruction(
        projectId=31,
        stepOrder=5,
        stepTitle="Add Holes", 
        instructions="""
        Use a toothpick or jewelry eyepin to poke a hole in the top of the cookies where the tips meet. Make sure that the holes are far enough from the edges to decrease the chances of the holes cracking and breaking during daily wearings.

        Leave the toothpick (or ear wire) in place until after you've baked the fortune cookie (Step 8).
        """,
        photoUrl="https://content.instructables.com/ORIG/FH0/CDPE/L4SGSNGE/FH0CDPEL4SGSNGE.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=2eb8116a0b648bf9e8dd16d22297b174",
        videoUrl="",
    )

    fortune_cookie6=Instruction(
        projectId=31,
        stepOrder=6,
        stepTitle="Add Texture and Coloring", 
        instructions="""
        Take a cleaned mascara brush (or toothbrush) and gently scrape it along the edges of the polymer clay cookies to give it some texture.
        """,
        photoUrl="https://content.instructables.com/ORIG/FWF/9HK2/L4SGSNH5/FWF9HK2L4SGSNH5.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=d514a82ccc4ba8904f2f4b93ad106720",
        videoUrl="",
    )

    fortune_cookie7=Instruction(
        projectId=31,
        stepOrder=7,
        stepTitle="Add Coloring", 
        instructions="""
        Use an Xacto knife to scrape off some brown and/or burnt orange pastels, and use a soft bristled paintbrush to add the pastels to the roughened edges of the cookies.

        The combined texture from Step 6 and subtle color of the pastels will give your cookies the appearance of having been baked.
        """,
        photoUrl="https://content.instructables.com/ORIG/FTP/ERYK/L4SGSNH7/FTPERYKL4SGSNH7.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=84eb30e30a7cf2dc78b9f85f6bf3220e",
        videoUrl="",
    )

    fortune_cookie8=Instruction(
        projectId=31,
        stepOrder=8,
        stepTitle="Bake", 
        instructions="""
        Leave the toothpicks (or eyepins) inserted in your cookies, and bake the polymer clay for 15 minutes at 275°F (or according to the instructions on your brand of polymer clay). Let the clay cool before moving onto the next step.
        """,
        photoUrl="https://content.instructables.com/ORIG/FYO/E6PY/L4SGSNMS/FYOE6PYL4SGSNMS.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=a03142d7cf5658fa50330136cd8fee9f",
        videoUrl="",
    )

    fortune_cookie9=Instruction(
        projectId=31,
        stepOrder=9,
        stepTitle="Add Jewelry Findings", 
        instructions="""
        Use some jewelry pliers to bend an eyepin so that it starts to look like a clothes hanger (first picture), and then poke it through the holes of one of your cookies. Wrap the leftover wire around the post of the eyepin, and repeat the process with the other cookie.

        Attach an ear wire to each of the eyepins, and -- boom! -- your earrings are done!
        """,
        photoUrl="https://content.instructables.com/ORIG/FG6/OE42/L4SGSNW8/FG6OE42L4SGSNW8.jpg?auto=webp&frame=1&width=400&height=1024&fit=bounds&md=2c0f349cb547a8b56780d998147ab307",
        videoUrl="",
    )

    planter1=Instruction(
        projectId=32,
        stepOrder=1,
        stepTitle="Cut the Wooden Bars", 
        instructions="""
        I used some 4mm gamari wood beads here for making the back plate. Then I marked about 7 inch each and cut several pieces of them. Because a single planter won't look as good as several planters together.

        Then I sanded and made them smooth.
        """,
        photoUrl="https://content.instructables.com/ORIG/FBM/YAIX/L38QMGDS/FBMYAIXL38QMGDS.jpg?auto=webp&frame=1&width=400&fit=bounds&md=3bcbf21db61b0b470c7df515b52a31d3",
        videoUrl="",
    )

    planter2=Instruction(
        projectId=32,
        stepOrder=2,
        stepTitle=" Mark & Drill Tube Holes", 
        instructions="""
        Next I used 15mm thick wood pieces for making the Tube holders. Then I marked the center and drilled holes with 16mm drill bits. Because we are going to use 15mm Test Tubes here.
        """,
        photoUrl="https://content.instructables.com/ORIG/FKR/FBS1/L38QMGEF/FKRFBS1L38QMGEF.jpg?auto=webp&frame=1&width=400&fit=bounds&md=81829f8510a995956fe4a118ca7cc50a",
        videoUrl="",
    )

    planter3=Instruction(
        projectId=32,
        stepOrder=3,
        stepTitle="Cut and Sand Tube Holders", 
        instructions="""
        Next, cut the wood pieces and made them smooth by sanding every edges and the hole too.
        """,
        photoUrl="https://content.instructables.com/ORIG/FO6/214N/L38QMGFH/FO6214NL38QMGFH.jpg?auto=webp&frame=1&width=800&fit=bounds&md=a11753b02ee438f38e862b3a0867c052",
        videoUrl="",
    )

    planter4=Instruction(
        projectId=32,
        stepOrder=4,
        stepTitle="Final Pieces to Join", 
        instructions="""
        Now, here I have made a few planter pieces and they are ready to join together.
        """,
        photoUrl="https://content.instructables.com/ORIG/FHY/M578/L38QMGGR/FHYM578L38QMGGR.jpg?auto=webp&frame=1&width=600&fit=bounds&md=d0cc7c762af3d5fc06238bbd7963961f",
        videoUrl="",
    )

    planter5=Instruction(
        projectId=32,
        stepOrder=5,
        stepTitle="Fix Tube Holder to the Back", 
        instructions="""
        In this step, I used some regular wood glue to join both the pieces together. Also I hammered a couple of nails in the back to give some extra protection, so that it may never get loose in future.
        """,
        photoUrl="https://content.instructables.com/ORIG/FPF/R0N3/L38QMGOE/FPFR0N3L38QMGOE.jpg?auto=webp&frame=1&width=400&fit=bounds&md=5a782752768f7d4174da56e4cfccca0d",
        videoUrl="",
    )

    planter6=Instruction(
        projectId=32,
        stepOrder=6,
        stepTitle="After Dried", 
        instructions="""
        So, after the wood glue dried up, the planters looks something like these.
        """,
        photoUrl="https://content.instructables.com/ORIG/FL8/6UD9/L38QMGW4/FL86UD9L38QMGW4.jpg?auto=webp&frame=1&width=400&fit=bounds&md=650c1c24437ad49f27d1f127ccc91a11",
        videoUrl="",
    )

    planter7=Instruction(
        projectId=32,
        stepOrder=7,
        stepTitle="Apply Coating Agent", 
        instructions="""
        Next, I used some Varnish as a coating agent and applied all over the areas. It suddenly enhances the look, gives a shiny texture and also protects the wood in long run.
        """,
        photoUrl="https://content.instructables.com/ORIG/FGV/MW0O/L38QMGXH/FGVMW0OL38QMGXH.jpg?auto=webp&frame=1&width=400&fit=bounds&md=2b64460a221963215f9ab523992ea082",
        videoUrl="",
    )

    planter8=Instruction(
        projectId=32,
        stepOrder=8,
        stepTitle="Final Product", 
        instructions="""
        Here is our final finished product of wooden wall planter for holding test tubes. This is a preview of our planters before mounting to the wall.
        """,
        photoUrl="https://content.instructables.com/ORIG/F6N/MBTH/L38QMGW5/F6NMBTHL38QMGW5.jpg?auto=webp&frame=1&width=800&fit=bounds&md=b0268c573aa052001950ecc746846bbb",
        videoUrl="",
    )

    planter9=Instruction(
        projectId=32,
        stepOrder=9,
        stepTitle="Attach to Wall", 
        instructions="""
        Next, I used some double sided tape and added to the back plate of our planters.

        Then I attached them to the wall in a random manners like, in unequal heights and in equal distances.

        Thus it looks really beautiful and attractive to any visitor that notices it.
        """,
        photoUrl="https://content.instructables.com/ORIG/FFN/VWUE/L3BLK91I/FFNVWUEL3BLK91I.jpg?auto=webp&frame=1&width=600&fit=bounds&md=a67e317914644046acaa57ce734236e1",
        videoUrl="",
    )

    planter10=Instruction(
        projectId=32,
        stepOrder=10,
        stepTitle="Test Tube Wall Planter", 
        instructions="""
        So, this wooden test tube wall planter is a very pretty and easy to makeHome Decor item that can suddenly enhances the look of your wall.

        It is very much suitable for bedrooms, offices, drawing rooms, restaurants, waiting rooms or any public places.

        Comment below, where else you use this planters.

        Also, comment any doubt or suggestion, I would love to hear those.
        """,
        photoUrl="https://content.instructables.com/ORIG/FH0/EGPL/L34GE8ZD/FH0EGPLL34GE8ZD.jpg?auto=webp&frame=1&width=600&fit=bounds&md=44568079e48d807922c0bd110d44b8a8",
        videoUrl="",
    )

    mirror1=Instruction(
        projectId=33,
        stepOrder=1,
        stepTitle="Measure and Cut", 
        instructions="""
        You know the old adage...measure twice, cut once! If you do it right, most standard bathroom mirrors can be entirely framed with just two pieces of 8' trim (including the one I linked in the previous step). Measure from the outside to the outside of the mirror and then cut the outside of the angle to that length. My standard mirror size was 30" wide by 36" tall.

        The first cut will be simply to mitre the trim. Naturally, when making a square frame, the easiest way is to set the mitre cut to 45 degrees. This also gives you straight seems (straight with respect to the corners of the mirror). There is one thing to remember when cutting the trim...it can only be cut ONE WAY. Unlike a 2x4 or similar piece of wood, the trim is thinner on one side than the other, meaning you cannot simply flip the piece of trim over. You will want the thin side on the INSIDE of the mirror so you will need to mitre the trim using BOTH mitre directions of 45 degrees. See the pictures demonstrating this with a power mitre saw.

        Once you make the first, cut you will have the 45 degree edge. Measure from the very point of that edge and mark where the point on the other side would be. Rotate your direction of cut, and mitre the opposite side. Now you will have one piece of the frame.

        At this point, you will note on your remaining trim, the angle is opposite of what is needed. You will need to perform another mitre cut to the opposite 45 degrees, essentially cutting off a triangle piece of trim. From there, simply measure, change to the opposite mitre angle, and cut again. At this point, you should have two pieces of cut trim that form have a frame as pictured!
        """,
        photoUrl="https://content.instructables.com/ORIG/FHL/31UF/JWESUJ31/FHL31UFJWESUJ31.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=243374827107025c001c7271f57a8736",
        videoUrl="",
    )

    mirror2=Instruction(
        projectId=33,
        stepOrder=2,
        stepTitle="(Optional) Sand Space for Mirror Clamps", 
        instructions="""
        My mirrors, and many standard builder mirrors have small clamps holding them to the wall (see picture). In order for our frame to lay flat on the mirror you will need to cut out a small space for those clamps. I used a Dremel with the sanding attachment (as pictured in the first step) to accomplish this.

        Simply measure from the edge of the mirrors where those clamps are (they are not necessarily in the same spaces with respect to the edge of the mirror on either side so be sure to measure them all), and mark the back of the trim. Then use your Dremel (or hand sander) to route out a space. See the included picture of the space routed out for the clamps. Most of the mirrors will have four clamps, two on top and two on bottom so you should only have to perform this action on the top and bottom pieces of the frame.
        """,
        photoUrl="https://content.instructables.com/ORIG/F20/YONE/JWESUJ75/F20YONEJWESUJ75.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=374aae2b549e2e33ab2c2c6702463a86",
        videoUrl="",
    )

    mirror3=Instruction(
        projectId=33,
        stepOrder=3,
        stepTitle="Attach Frame to Mirror!", 
        instructions="""
        This is it...last step! Now that you have your frame pieces cut, its time to attach them to your mirror. Grab your level, liquid nails (in the caulk gun) and painters tape! Spread the liquid nails on the backside of the frame pieces in a wave pattern as pictured. Then, using the level, place the bottom piece of the frame on the mirror and ensure the bottom edge of the frame aligns with the bottom edge of the mirror. You can double check with the level.

        Once you get that in place (the liquid nails should gently hold in place) wrap a piece or two of the painters tape as shown. Then, place the two sides, being careful to align them with the corners of the bottom piece as pictured. Finally, place the top piece.

        NOTE: The liquid nails does not dry immediately but it does start to set within 10 minutes or so. I left my tape on for a few hours to ensure it was set.

        That's it for the cheap, easy, DIY mirror frame!
        """,
        photoUrl="https://content.instructables.com/ORIG/F1S/EJLS/JWESUJ64/F1SEJLSJWESUJ64.jpg?auto=webp&frame=1&width=205&height=1024&fit=bounds&md=3f21254b9fad4e6293a772f684b15822",
        videoUrl="",
    )

    airplane1=Instruction(
        projectId=34,
        stepOrder=1,
        stepTitle="Begin Construction", 
        instructions="""
        First, begin by folding your your graph paper in half (excluding three boxes on the perforated side). Once the paper has been folded appropriately, make two marks--13 full boxes apart (allow for a further box back behind the airframe). Use a ruler to make a straight line with the length of 13 boxes directly up 1 row of boxes from the two marks you just made. Then make the canards, vertical stabilizer, spars and counterweight as shown. To avoid confusion, one line you will cut along has been omitted from the photograph; it will be explained on the next step.

        After the fuselage is made, take another sheet of paper that is folded in half along the lines of boxes. Mark out the wing as shown and directed in the photograph's notes (1 box of constant chord at the root; a leading edge sweep forward of 1 box of chord expanding every 4 boxes outward from the constant chord box; and a trailing edge sweep of 3 box of decay along the 5 boxes outward from the center). This will complete the wings.

        Solid lines indicate places to cut. Dotted lines indicate fold lines.

        Note: 1 box = 0.25 inches
        """,
        photoUrl="https://content.instructables.com/ORIG/F02/YPJX/J12O172E/F02YPJXJ12O172E.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=49453a35746c50f11a338d0e770fd8d9",
        videoUrl="",
    )

    airplane2=Instruction(
        projectId=34,
        stepOrder=2,
        stepTitle="Making the Fuselage; Stapling", 
        instructions="""
        Cut out your fuselage and cut away the bits of the canards beyond the horizontal solid line. Then fold the counterweights into place. Cut away one of the vertical stabilizers as shown in the fifth photograph.

        Fold along the dotted horizontal lines then tape where indicated. After making the necessary taping, cut away the portion of the rear fuselage below the diagonal line. Then apply one staple in the area of the counterweight. Secure the rear ventral portion with tape as shown to complete the step.
        """,
        photoUrl="https://content.instructables.com/ORIG/FUL/XS42/J12O17SU/FULXS42J12O17SU.jpg?auto=webp&frame=1&width=400&height=1024&fit=bounds&md=3a101109cc77b658b56bacfa1d9bd394",
        videoUrl="",
    )

    airplane3=Instruction(
        projectId=34,
        stepOrder=3,
        stepTitle="Applying the Wings", 
        instructions="""
        Cut out your Reaper's wings and lay them beneath the fuselage as shown. Apply tape where designated to secure them to the spars. Apply tape to the LERX joint where noted. This will complete the aircraft.
        """,
        photoUrl="https://content.instructables.com/ORIG/F8C/ONN8/J12O18N6/F8CONN8J12O18N6.jpg?auto=webp&frame=1&width=400&height=1024&fit=bounds&md=3dca8b98c0d2bf87cd59b25847d2bd31",
        videoUrl="",
    )

    airplane4=Instruction(
        projectId=34,
        stepOrder=4,
        stepTitle="Flight", 
        instructions="""
        Despite its unusual shape, the Reaper flies quite conventionally and behaves predictably. With proper trimming, the aircraft should fly where it is pointed.

        Launches should be done at moderate speed at neutral or slightly positive or negative attitudes. Test flights should be conducted to see if any trimming needs to be done. If the aircraft dives, add camber to canards by bending their leading and trailing edges downward slightly on each side.

        Additional applicable surfaces include elevators (as canard trim), ailerons, flaps, air brakes and a trimmable rudder. Enjoy!
        """,
        photoUrl="https://content.instructables.com/ORIG/F53/CS58/J12O18NU/F53CS58J12O18NU.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=d673ef4bdd1ba9b86081c827d21faa83",
        videoUrl="",
    )

    garden_box1=Instruction(
        projectId=35,
        stepOrder=1,
        stepTitle="Cutting and Pre Assembly", 
        instructions="""
        Cut all boards and bars and posts to the desired length, 
        Pre assemble the front and back sides as seen on the picture
        """,
        photoUrl="https://content.instructables.com/ORIG/F7R/CMWM/L49W2AOJ/F7RCMWML49W2AOJ.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=e10197678df240b6300ce74086b42d63",
        videoUrl="",
    )

    garden_box2=Instruction(
        projectId=35,
        stepOrder=2,
        stepTitle="Assembly of All 4 Sides", 
        instructions="""
        Assemble all 4 sides, 
        Connect to the corner posts, 
        Install dimpled sheet and chicken wire inside the bed
        """,
        photoUrl="https://content.instructables.com/ORIG/FZO/B8NT/L49W2B30/FZOB8NTL49W2B30.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=25afa306651e3d3f372ce1ff28339643",
        videoUrl="",
    )

    garden_box3=Instruction(
        projectId=35,
        stepOrder=3,
        stepTitle="Top Cover and Filling", 
        instructions="""
        Install the boards on the top by using sheet brackets for example, 
        Paint all sides and the top with wood stain, 
        Fill the bed with all sorts of green waste and lots of soil
        """,
        photoUrl="https://content.instructables.com/ORIG/FWY/2TUJ/L49W2862/FWY2TUJL49W2862.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=f0f4dd94b4a433ce214940e783b7159a",
        videoUrl="",
    )

    garden_box4=Instruction(
        projectId=35,
        stepOrder=4,
        stepTitle="Decoartion", 
        instructions="""
        The decoration element can make a real difference and turns any raised bed into an eye catcher

        Choose a decorative template e.g. from etsy.com
        Fairy svg | Etsy DE
        cut with fretwork tool
        If it is a complex shape as my "Garden Fairy" ask someone with a CNC Mill to cut it for you
        paint in a nice colour
        install to the bed
        """,
        photoUrl="https://content.instructables.com/ORIG/FJO/1L2X/L49W2864/FJO1L2XL49W2864.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=884bb3efe2b579e5d6178ccc7e92263d",
        videoUrl="",
    )

    garden_box5=Instruction(
        projectId=35,
        stepOrder=5,
        stepTitle="Finished", 
        instructions="""
        No raised garden bed looks like the other.

        I hope to give you some inspiration for your own project!

        Enjoy the work and the result. Good luck.
        """,
        photoUrl="https://content.instructables.com/ORIG/FON/H93U/L49W2DCB/FONH93UL49W2DCB.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=11bc55e6318ca3d24b0ade6eabae1a82",
        videoUrl="",
    )

    rc_airplane1=Instruction(
        projectId=36,
        stepOrder=1,
        stepTitle="Fuselage", 
        instructions="""
        For the fuselage, checkout above image or you can make your own fuselage by taking different measurements ratio and sizes.
        Cut two layers of fuselage ( Image1) and join them by making interior structure as shown above in image's (image2).
        """,
        photoUrl="https://content.instructables.com/ORIG/FCS/OFJV/KZ9ULQTS/FCSOFJVKZ9ULQTS.jpg?auto=webp&frame=1&crop=3:2&width=501&height=1024&fit=bounds&md=f328a8b0b66a09a4084d12810e07e32c",
        videoUrl="",
    )

    rc_airplane2=Instruction(
        projectId=36,
        stepOrder=2,
        stepTitle="Vertical Stab & Horizontal Stab", 
        instructions="""
        Now we will work on the tail section, For the reference you can see the measurements of my design.
        Its your choice how you want to give looks to your airplane.
        For more clarification look at above images.
        Once done, Tape it.
        """,
        photoUrl="https://content.instructables.com/ORIG/FUW/QUF7/KZ9ULQ1T/FUWQUF7KZ9ULQ1T.png?auto=webp&frame=1&crop=3:2&width=900&fit=bounds&md=f7bc20a45ea6913eba5669e24e71fabb",
        videoUrl="",
    )

    rc_airplane3=Instruction(
        projectId=36,
        stepOrder=3,
        stepTitle="Assembling Step 1 & Step 2", 
        instructions="""
        Now we will assemble the fuselage and the stabilizers.
        Make a cut at the end of the fuselage for inserting the horizontal stabilizer.
        Do the same for vertical stabilizer make a cut at the horizontal center and stick the vertical stab.
        """,
        photoUrl="https://content.instructables.com/ORIG/FNP/CYXP/KZ9ULR38/FNPCYXPKZ9ULR38.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=e89a282d189595f19d3db8cb67e70f43",
        videoUrl="",
    )

    rc_airplane4=Instruction(
        projectId=36,
        stepOrder=4,
        stepTitle="Motor Mounting", 
        instructions="""
        Now take a plywood piece and mount the motor on it and then stick the plywood at leading edge just remember motor should be downwards; as the angle matters the thrust will generate downwards so that lift can be achieved.
        Once done, stick more plywood at the corners for more strength as shown above in the images.
        """,
        photoUrl="https://content.instructables.com/ORIG/F82/1DWV/KZ9ULS0K/F821DWVKZ9ULS0K.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=116161c55cbe759a45d3990806ee4e7b",
        videoUrl="",
    )

    rc_airplane5=Instruction(
        projectId=36,
        stepOrder=5,
        stepTitle="Landing Gear", 
        instructions="""
        Now take a thicker steel rod and bend it as shown in above image.
        Now attach the tires with the lower part and see if it's moving or not.
        Many people say that landing gears just add more Weight to their planes and they are not useful so yes its kind of true but I personally recommend this because sometimes its too difficult to manage both the transmitter and the plane it's completely optional :)
        Once done, stick the landing gears to the bottom part of the plane.
        """,
        photoUrl="https://content.instructables.com/ORIG/FZ7/91LH/KZ9ULUCS/FZ791LHKZ9ULUCS.jpg?auto=webp&frame=1&width=247&height=1024&fit=bounds&md=2197fa40601be104ae40405ab9e0f273",
        videoUrl="",
    )

    rc_airplane6=Instruction(
        projectId=36,
        stepOrder=6,
        stepTitle="Wing", 
        instructions="""
        This is the most important part and this will decide your airplane characteristics.
        For making the wing take a thin steel rod and some strips of foam and stick them on the doted lines image1.
        Now apply some heat and fold the wing from the dark line as shown in image 1.
        """,
        photoUrl="https://content.instructables.com/ORIG/F48/F1O6/KZ9ULV8N/F48F1O6KZ9ULV8N.jpg?auto=webp&frame=1&width=400&height=1024&fit=bounds&md=fac0f94d8d8e0f662cd55814d5821a2b",
        videoUrl="",
    )

    rc_airplane7=Instruction(
        projectId=36,
        stepOrder=7,
        stepTitle="Electronics'", 
        instructions="""
        Now we will be installing all electronics such as ESC ,servos and the battery.
        Install servos for the elevator, rudder and ailerons.
        Install the servos and control assembly to each control surface keeping in mind the neutral positions of each control surfaces.

        Connect ESC to the motor and connect all other connection to the receiver such as -

        Channel1 - ailerons
        Channel2 - elevator
        Channel3 - throttle
        Channel4 - rudder
        """,
        photoUrl="https://content.instructables.com/ORIG/F61/WX8O/KZ9ULY6V/F61WX8OKZ9ULY6V.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=23c36f756c95d3ca857aabfccae670b8",
        videoUrl="",
    )

    rc_airplane8=Instruction(
        projectId=36,
        stepOrder=8,
        stepTitle=" Putting Everything Together", 
        instructions="""
        Check all the control surfaces before fight and make sure that they are working properly.
        Check CG of the plane before flight.
        Make sure your all electronics are working properly.
        You can add different touches to your plane so that it looks amazing I personally love simple and classic planes.
        """,
        photoUrl="https://content.instructables.com/ORIG/FL5/M3Q4/KZ9ULZFB/FL5M3Q4KZ9ULZFB.jpg?auto=webp&frame=1&width=490&height=1024&fit=bounds&md=169d45eb3836d53627141a6aece0c17b",
        videoUrl="",
    )

    rc_airplane9=Instruction(
        projectId=36,
        stepOrder=9,
        stepTitle="Done", 
        instructions="""
        Congratulations guys ! we made it.

        I hope you enjoyed

        Thanks for watching : )

        GOOD LUCK FOR YOUR FIRST MAIDEN FLIGHT !!
        """,
        photoUrl="https://content.instructables.com/ORIG/FAW/A3GM/KZ9UM0AA/FAWA3GMKZ9UM0AA.jpg?auto=webp&frame=1&crop=3:2&width=600&height=1024&fit=bounds&md=91a0236dfde24e987fafb559dafce5ec",
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
    db.session.add(bike_mount1)
    db.session.add(bike_mount2)
    db.session.add(bike_mount3)
    db.session.add(bike_mount4)
    db.session.add(bike_mount5)
    db.session.add(bike_mount6)
    db.session.add(bike_mount7)
    db.session.add(data_crystals1)
    db.session.add(data_crystals2)
    db.session.add(data_crystals3)
    db.session.add(data_crystals4)
    db.session.add(data_crystals5)
    db.session.add(data_crystals6)
    db.session.add(data_crystals7)
    db.session.add(data_crystals8)
    db.session.add(data_crystals9)
    db.session.add(data_crystals10)
    db.session.add(mpcnc_controller1)
    db.session.add(mpcnc_controller2)
    db.session.add(garage_door1)
    db.session.add(garage_door2)
    db.session.add(garage_door3)
    db.session.add(garage_door4)
    db.session.add(garage_door5)
    db.session.add(garage_door6)
    db.session.add(garage_door7)
    db.session.add(poop_bag1)
    db.session.add(poop_bag2)
    db.session.add(poop_bag3)
    db.session.add(poop_bag4)
    db.session.add(cup_carrier1)
    db.session.add(cup_carrier2)
    db.session.add(cup_carrier3)
    db.session.add(cup_carrier4)
    db.session.add(cup_carrier5)
    db.session.add(cup_carrier6)
    db.session.add(cup_carrier7)
    db.session.add(cardboard1)
    db.session.add(cardboard2)
    db.session.add(cardboard3)
    db.session.add(cardboard4)
    db.session.add(cardboard5)
    db.session.add(cardboard6)
    db.session.add(cardboard7)
    db.session.add(cardboard8)
    db.session.add(cardboard9)
    db.session.add(zentrierwinkel1)
    db.session.add(zentrierwinkel2)
    db.session.add(zentrierwinkel3)
    db.session.add(zentrierwinkel4)
    db.session.add(zentrierwinkel5)
    db.session.add(zentrierwinkel6)
    db.session.add(zentrierwinkel7)
    db.session.add(zentrierwinkel8)
    db.session.add(smores1)
    db.session.add(smores2)
    db.session.add(smores3)
    db.session.add(gearbox1)
    db.session.add(gearbox2)
    db.session.add(gearbox3)
    db.session.add(gearbox4)
    db.session.add(gearbox5)
    db.session.add(gearbox6)
    db.session.add(garden_tables1)
    db.session.add(garden_tables2)
    db.session.add(garden_tables3)
    db.session.add(garden_tables4)
    db.session.add(garden_tables5)
    db.session.add(garden_tables6)
    db.session.add(garden_tables7)
    db.session.add(garden_tables8)
    db.session.add(gummy_bears1)
    db.session.add(gummy_bears2)
    db.session.add(gummy_bears3)
    db.session.add(gummy_bears4)
    db.session.add(gummy_bears5)
    db.session.add(gummy_bears6)
    db.session.add(gummy_bears7)
    db.session.add(fortune_cookie1)
    db.session.add(fortune_cookie2)
    db.session.add(fortune_cookie3)
    db.session.add(fortune_cookie4)
    db.session.add(fortune_cookie5)
    db.session.add(fortune_cookie6)
    db.session.add(fortune_cookie7)
    db.session.add(fortune_cookie8)
    db.session.add(fortune_cookie9)
    db.session.add(planter1)
    db.session.add(planter2)
    db.session.add(planter3)
    db.session.add(planter4)
    db.session.add(planter5)
    db.session.add(planter6)
    db.session.add(planter7)
    db.session.add(planter8)
    db.session.add(planter9)
    db.session.add(planter10)
    db.session.add(mirror1)
    db.session.add(mirror2)
    db.session.add(mirror3)
    db.session.add(airplane1)
    db.session.add(airplane2)
    db.session.add(airplane3)
    db.session.add(airplane4)
    db.session.add(garden_box1)
    db.session.add(garden_box2)
    db.session.add(garden_box3)
    db.session.add(garden_box4)
    db.session.add(garden_box5)
    db.session.add(rc_airplane1)
    db.session.add(rc_airplane2)
    db.session.add(rc_airplane3)
    db.session.add(rc_airplane4)
    db.session.add(rc_airplane5)
    db.session.add(rc_airplane6)
    db.session.add(rc_airplane7)
    db.session.add(rc_airplane8)
    db.session.add(rc_airplane9)
    
    db.session.commit()


def undo_instructions():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.instructions RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM instructions")

    db.session.commit()