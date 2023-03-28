# Hunger Games Simulator
import pygame, sys, time, random
pygame.init()

WIDTH = 1200
HEIGHT = 750

# Import all local variables
from lvariables import *

# Title screen with start button
def title_screen():
    horn_of_plenty_song.set_volume(0.30)
    horn_of_plenty_song.play()
    while True:
        MOUSE_POSITION = pygame.mouse.get_pos()
        
        SCREEN.blit(title_image, (0,0))
        SCREEN.blit(title_text, (WIDTH/2 - 480, HEIGHT/2 - 100))
        pygame.display.set_caption('Hunger Games Simulator')

        s = SCREEN.blit(start_text, (WIDTH/2 - 70, HEIGHT/2 + 80))
        if s.collidepoint(MOUSE_POSITION):
            s = SCREEN.blit(start_text_hover, (WIDTH/2 - 70, HEIGHT/2 + 80))
                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            # clicked start button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if s.collidepoint(event.pos):
                    click_sound.play()
                    horn_of_plenty_song.stop()
                    add_names_screen()
        pygame.display.update()


# Allows the user to input tributes' names
add_names_text = pixelfont.render('Enter Tribute Name', True, 'white')

pygame.mixer.music.load('assets/reaping.wav')
pygame.mixer.music.set_volume(0.30)
def add_names_screen():
    global tributes
    pygame.mixer.music.play(-1)
    input_box = pygame.Rect(WIDTH/2-200, HEIGHT/2, 400, 55)
    text = ''
    tcount = 0
    
    while True:
        # background and text
        tcount_text = pixelfont.render(f'{tcount}', True, 'white')
        SCREEN.blit(add_names_image, (0,0))
        SCREEN.blit(add_names_text, (WIDTH/2-290, HEIGHT/2-100))
        SCREEN.blit(tcount_text, (WIDTH/2-270, HEIGHT/2+5))
        pygame.display.set_caption('The Reaping')

        # enough tributes to start
        if len(tributes) == 24:
            start_simulator()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                # typing name
                if event.key == pygame.K_RETURN:
                    tributes.append(text)
                    text = ''
                    tcount += 1
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
    
        txt_surface = pixelfont.render(text, True, 'white')
        input_box.w = max(400, txt_surface.get_width()+10)
        SCREEN.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(SCREEN, 'white', input_box, 2)
        
        pygame.display.update()


# Updates the event options based on the day
def update_event_options(day_num):
    global cdeath_events
    global calive_events
    if day_num == 1:
        cdeath_events = death_events1
        calive_events = alive_events1
    elif day_num >=3:
        cdeath_events = death_events3
        calive_events = alive_events2
    else:
        cdeath_events = death_events2
        calive_events = alive_events2
        

# Randomly assigns events to tributes and puts the pairing
# into current_events
def fill_current_events(tributes_copy, death_count, alive_count):
    global current_events

    cdeath_eventsc = cdeath_events.copy()
    calive_eventsc = calive_events.copy()
    for i in range(death_count):
        current_tribute = random.choice(tributes_copy)
        current_event = random.choice(cdeath_eventsc)      
        result = current_tribute + " " + current_event
        
        # includes second person
        if current_event[len(current_event)-2:] == "by":
            # find a different tribute to kill them
            second_tribute = random.choice(tributes_copy)
            while second_tribute == current_tribute:
                second_tribute = random.choice(tributes)
            
            result = result + " " + second_tribute
       
        current_events.append(result)
        tributes_copy.remove(current_tribute)
        tributes.remove(current_tribute)
        cdeath_eventsc.remove(current_event)
        
    for i in range(alive_count):
        current_tribute = random.choice(tributes_copy)
        current_event = random.choice(calive_eventsc)

        result = current_tribute + " " + current_event
        last_four_letters = current_event[len(current_event)-4:]
        if last_four_letters == "with" or last_four_letters == "from":
            second_tribute = random.choice(tributes_copy)
            if len(tributes) == 1: # edge case where there are no more tributes
                second_tribute = "a bear"
            else:
                while second_tribute == current_tribute:
                    second_tribute = random.choice(tributes)
            
            result = result + " " + second_tribute
        current_events.append(result)
        tributes_copy.remove(current_tribute)
        calive_eventsc.remove(current_event)


