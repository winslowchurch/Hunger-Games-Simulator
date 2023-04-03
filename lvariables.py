# Local variables for main
import pygame, sys
pygame.init()

WIDTH = 1200
HEIGHT = 750

green_color = (115, 152, 109);
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT), pygame.RESIZABLE)

# Fonts and Text
pixelfont = pygame.font.Font('assets/Minecraft.ttf', 60)
titlefont = pygame.font.Font('assets/Minecraft.ttf', 80)
smallerpixelfont = pygame.font.Font('assets/Minecraft.ttf', 40)
hugefont = pygame.font.Font('assets/Minecraft.ttf', 170)

title_text = titlefont.render('Hunger Games Simulator', True, 'white')
start_text = pixelfont.render('Start', True, 'white')
start_text_hover = pixelfont.render('Start', True, green_color, 'white')
continue_text = pixelfont.render("Continue", True, 'white')
continue_text_hover = pixelfont.render("Continue", True, green_color, 'white')

# Sounds and Music
click_sound = pygame.mixer.Sound('assets/click.wav')
horn_of_plenty_song = pygame.mixer.Sound('assets/horn_of_plenty.wav')
victory_sound = pygame.mixer.Sound('assets/victory.wav')

# Images
title_image = pygame.image.load('assets/title_background.jpg')
title_image = pygame.transform.scale(title_image, (WIDTH, HEIGHT))
add_names_image = pygame.image.load('assets/names_background.jpg')
add_names_image = pygame.transform.scale(add_names_image, (WIDTH, HEIGHT))
winner_image = pygame.image.load('assets/winner.jpg')
winner_image = pygame.transform.scale(winner_image, (WIDTH, HEIGHT))

background1_image = pygame.image.load('assets/background1.jpg')
background1_image = pygame.transform.scale(background1_image, (WIDTH, HEIGHT))
background2_image = pygame.image.load('assets/background2.jpg')
background2_image = pygame.transform.scale(background2_image, (WIDTH, HEIGHT))
background3_image = pygame.image.load('assets/background3.jpg')
background3_image = pygame.transform.scale(background3_image, (WIDTH, HEIGHT))
background4_image = pygame.image.load('assets/background4.jpg')
background4_image = pygame.transform.scale(background4_image, (WIDTH, HEIGHT))
background5_image = pygame.image.load('assets/background5.jpg')
background5_image = pygame.transform.scale(background5_image, (WIDTH, HEIGHT))
background6_image = pygame.image.load('assets/background6.jpg')
background6_image = pygame.transform.scale(background6_image, (WIDTH, HEIGHT))
background7_image = pygame.image.load('assets/background7.jpg')
background7_image = pygame.transform.scale(background7_image, (WIDTH, HEIGHT))
background8_image = pygame.image.load('assets/background8.jpg')
background8_image = pygame.transform.scale(background8_image, (WIDTH, HEIGHT))
background9_image = pygame.image.load('assets/background9.jpg')
background9_image = pygame.transform.scale(background9_image, (WIDTH, HEIGHT))
background10_image = pygame.image.load('assets/background10.jpg')
background10_image = pygame.transform.scale(background10_image, (WIDTH, HEIGHT))
background11_image = pygame.image.load('assets/background11.jpg')
background11_image = pygame.transform.scale(background11_image, (WIDTH, HEIGHT))
background12_image = pygame.image.load('assets/background12.jpg')
background12_image = pygame.transform.scale(background12_image, (WIDTH, HEIGHT))
background13_image = pygame.image.load('assets/background13.jpg')
background13_image = pygame.transform.scale(background13_image, (WIDTH, HEIGHT))
background14_image = pygame.image.load('assets/background14.jpg')
background14_image = pygame.transform.scale(background14_image, (WIDTH, HEIGHT))

background_images = [background1_image, background2_image, background3_image, background4_image, background5_image, background6_image,
                     background7_image, background8_image, background9_image, background10_image, background11_image, background12_image,
                     background13_image, background14_image]

#tributes = []
tributes = ["Maddie","Winslow","Zeena","Kylee","Jerry","Max","Nick","Avi","Ellie","Jackie","Megan","Justin",
            "Serena","Jack","Hudson","Addison","Graydon","Sam","Katniss","Gooter","Peeta","Michela","Kat","Amanda"]

alive_events1 = ["has a panic attack", "catches and eats a rabbit", "runs away from the cornucopia", "heads for the woods", "panics and runs away",
                 "acquires a knife", "gets a sword from the cornucopia", "gets a backpack", "runs into a tree branch", "tackles another tribute for supplies",
                 "survives a fistfight with", "escapes a knife fight with", "tries to find a water source", "heads for highground", "tries to seduce the careers",
                 "hides in a bush", "camaflouges in the trees", "finds a cave", "eats a squirrel", "starts a fire", "wishes they didn't volunteer",
                 "camps out by the river", "sprints away from everyone", "gets an empty bag from the cornucopia", "runs away from", "wrestles over a sleeping bag with",
                 "steals a knife from", "takes food from", "doesn't get anything from the cornucopia", "sets up camp for the night", "sleeps in a tree",
                 "is already losing their mind", "makes a tent out of branches", "fights with", "survives the bloodbath", "makes it through the first day unharmed",
                 "forms an alliance with", "makes an alliance with", "is already hungry", "teams up with", "stays up all night", "tries to keep it together",
                 "rocks back and forth in fetal position"]

