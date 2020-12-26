import menu
import title


##########################################
##                                      ##
##         prettytable's Menu           ##
##                                      ##
##########################################


# RESTAURANT MENU:

### Variables ###

# Simple Title
restaurant_title = ['My Restaurant']

# Title with frame
restaurant_name = 'My Restaurant'
frame = '=' * len(restaurant_name)
restaurant_title = [frame, restaurant_name, frame]

# Restaurant food
food = ('meat', 'fish', 'salad', 'pasta')


### Restaurant Menu ###
restaurant_menu = menu.Menu(
    title=restaurant_title,
    title_indentation=25,
    title_to_items_lines=2,
    item_to_item_lines=2,
    capitalize_items=True,
    items_identation=5,
    bullets='.',
    bullet_to_item_spaces=1,
    separator=None)

restaurant_menu.add_items(food)
print(restaurant_menu)

print('\n\n\n')


##########################################
##                                      ##
##         prettytable's Title          ##
##                                      ##
##########################################


# VIDEO GAME TITLE DESIGN:

### Creating title ###

game_title = title.Title(
    text='Amazing Game',
    background='-',
    border='=',
    width=5,
    height=4,
    bg_height=3,
    bg_width=2)

print(game_title)

print('\n\n\n')


### Getting title lines (in tuple) ###

game_title_lines = game_title.title_lines
print('title lines:', game_title_lines)

print('\n\n\n')


### Indenting title ###

indentation = '\t'
indented_title = ''

for line in game_title_lines:
    indented_title += indentation + line + '\n'

print(indented_title)

print('\n\n\n')


##########################################
##                                      ##
## Combining prettytable's Title & Menu ##
##                                      ##
##########################################

# MATH EXAM DESIGN:

exam_title_text = 'First Math Exam'
exam_questions = ('3x + 2 = x', '2x + 1 = x', '4x - 2 = 10x')

### Exam Title ###

exam_title = title.Title(
    text=exam_title_text,
    border=':',
    width=20,
    height=2,
    bg_height=1,
    bg_width=17)


### Exam Menu ###

exam_menu = menu.Menu(
    title=exam_title.title_lines,
    title_indentation=25,
    title_to_items_lines=4,
    item_to_item_lines=2,
    capitalize_items=False,
    items_identation=5,
    bullets='numbers',
    bullet_to_item_spaces=3,
    separator=')')

exam_menu.add_items(exam_questions)

print(exam_menu)
