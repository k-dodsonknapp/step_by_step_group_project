from unicodedata import category
from app.models.db import db
from app.models.project import Project
import os


environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")

# demo projects
def seed_project():
    bird_house= Project(
        userId=1, 
        title="How to build a bird house.", 
        titleImage="https://images.unsplash.com/photo-1590238750866-f99d3febe496?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NXx8YmlyZCUyMGhvdXNlfGVufDB8fDB8fA%3D%3D&w=1000&q=80", 
        overview="This is how to construct a bird house!",
        category="Crafts",
        favorites=0,
        views=0,
    )

    casino_clock= Project(
        userId=2, 
        title="Casino'clock - Playing card flap display / clock", 
        titleImage="https://content.instructables.com/ORIG/F8U/KR3T/KZCPHOFJ/F8UKR3TKZCPHOFJ.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=16727930c4e9a859906b057dd58a338d", 
        overview="""
                    One of the main difficulty to make a split flap display with 3D printer is the fabrication of flaps. 
                    Therefore I used off-the-shelf playing cards for flaps, and made a funny and crazy clock with minimum number of parts. 
                    Simple design : each display unit consists of only 3 types of parts. Sensor is not used to find the origin. 
                    Funny motion : by arranging cards randomly, you can enjoy busy motion of flaps 
                    WiFi time acquisition : current time is acquired via WiFi using ntp
                """,
        category="Circuits",
        favorites=0,
        views=0,
    )

    one_board_mug= Project(
        userId=3, 
        title="One Board Mug", 
        titleImage="https://content.instructables.com/ORIG/FST/TDM1/KZBA18KY/FSTTDM1KZBA18KY.jpg?auto=webp&frame=1&width=612&height=1024&fit=bounds&md=eb345ed6f0c79b14398aa15b45a9edb5", 
        overview="Create a fun and unique drinking vessel from one board of pine.",
        category="Workshop",
        favorites=0,
        views=0,
    )

    skillet_burger= Project(
        userId=1, 
        title="Onion Skillet Bacon Cheeseburgers", 
        titleImage="https://content.instructables.com/ORIG/FSA/PGFW/KYK4NWBL/FSAPGFWKYK4NWBL.jpg?auto=webp&frame=1&width=700&height=1024&fit=bounds&md=e5c78e47e1d1406d50a53dc73e21b425", 
        overview="""
                    Looking for a delicious stacked-up burger? Then you came to the right place! A bacon cheeseburger with onions cooked in bacon grease!
                    
                    Makes 6 Burgers Prep Time 10 minutes Cook time 30 minutes

                    Ingredients

                    3 Yellow Onions, cut into slices
                    6 Brioche Buns
                    6 Slices Sharp Cheddar
                    8 Slices Thick-Cut Bacon, cut in half
                    1 cup Bread and Butter Pickles
                    For the Patty:

                    1 lb Ground Beef
                    1 lb Ground Pork
                    1 bag Garlic Pepper Crispy Onions, crushed
                    1 tsp Salt
                    1 tsp Red Pepper Flakes
                    1 tsp Parsley
                    For the Sauce:

                    1/2 cup Mayo
                    1/2 cup BBQ Sauce
                    1/4 cup Pickle Juice
                """,
        category="Cooking",
        favorites=0,
        views=0,
    )

    james_webb_clock= Project(
        userId=2, 
        title="James Webb Space TeleClock", 
        titleImage="https://content.instructables.com/ORIG/FY7/2PZZ/KYVK6ZDO/FY72PZZKYVK6ZDO.jpg?auto=webp&frame=1&width=597&height=1024&fit=bounds&md=77bcb2dcb44a2791d61936b6c3c87b86", 
        overview="""
                    Inspired by the launch of the James Webb Telescope on 24/12/2021, I was driven to make something to commemorate this incredible achievement, hence the James Webb Space Teleclock. The aim was to make a decorative item for the home that resembled the mirror portion of the telescope which in my opinion is not only an engineering marvel but a gorgeous one at that. Making it into a clock was just to make it functional as well :)

                    If you are interested in the 25 years of engineering that went into building the James Webb Telescope I would recommend watching this episode of Real Engineering
                """,
        category="Living",
        favorites=0,
        views=0,
    )

    slowmo_birds= Project(
        userId=3, 
        title="How to Photograph Birds in Flight the Easy Way", 
        titleImage="https://content.instructables.com/ORIG/FHX/FUC6/KY2ZEWJO/FHXFUC6KY2ZEWJO.jpg?auto=webp&frame=1&width=933&fit=bounds&md=d9800a2e705e47bde451618173fe795d", 
        overview="""
                    With a simple set-up, you can produce excellent photographs of birds in flight--from the comfort of your house! Birds are attractive targets for wildlife photographers. They are aesthetically pleasing, ubiquitous, and charismatic. But once one has mastered the "bird on a stick" photo, a photographer may feel challenged to produce more interesting photos. Bird in flight (BIF) photos are dramatic, but much harder to get. Some degree of chance is usually required, and a long time in the field. The method demonstrated here is relatively simple and allows one to take BIF images in the dead of winter, when birds are most drawn to feeders. Meanwhile, the photographer is warm and cozy.
                """,
        category="Outside",
        favorites=0,
        views=0,
    )

    dragonfly= Project(
        userId=1, 
        title="3D Printed Dragonfly With Tinkercad", 
        titleImage="https://content.instructables.com/ORIG/F4R/GOS2/KSN80SUN/F4RGOS2KSN80SUN.jpg?auto=webp&frame=1&width=874&height=1024&fit=bounds&md=346c7b528b8144375851419c41c9e424", 
        overview="""
                    Do you hear about bamboo dragonflies? I played it in my childhood, which kids' hands can make with a stick and long blade fixed on the top of the shaft. Kids can spin the pole with their hands to let it fly high in the air, which looks like a dragonfly. It is a fascinating toy to play with among kids' outdoor activities. This time I made it with Autodesk Tinkercad and the 3D printer.
                """,
        category="Teachers",
        favorites=0,
        views=0,
    )

    arcade_stick = Project (
        userId = 1,
        title="Simple Wood Arcade Stick",
        titleImage="https://content.instructables.com/ORIG/FOO/JQM4/L1C5JWFO/FOOJQM4L1C5JWFO.jpg?auto=webp&frame=1&width=790&height=1024&fit=bounds&md=5bc681ceff36641e5720e856a562ab9d",
        overview="""
        I’ve been into playing retro games lately and thought it would be cool to build an arcade stick (also called a “fight stick”) for use with RetroPie. 
        I had some leftover IKEA oak butcher block from a kitchen project and figured it would be a great material to use for this. 
        I love the look and the feel of it and at 1 1/8-inch thick, it’s super sturdy and solid. Also, it’s easy to treat with mineral oil to make it look nice.
        """,
        category="Circuits",
        favorites=0,
        views=0,
    )

    minecraft_torch = Project (
        userId = 3,
        title="MINECRAFT-Inspired Light-Up LED Torch",
        titleImage="https://content.instructables.com/ORIG/F4Y/BMJD/L1AQ24KM/F4YBMJDL1AQ24KM.jpg?auto=webp&frame=1&crop=3:2&width=800&height=1024&fit=bounds&md=ccb022a3073c05b57df028ebe30400e0",
        overview="""
        We love Paper Circuits and yes, we still love MINECRAFT! We've created templates for these torches as well as six other Minecraft-Inspired projects! We've included a PDF eBook with all the files.

        If you are brand new to building paper circuits check out our guide to Getting Started with Paper Circuits to learn the basics.
        """,
        category="Circuits",
        favorites=0,
        views=0,
    )

    giant_matches=Project(
        userId=3,
        title="Giant Matches - That Work!",
        titleImage="https://content.instructables.com/ORIG/FM0/LQTT/L4LBOJCW/FM0LQTTL4LBOJCW.jpg?auto=webp&frame=1&crop=3:2&width=600&height=1024&fit=bounds&md=a1f9f4fefd53e9ff6d07d759b93f9d30",
        overview="""
        Many years ago, I saw Shrek The Musical back in London. There was one scene in particular that I remember very well, that involved a giant box of matches. Unfortunately, that day no matches were lit on the scene, but that image of a giant match in a huge box stuck in my brain. There is something quirky about it that I dig - and above all, I was really curious if such a big match would actually light up and how big would that flame then be.

        So, without any further ado, let's make some giant matches with a nice box to go with them, to answer those burning questions.
        """,
        category="Outside",
        favorites=0,
        views=0,
    )

    bike_lamp=Project(
        userId=1,
        title="Be Seen! 3D Printed Bike Lights With Fusion 360",
        titleImage="https://content.instructables.com/ORIG/FX1/S8ZB/L2EQF6ZI/FX1S8ZBL2EQF6ZI.jpg?auto=webp&frame=1&width=400&height=1024&fit=bounds&md=973936be7f8d4952d83d6839f695e0a9",
        overview="""
        When I'm out and about on my bicycle at night I like to Be Seen, the more lights the better, I do have some USB rechargeable lights and they work really well, my bike is electric and it has of all things a USB port, I'm thinking along the lines of having a Bike lamp as say a reserve lamp, it could run off either AA or AAA Batteries or USB?

        The trips I make on an evening are no marathons but a time or 2 I've forgotten to charge my lights or something and here in the UK having no lights carries a hefty fine.

        My cycle helmet has a built in rear LED lamp, so my thinking is with a reserve front lamp I've got all bases covered, not sure how much it would drain the bike battery yet but should be ok over short distances, and the LED lamp that I'm going to use is 5v with 9 LED's and on 4 xAA batteries (even they could be rechargeable) the LED lasts for 5 Hours.

        After seeing the light it's time to get on with a design.
        """,
        category="Outside",
        favorites=0,
        views=0,
    )

    rainbow=Project(
        userId=6,
        title="Holographic Rainbow Reflective 3D Prints - 3D Printing on Diffraction Grating Sheets",
        titleImage="https://content.instructables.com/ORIG/FG5/GBXG/L4R1CJG3/FG5GBXGL4R1CJG3.jpg?auto=webp&frame=1&width=632&height=1024&fit=bounds&md=c6aef9abb5200a296087377b2bacd5f0",
        overview="""
        A few years ago, I learned you could 3D print on a diffraction grating sheet and it will transfer the rainbow reflectiveness onto the print (the same as this chocolate). Like most things, I tried it out, had some luck and some failure, then moved on to something else. Luckily, I decided to finally visit it again and am having consistent good results and wanted to share how I'm doing it, so you can too!

        *Be aware that the reflectiveness works best in direct sunlight, but can also work with other lights.
        """,
        category="Workshop",
        favorites=0,
        views=0,
    )

    frankenstein=Project(
        userId=5,
        title="Teach Electrical Circuits- Frankenstein ER",
        titleImage="https://content.instructables.com/ORIG/FC7/V4PZ/L3YGJH7E/FC7V4PZL3YGJH7E.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=ea12fd6900ceea153d72023192902151",
        overview="""
        The game operation is a standard in my electrical circuit curriculum. I love the language connection as the students get butterflies in their stomach trying to avoid the shrill buzzer that indicates the circuit has been completed.  It is also the perfect introduction to  Frankenstein ER. The room is dimmed, mangled monster heads are delivered to teams to repair, to rebuild, to advance them from interns to doctors that can build their own Frankenstien to protect their candy stash.  

        Teaching circuits always lights up my day and I am always looking for projects that connect learning to seasonal events.  Years ago, I saw a monster snatch game in Make magazine (https://makezine.com/projects/monster-candy-game/).  It was a great idea but too complicated and expensive for an elementary classroom.  So I modified it to an easy, fun and project that produces monster size learning and is a seasonal favorites that rewards the player with the chance to get a piece of candy for understanding the parts of a circuit.
        """,
        category="Teachers",
        favorites=0,
        views=0,
    )

    ice_cream=Project(
        userId=4,
        title="World's Easiest Way to Make Dipped Ice Cream",
        titleImage="https://content.instructables.com/ORIG/FEW/LVTX/L4LBN3M7/FEWLVTXL4LBN3M7.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=1a73c1c279c44233c557310d38d9331d",
        overview="""
        I scream! You scream! We all scream for Ice Cream! Everyone loves ice cream, but have you ever thought of adding It with some chocolate and peanuts. Just thinking of that makes me hungry for dipped ice cream. This is why you have to try this recipe.
        """,
        category="Cooking",
        favorites=0,
        views=0,
    )

    hot_chocolate=Project(
        userId=3,
        title="French Hot Chocolate",
        titleImage="https://content.instructables.com/ORIG/F9O/VXCJ/KZ9UMEEF/F9OVXCJKZ9UMEEF.jpg?auto=webp&frame=1&width=570&height=1024&fit=bounds&md=ef91a0a81d51a6ebb85cef4412143f65",
        overview="""
        French Hot Chocolate is the perfect beverage to sip on after being out on a cold winter day, but not only is it delicious and warm but it is very easy to make.
        """,
        category="Cooking",
        favorites=0,
        views=0,
    )

    cocoa_bombs=Project(
        userId=2,
        title="☕🍫Hot Cocoa Bombs🍫☕",
        titleImage="https://content.instructables.com/ORIG/FKX/H8AQ/KV3TDZJW/FKXH8AQKV3TDZJW.png?auto=webp&frame=1&width=515&fit=bounds&md=4eb1a85d2289fbae7b6fb9d9c8f3227d",
        overview="""
        I made this recipe because I feel like it is always so hard to make hot cocoa, but with this recipe, you can just plop one in the milk and stir for a little bit then you have yourself a nice little cup of fast and easy hot cocoa. This is the second instructable I have created. I love doing Instructables. It is such a fun way to express your creativity.
        """,
        category="Cooking",
        favorites=0,
        views=0,
    )

    blossom=Project(
        userId=1,
        title="Blossom Branch Arrangement",
        titleImage="https://content.instructables.com/ORIG/F57/NS1O/L4PLX73W/F57NS1OL4PLX73W.png?auto=webp&frame=1&width=963&fit=bounds&md=5bd39168d63663cb0766616b5645ed96",
        overview="""
        Hello everyone! I'm so excited to share this upcycled craft with all of you. We're using just a few materials, and what is so exciting about this is that I had all of my materials on hand. If you were to have to purchase materials, I purchased my paint at my local Walmart for $0.50 each, and my craft foam was $1.25 at my local Dollar Tree. You can also find your floral at Dollar Tree, or any craft store at a discounted price.
        """,
        category="Craft",
        favorites=0,
        views=0,
    )

    torus=Project(
        userId=6,
        title="How to Make a Cardboard Torus(You Can Also Make a Sculpture Out of It As It Is Being Shown)",
        titleImage="https://content.instructables.com/ORIG/FVW/1Z2N/L42QV8A3/FVW1Z2NL42QV8A3.jpg?auto=webp&frame=1&width=350&height=1024&fit=bounds&md=5fa4aa68632c29e529a2aac6c742361b",
        overview="""
        In this image I created a cardboard sculpture. The geometric shape I wanted to use was the torus so the main focus of this sculpture was how to make a tours by using carboard. And as stated in the title I presented this original handmade sculpture as an example on what is capable if one were to create a torus out of carboard.
        """,
        category="Craft",
        favorites=0,
        views=0,
    )

    bike_mount=Project(
        userId=5,
        title="Bike Wall Mount, SUPER HANDY!",
        titleImage="https://content.instructables.com/ORIG/FFH/3EW3/JUGRSTJH/FFH3EW3JUGRSTJH.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=ff6f8b77c27ca3f7462c30e0fbe72903",
        overview="""
        I needed a bike rack and came up with this.

        If you want to watch the video check out the ol' youtube: https://www.youtube.com/watch?v=0NQ9S2y85i0&t=6s

        This was a fun project and it works really well. I use it consistently. The Process of figuring out how to make the hands was great and would consider making some coat hangers that are similar.
        """,
        category="Workshop",
        favorites=0,
        views=0,
    )

    data_crystals=Project(
        userId=4,
        title="Data Crystals: 3D Data Visualizations From Open Data",
        titleImage="https://content.instructables.com/ORIG/F1G/ONSR/HTPUP3BW/F1GONSRHTPUP3BW.jpg?auto=webp&frame=1&width=1024&fit=bounds&md=799f225ed8f23b854d1a2bcf21145512",
        overview="""
        One of my projects while a resident artist at Autodesk has been to create "Data Crystals" —  3D prints that I algorithmically generate using data as input. I design these 3D data visualizations for aesthetics over legibility and they show off what can be done with code and 3D printing.

        I've finished the first three and have several more in production. This batch is derived from San Francisco Open Data sets.

        This Instructable will give an overview of my creative and technical process for making these and I hope will encourage others to think about creative data visualization techniques.

        At some point, I will likely share my code, but right now this project is too fresh and the code is too rough for public consumption. 
        """,
        category="Workshop",
        favorites=0,
        views=0,
    )

    mpcnc_controller=Project(
        userId=3,
        title="Wireless MPCNC Controller (3d Printed CNC System)",
        titleImage="https://content.instructables.com/ORIG/FMT/3TVC/L4MRAN41/FMT3TVCL4MRAN41.jpg?auto=webp&frame=1&crop=3:2&width=918&height=1024&fit=bounds&md=c9e814e7041e69074571ca97911e796d",
        overview="""
        This is my wireless remote for my 3d printed CNC machine (MPCNC).
        """,
        category="Circuits",
        favorites=0,
        views=0,
    )

    garage_door=Project(
        userId=2,
        title="How to Make a Garage Door (EASY!!!)",
        titleImage="https://content.instructables.com/ORIG/FN0/9F4R/L4IQAABR/FN09F4RL4IQAABR.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=873d56eaa22151a580dfd9028725cb2c",
        overview="""
        This is a EASY arduino project that you could create to impress your teacher and friends. This project is an IR sensor-controlled garage door. It uses 2 Servo motor's to move the garage door into an opened and closed orentation. The inferred sensor (IR) is effective and long range with a range of 1-5 meters. This project is great When paired with an arduino car project.
        """,
        category="Circuits",
        favorites=0,
        views=0,
    )

    poop_bag=Project(
        userId=1,
        title="Leather Dog Poop Bag Holder / Dispenser",
        titleImage="https://content.instructables.com/ORIG/FDD/PP0I/L4TW9314/FDDPP0IL4TW9314.jpg?auto=webp&frame=1&width=800&height=1024&fit=bounds&md=ca9b3c7eb00cbcd727277bfb4e2509b2",
        overview="""
        In this project i wanted to find a stylish and practical solution for dog waste/poop bags. And this is it, a very cool project where you can use your leather scraps. If you are new in leathercraft, this project is for you my friend. This holder/dispenser can accommodate a roll in size of 3 cm x 6 cm (1,1811 inch x 2,3622 inch). With a carabiner hook you can attach the holder on your jeans, pents or your dog leash. By the way, leather is very robust and sustainable material. I LOVE working with leather so much. Okay, let us make one :)
        """,
        category="Craft",
        favorites=0,
        views=0,
    )

    cup_carrier=Project(
        userId=6,
        title="D4E1 - Coffee Cup Carrier",
        titleImage="https://content.instructables.com/ORIG/FQX/PSFF/L4H1A92I/FQXPSFFL4H1A92I.jpg?auto=webp&frame=1&width=400&height=1024&fit=bounds&md=f7f4d34996de50b46226aee24b0acf40",
        overview="""
        As part of the Postgraduate education Makerskills for Occupational Therapists at Howest University College, Kortrijk (Belgium) the Coffee cup Carrier has been developed for and together with K, a young woman with Cerebral Palsy.

        This condition not only impacts K’s strength and proprioception of the upper left limb, it also impacts her balance and gait. Consequently, when K likes to grab a cup of coffee, she tends to spill coffee especially when stairs are involved. When walking up or down the stairs, K needs her right hand to hold on to the banister which forces her to carry the coffee cup in the left hand. Due to the tremor of the left hand and the diminished proprioception, she is bound to spill coffee. To avoid handburn or sliding over the spilt coffee, she needs to ask others to carry her coffee cup. However, as a strong an independent young woman, she would like to carry her coffee cup herself. That is why we created this Coffee cup Carrier inspired on the Spillnot designs of Steve.Dickie and Dave88 found on Thingiverse.

        To meet K's demand for portability, the Coffee cup Carrrier is composed out of two parts in 3D print: a platform to put the drink on and an upright handle with ribbon to carry the whole. Both parts are held together by a screw with nut. As the working of the Spillnot breaks when you would coincidently bump into an obstacle, for example a wall or a banister, we introduced a non-skid layer on the platform and a velcro to tie the cup or glass to the handle. The non-skid prevents the cup from sliding over the platform and the velcro secures the carrier that the glass or cup won’t fall off.

        It is a simple design which easily can be made by anyone with access to a 3D printer and this building plan. Have fun with it and feel free to adjust elements according to your own situation.
        """,
        category="Living",
        favorites=0,
        views=0,
    )

    cardboard=Project(
        userId=5,
        title="Cardboard Castle",
        titleImage="https://content.instructables.com/ORIG/FNC/1PQE/L41BGOIL/FNC1PQEL41BGOIL.jpg?auto=webp&frame=1&width=800&height=1024&fit=bounds&md=a99f3f3694457fb7646de8b28b6d6d63",
        overview="""
        Collect as many cardboard boxes as possible!
        I end up getting the majority of mine off Facebook marketplace and my local Harvey Norman store also gave me some of the large fridge boxes.
        """,
        category="Craft",
        favorites=0,
        views=0,
    )

    zentrierwinkel=Project(
        userId=4,
        title="Zentrierwinkel",
        titleImage="https://content.instructables.com/ORIG/FCW/U7PE/L3EGD014/FCWU7PEL3EGD014.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=abd6b128a78d67a20b9c2bcfb75883cb",
        overview="""
        Heute zeige ich dir, wie man einen Zentrierwinkel einfach selber bauen kann. Ein Zentrierwinkel hilft dir dabei, den Mittelpunkt runder Objekte zu bestimmen. Was du zum Bauen dieses Mittelpunktfinders brauchst, siehst du gleich.
        """,
        category="Teachers",
        favorites=0,
        views=0,
    )

    smores=Project(
        userId=3,
        title="HOMEMADE S’MORES ICE CREAM",
        titleImage="https://content.instructables.com/ORIG/FIN/DUZL/L4MR0XIO/FINDUZLL4MR0XIO.jpg?auto=webp&frame=1&width=875&height=1024&fit=bounds&md=652db637f3dfc662539d4cec102de5d8",
        overview="""
        This ice cream came out delicious. It is creamy and sweet with all the real flavors of s’mores. I used Ghirardelli milk chocolate caramel squares, crushed graham crackers and toasted mini marshmallows. I really wanted to get that charred marshmallow flavor into each bite, it’s the best part. It worked!
        """,
        category="Cooking",
        favorites=0,
        views=0,
    )

    gearbox=Project(
        userId=2,
        title="Strong Worm Gearbox on 3d Printer",
        titleImage="https://content.instructables.com/ORIG/FXC/S43T/L4LBLIVL/FXCS43TL4LBLIVL.png?auto=webp&frame=1&width=397&fit=bounds&md=055d5d209eed3bc3116e3f862865518c",
        overview="""
        Strong Worm Gearbox on 3d Printer
        """,
        category="Workshop",
        favorites=0,
        views=0,
    )

    garden_tables=Project(
        userId=1,
        title="Quick and Easy Garden Tables From Old Pallets",
        titleImage="https://content.instructables.com/ORIG/F2J/BSBL/L3IQWXY3/F2JBSBLL3IQWXY3.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=94de97b15c3f680ca04bd6c5d9c8847e",
        overview="""
        I needed some side-table height tables for a garden party where guests will have buffet plates they can rest on their laps but will need a table nearby for drinks. I also wanted these tables to be (1) free; (2) usable after the event; and (3) from repurposed materials. I had been saving a couple of pallets from a delivery years ago, so I decided to work with them.
        """,
        category="Outside",
        favorites=0,
        views=0,
    )

    gummy_bears=Project(
        userId=6,
        title="Gummi Bear Science",
        titleImage="https://content.instructables.com/ORIG/FGF/2XDO/L42QW0FA/FGF2XDOL42QW0FA.jpg?auto=webp&frame=1&width=700&height=1024&fit=bounds&md=d743cfcb7f56e084029f3b76964c0c94",
        overview="""
        Welcome...to Gummi Bear Science Corner! We are going to explore osmosis by way of gummi bear growth.
        """,
        category="Teachers",
        favorites=0,
        views=0,
    )

    fortune_cookie=Project(
        userId=5,
        title="Fortune Cookie Earrings",
        titleImage="https://content.instructables.com/ORIG/FA6/7C8G/L4R1DZ02/FA67C8GL4R1DZ02.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=2d4127d1d428ec935faa3bc9f0374525",
        overview="""
        For some reason a lot of my craft projects and Instructables seem to be inspired by food. Not sure what that says about me, but I'm back with another addition to my list of food-themed projects.

        So how did these earrings come into existence? Well, one night after indulging on way too many crab rangoons, I found myself staring at an unopened fortune cookie, simultaneously scolding myself for eating too much and wondering if I had enough room for the dessert. As the food coma began to hit, my mind began to wander and my internal debate faded into oblivion as this thought crossed my mind: Fortune cookie earrings would be hella cute.

        And so, I got to work making my earrings, and the fortune cookie was left in tact (so I could save it for the photoshoot with my finished earrings).
        """,
        category="Craft",
        favorites=0,
        views=0,
    )

    planter=Project(
        userId=4,
        title="Wooden Test Tube Wall Planter",
        titleImage="https://content.instructables.com/ORIG/FW6/GD10/L34GE8TX/FW6GD10L34GE8TX.jpg?auto=webp&frame=1&width=600&fit=bounds&md=763c7994ab874f7b07f36aa21a7030ae",
        overview="""
        Indoor wall planting are very rare and organized way to provide decoration, that's why I built this Wooden Test Tube Wall Planter or you can say a plant propagation system that can carry a single tube for holding the plants.

        Many studies say that Indoor planting is a great way to decorate your home at the time it improves the air quality of your room. But a single plant won't make a difference, the bigger the leaf the better. Because, a person spends most of his time inside a room or office or like that. So, it is very much important to breath a quality air as much possible. And an indoor planting may help you achieve a circulated pure air.

        Also, wall planting can decorate your room in a different way as well it can move your space from the desk to the wall. Most of the plantings are done on tabletops or in plant pots, but wall pots are not generally seen everywhere.

        So, I've made a simple way to get some indoor plants and organize them in a very decorating way to improve you home. So, let's see the making now.
        """,
        category="Living",
        favorites=0,
        views=0,
    )

    mirror=Project(
        userId=3,
        title="Cheap, Easy, Anyone Can DIY Mirror Frame!",
        titleImage="https://content.instructables.com/ORIG/F4N/IPA4/JWESUQOL/F4NIPA4JWESUQOL.jpg?auto=webp&frame=1&width=882&height=1024&fit=bounds&md=b011042ea973f9e1eaa5793125ab303e",
        overview="""
        Ok so there are about a thousand different tutorials online for DIY mirror frames so naturally, I decided to write a quick Instructable for mine. My house had the standard builder mirrors and I wanted to jazz them up a bit without spending a fortune. I wanted to write this up mainly because this project is so simple ANYONE can make these frames with no experience, about $15, and a couple of hours. 
        """,
        category="Living",
        favorites=0,
        views=0,
    )

    airplane=Project(
        userId=2,
        title="How to Make the Reaper Paper Airplane",
        titleImage="https://content.instructables.com/ORIG/F53/CS58/J12O18NU/F53CS58J12O18NU.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=d673ef4bdd1ba9b86081c827d21faa83",
        overview="""
        Fast, long range and uniquely shaped, the Reaper is a miniature "drone cruiser" paper airplane possessing an unconventional pairing of canards and forward swept wings. The aircraft's layout is somewhat reminiscent of the radical but unbuilt Convair XB-53.

        After the success of the SkyDragonfly, I decided to develop a more advanced cruiser featuring canards. To that end, I decided to use swept wings. To address balance, the wings were swept forward to make the centers of lift and gravity workable. The shape of the canards was drawn from previous canard aircraft like the popular Fang.

        Testing showed the Reaper to be a stable and quick aircraft. Despite its unconventional shape, the aircraft proved to be very docile and accommodating. With these good handling traits and satisfactory performance, the Reaper was approved for publication.

        TAA USAF Designation: D443-1
        """,
        category="Living",
        favorites=0,
        views=0,
    )

    garden_box=Project(
        userId=1,
        title="Raised Garden Bed With an Decorative Eye Catcher",
        titleImage="https://content.instructables.com/ORIG/FAX/Y7N2/L49W2EG4/FAXY7N2L49W2EG4.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=53440dd7c343e2c5bdd1cc6988f38a9d",
        overview="""
        A raised garden bed is very practically for different reasons. Of course it is back-friendly, but also helps your plants to grow rapidly to a rich harvest.

        Putting up a raised bed in your backyard, you may want to give it a nice look as well.

        I show you how I did that.
        """,
        category="Outside",
        favorites=0,
        views=0,
    )

    rc_airplane=Project(
        userId=1,
        title="How to Make a Homemade RC Airplane Under 200$",
        titleImage="https://content.instructables.com/ORIG/FWS/XLCQ/KZ9UM0ZF/FWSXLCQKZ9UM0ZF.jpg?auto=webp&frame=1&crop=3:2&width=400&height=1024&fit=bounds&md=8f817457c4d33f0257aa005984f80de8",
        overview="""
        If you are a beginner, intermediate or a pro in RC aeromodelling, it really doesn't matter because if you love RC planes like me and enjoy flying them, then you are at your right destination. Because in today's Instrutable I will be guiding you how to make your own RC airplane which looks amazing and I will be sharing some of my own experiences and tricks that will help you to get your dream plane !

        Before we move on you may want to know these basic terminology of RC aircrafts -

        Accurate measurements
        Understanding the electronics'
        Aircraft specification
        There are more but these 3 are enough and just remember them while making and it will help you very much :)

        Also I will be sharing my design so that you can look at it for reference...
        """,
        category="Teachers",
        favorites=0,
        views=0,
    )

    db.session.add(bird_house)
    db.session.add(casino_clock)
    db.session.add(one_board_mug)
    db.session.add(skillet_burger)
    db.session.add(james_webb_clock)
    db.session.add(slowmo_birds)
    db.session.add(dragonfly)
    db.session.add(arcade_stick)
    db.session.add(minecraft_torch)
    db.session.add(giant_matches)
    db.session.add(bike_lamp)
    db.session.add(rainbow)
    db.session.add(frankenstein)
    db.session.add(ice_cream)
    db.session.add(hot_chocolate)
    db.session.add(cocoa_bombs)
    db.session.add(blossom)
    db.session.add(torus)
    db.session.add(bike_mount)
    db.session.add(data_crystals)
    db.session.add(mpcnc_controller)
    db.session.add(garage_door)
    db.session.add(poop_bag)
    db.session.add(cup_carrier)
    db.session.add(cardboard)
    db.session.add(zentrierwinkel)
    db.session.add(smores)
    db.session.add(gearbox)
    db.session.add(garden_tables)
    db.session.add(gummy_bears)
    db.session.add(fortune_cookie)
    db.session.add(planter)
    db.session.add(mirror)
    db.session.add(airplane)
    db.session.add(garden_box)
    db.session.add(rc_airplane)

    db.session.commit()

def undo_projects():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.projects RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM projects")
    db.session.execute("SELECT setval(pg_get_serial_sequence('projects', 'id'), 1, false);")

    db.session.commit()