# show seven events at a time
def show_events_on_screen(print_events_screen):
    global are_more_events
    printed_count = 0
    cdepth = 110
    cincrement = (HEIGHT - 150) / 7
    events_left = (len(current_events) - (print_events_screen * 7))
    
    if events_left > 7:
        are_more_events = True
    else:
        are_more_events = False

    if are_more_events:
        current_batch_count = 7
    else:
        current_batch_count = events_left
        
    #for cevent in current_events:
    for i in range(current_batch_count):
        ce_index = (print_events_screen * 7) + i
        cevent = current_events[ce_index]
        ctext = smallerpixelfont.render(cevent, True, 'white')
        SCREEN.blit(ctext, (50, cdepth))
        cdepth += cincrement
        printed_count += 1       

        
cdeath_events = []
calive_events = []
current_events = []
are_more_events = True
def start_simulator():
    global tributes
    global dead_tributes
    global current_events
    
    day_num = 1
    filled_events = False
    print_events_screen = 0
    current_background_image = background1_image
    
    while True:
        MOUSE_POSITION = pygame.mouse.get_pos()

        # fill out current_events once
        if not filled_events:
            tributes_copy = tributes.copy()
            current_background_image = random.choice(background_images)
            
            update_event_options(day_num)       
            
            # randomly select number of tributes to die that day
            if day_num == 1:
                death_count = random.randint(3,9)
            elif len(tributes) == 3:
                death_count = random.randint(1,2)
            else:
                death_count = random.randint(0, len(tributes_copy)//2)
            alive_count = len(tributes_copy) - death_count
                
            fill_current_events(tributes_copy, death_count, alive_count)
            random.shuffle(current_events)
        # Done pairing tributes with events 
        filled_events = True
        
        # Background and Day number
        SCREEN.blit(current_background_image, (0,0))
        day_num_text = titlefont.render(f'Day {day_num}', True, 'white')
        SCREEN.blit(day_num_text, (10, 10))
        # Continue text with hover feature
        c = SCREEN.blit(continue_text, (WIDTH - 270, HEIGHT - 60))
        if c.collidepoint(MOUSE_POSITION):
            c = SCREEN.blit(continue_text_hover, (WIDTH - 270, HEIGHT - 60))
        pygame.display.set_caption('Hunger Games Simulator')

        # blitz the contents of current events
        show_events_on_screen(print_events_screen)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if c.collidepoint(event.pos):
                    click_sound.play()
                    # still more events for the day
                    if are_more_events:
                        print_events_screen += 1
                    else: # move onto next day
                        day_num += 1
                        current_events = [] # fresh slate
                        filled_events = False
                        print_events_screen = 0
                        
                        if len(tributes) == 1: # winner!
                            victory_sound.play()
                            winner_screen(tributes[0])
        pygame.display.update()


# The winner's name is displayed and the user has the option to play again
def winner_screen(winner):
    global tributes
    winner_ntext = hugefont.render(f'{winner} Wins!', True, 'white')
    winner_stext = hugefont.render(f'{winner} Wins!', True, green_color)
    play_again_text = pixelfont.render('Play Again', True, 'white')
    play_again_text_hover = pixelfont.render('Play Again', True, green_color, 'white')
    text_width = winner_ntext.get_width()
    
    while True:
        MOUSE_POSITION = pygame.mouse.get_pos()
        
        SCREEN.blit(winner_image, (0,0))
        SCREEN.blit(winner_stext, (WIDTH//2 - (text_width/2), HEIGHT/2 - 80))
        SCREEN.blit(winner_ntext, (WIDTH//2 - (text_width/2), HEIGHT/2 - 90))

        p = SCREEN.blit(play_again_text, (WIDTH/2 - 140, HEIGHT - 80))
        if p.collidepoint(MOUSE_POSITION):
            p = SCREEN.blit(play_again_text_hover, (WIDTH/2-140, HEIGHT - 80))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit
            # restart game
            if event.type == pygame.MOUSEBUTTONDOWN:
                if p.collidepoint(event.pos):
                    tributes = [] # reset for next play through
                    click_sound.play()
                    pygame.mixer.music.stop()
                    add_names_screen()
                
        pygame.display.update()
  
title_screen()
