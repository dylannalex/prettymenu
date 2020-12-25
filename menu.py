from string import ascii_lowercase


class Menu:

    defaults = {
        'title': None,
        'border_to_title_spaces': 0,
        'title_to_items_lines': 2,
        'item_to_item_lines': 1,
        'capitalize_items': True,
        'border_to_item_spaces': 0,
        'bullets': 'numbers',
        'separator': None}

    def __init__(self, **kwargs):
        '''
        ### Params ###

        title:                      string
        border_to_title_spaces:     integer (spaces from border to title)
        capitalize_items:           bool
        border_to_item_spaces:      integer
        bullet:                    'numbers', 'alphabet' or string
        bullet_to_item_spaces:      integer (spaces from bullet [counting separator] to item)
        separator:                  char between bullet and item

        ### Exceptions ###

        title must be specified
        title_to_items_lines cannot be less than 1
        item_to_item_lines cannot be less than 1
        bullets &  separator length must be 1 [char]

        ### Recommendations ###

        border_to_title_spaces & border_to_item_spaces should not be negative
        '''

        options = self.defaults | kwargs

        # invalid options exception
        for option in options:
            if option not in self.defaults:
                raise TypeError(f'{option} is not a valid parameter')

        # attributes
        self.title_text = options['title']
        self.border_to_title_spaces = options['border_to_title_spaces']
        self.title_to_items_lines = options['title_to_items_lines']
        self.capitalize_items = options['capitalize_items']
        self.item_to_item_lines = options['item_to_item_lines']
        self.border_to_item_spaces = options['border_to_item_spaces']
        if options['bullets'] == None:
            self.bullets = ''
        else:
            self.bullets = options['bullets']
        if options['separator'] == None:
            self.separator = ''
        else:
            self.separator = options['separator']

        self.menu_items = {}
        self._exceptions()

    @property
    def title(self):
        return self.title_text.center(self.border_to_title_spaces)

    def display(self, print_title=True):
        '''
        Displays the menu, containing the title (if print_title == True) and the items.

        ### Params ###

        print_title:        if False title is not displayed
        '''
        # display title
        if print_title:
            print(self.title, end='\n' * self.title_to_items_lines)

        # display items
        for k, v in self.menu_items.items():
            item_start = ' ' * self.border_to_item_spaces
            if self.bullets == 'numbers':
                item_start += f'{k+1}{self.separator}'
            elif self.bullets == 'alphabet':
                item_start += f'{ascii_lowercase[k]}{self.separator}'
            else:
                item_start += f'{self.bullets}'
            print(item_start, v, end='\n' * self.item_to_item_lines)

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

    def _exceptions(self):
        # unespecified title
        if isinstance(self.title_text, type(None)):
            raise KeyError('title must be specified')

        # item_to_item & title_to_items_lines negative or zero
        if self.item_to_item_lines < 1:
            raise ValueError('item_to_item_lines cannot be less than one')

        if self.title_to_items_lines < 1:
            raise ValueError('title_to_items_lines cannot be less than one')

        # strings length exception
        if len(self.separator) > 1:
            raise ValueError('separator length cannot be grater than one')


if __name__ == '__main__':
    m = Menu(title='Title1',
             border_to_title_spaces=100,
             border_to_item_spaces=10,
             title_to_items_lines=2,
             item_to_item_lines=2,
             separator='-',
             bullets='alphabet')

    m.add_items(['option 1', 'option 2', 'option 3', 'option 4', 'option 5'])
    m.add_item('option 6')
    m.display(1)
    input('')