alive_events2 = ["picks flowers", "climbs a tree", "eats berries", "is extremely hungry", "has an existential crisis", "catches and eats a weird looking bird",
                 "gets attacked by a squirrel but survives", "runs into a tree branch", "sprains their ankle", "is starting to go insane", "is looking for water",
                 "tends to their wounds", "scrapes their knee on a rock", "sets a booby trap", "hunts for food", "gets a knife from a sponsor",
                 "gets a loaf of bread from a sponsor", "gets medicine from a sponsor", "cries themself to sleep", "is forced to eat tree bark",
                 "seriously considers suicide", "thinks about going home", "hunts for other tributes", "gets stung by a tracker jacker", "steals supplies from",
                 "hides in a bush", "tries to build a fire but fails", "frolicks in a field", "steals food from", "goes fishing", "looks for other tributes",
                 "drinks dirty water and throws up", "is surprised they made it this far", "trips and gets a concussion", "does a lil dance to try and get sponsored",
                 "is somehow still alive", "stubs their toe real bad", "makes a spear out of a stick", "falls into a pit", "survives a fight with", "steals weapons from",
                 "has sleep deprivation", "has no sponsors", "falls out of a tree but is ok", "is using up supplies quickly", "is out of supplies",
                 "accidentally uses poison oak as toilet paper", "hides in tall grass", "has to eat bugs", "survives a fight with", "escapes from", "makes a plan",
                 "drinks rainwater", "eats a rock to feel full", "is severely dehydrated", "sets traps in the forest", "scavenges for supplies", "hunts in the night",
                 "has no clue how many tributes are left", "broke their wrist falling down a hill", "tumbles down a hill but is okay", "gets caught in a trap but escapes",
                 "can't find any food", "eats eggs from a bird's nest", "gets swarmed by bees", "fights a badger over some berries", "hallucinates from lack of sleep",
                 "has no survival instincts", "took a nap", "has a fever", "is going a lil crazy", "stepped in a puddle and got their socks all wet",
                 "got wacked in the head by a sponsor parachute", "plays tic tac toe with themself in the dirt", "lost all their weapons when they fell down a hill",
                 "got distracted by their reflection in the water", "had a dream that they won", "'s shelter isn't good and they get drenched by rain",
                 "flips off the cameras", "brushes their hair with a twig", "gets a splinter"]

death_events1 = ["gets stabbed by", "immediately steps on a landmine", "gets thier throat slit by", "gets their head bashed in by", "gets speared by",
                 "gets poised darted by", "is strangled by", "gets drowned by", "bleeds out from being cut by", "gets mauled by a bear", "gets their neck snapped by",
                 "gets a knife thrown in their heart by", "eats poison by accident", "doesn't even reach the cornucopia", "gets shot with an arrow by",
                 "is beaten to death by", "gets axed by", "dies in the bloodbath", "is killed by", "is immediately murdered by", "falls out of a tree and dies",
                 "gets knifed by", "is choked to death by", "is fatally impaled by", "is burned to death by the gamemakers", "dies in quicksand", "is bludgeoned to death by",
                 "is poisoned by"]

death_events2 = ["gets stabbed by", "commits suicide", "sleepwalks right into the career pack camp", "is hunted and killed by", "gets strangled by",
                 "gets shot with an arrow by", "gets a sword to the face by", "gets their head bashed in by", "is set on fire by", "dies after being paralyzed by",
                 "gets electrocuted by", "tries to befriend a wolf. It mauls them to death", "drowns in three feet of water", "is beaten to death by",
                 "is blown up by", "is killed because the gamemakers were bored", "gets impaled by a trident by", "gets an axe to the chest by", "inhales poison fog and dies",
                 "trips over a rock and snaps their own neck", "holds the bow the wrong way and kills themself", "cries too loud and the career pack finds them",
                 "tries to set a trap but it backfires and kills them", "dies from heat exhaustion", "gets struck by lightning", "gets run over by a boulder", "gets smushed by a falling tree",
                 "is killed by the elements", "has an allergic reaction and dies", "isn't very fast at running and gets killed by"]

death_events3 = ["gets stabbed by", "commits unlife by jumping off a cliff", "is killed by tracker jackers", "gets set on fire by", "is hunted and killed by",
                 "gets pushed off a waterfall by", "is strangled by", "dies of dehydration", "gets their throat slit by", "is killed by a mutt", "eats poison berries on purpose", "gets drowned by",
                 "starves to death", "freezes to death", "gets axed by", "dies from poisonous fog", "is stabbed in the back by", "is beaten to death by", "gets their neck snapped by",
                 "gets bitten by a bunny and dies from infection", "gets a sword to the face by", "gets bitten by a poison frog and dies", "gets shot with an arrow by",
                 "is electrocuted by", "gets killed in an avalanche", "gets smushed by a rock", "gets killed by a tornado", "downs in a whirlpool", "gets struck by lightning",
                 "dies from a tree falling on them", "tries to pet a bear and dies immeditaley", "dies in quicksand", "is pushed into lava by", "is thrown into a volcano by",
                 "is bludgeoned to death by", "is poisoned by", "choked to death on food sent by a sponsor", "was burned alive in acid rain", "was electrocuted by the force field"]
