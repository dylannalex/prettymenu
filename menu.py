from string import ascii_lowercase


class Menu:

    defaults = {
        'title': 'Menu',
        'border_to_title_spaces': 0,
        'lines_between_items': 1,
        'capitalize_items': True,
        'border_to_item_spaces': 0,
        'bullets': 'numbers',
        'separator': ')'}

    def __init__(self, **kwargs):
        '''
        ### Params ###

        title:                      string
        border_to_title_spaces:     integer (spaces from border to title)
        capitalize_items:           bool
        border_to_item_spaces:      integer
        bullet:                    'numbers', 'alphabet' or char
        bullet_to_item_spaces:      integer (spaces from bullet [counting separator] to item)
        separator:                  char between bullet and item

        ### Exceptions ###

        border_to_title_spaces, lines_beween_items & border_to_item_spaces cannot be negative
        '''

        options = self.defaults | kwargs

        # invalid options exception
        for option in options:
            if option not in self.defaults:
                raise TypeError(f'{option} is not a valid parameter')

        self.title = options['title'].center(options['border_to_title_spaces'])
        self.capitalize_items = options['capitalize_items']
        self.lines_between_items = options['lines_between_items']
        self.border_to_item_spaces = options['border_to_item_spaces']
        self.bullets = options['bullets']
        self.separator = options['separator']
        self.menu_items = {}

    def add_item(self, item):
        if self.capitalize_items:
            self.menu_items[len(self.menu_items)] = item.capitalize()
        else:
            self.menu_items[len(self.menu_items)] = item

    def add_items(self, items):
        for item in items:
            if self.capitalize_items:
                self.menu_items[len(self.menu_items)] = item.capitalize()
            else:
                self.menu_items[len(self.menu_items)] = item

    def display(self, print_title=True):
        '''
        Displays the menu, containing the title (if print_title == True) and the items.

        ### Params ###

        print_title:        if False title is not displayed
        '''
        # display title
        if print_title:
            print(self.title, end='\n\n')

        # display items
        for k, v in self.menu_items.items():
            item_start = ' ' * self.border_to_item_spaces
            if self.bullets == 'numbers':
                item_start += f'{k+1}{self.separator}'
            elif self.bullets == 'alphabet':
                item_start += f'{ascii_lowercase[k]}{self.separator}'
            else:
                item_start += f'{self.bullets}'
            print(item_start, v, end='\n' * self.lines_between_items)


if __name__ == '__main__':
    m = Menu(title='Title1',
             border_to_title_spaces=100,
             border_to_item_spaces=10,
             lines_between_items=2,
             separator=')',
             bullets='alphabet')

    m.add_items(['option 1', 'option 2', 'option 3', 'option 4', 'option 5'])
    m.add_item('option 6')
    m.display(1)
    input('')
