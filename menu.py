from string import ascii_lowercase


class Menu:

    defaults = {
        'title': None,
        'title_indentation': 0,
        'title_to_items_lines': 2,
        'item_to_item_lines': 1,
        'capitalize_items': True,
        'items_identation': 0,
        'bullets': 'numbers',
        'bullet_to_item_spaces': 1,
        'separator': None}

    bullets_defaults = (
        'numbers',
        'alphabet')

    def __init__(self, **kwargs):
        '''
        ### Params ###

        title:                      [list / tuple]
        title_indentation:          spaces from border to title [integer]
        capitalize_items:           [bool]
        items_identation:           [int]
        bullets:                   'numbers', 'alphabet' or [string]
        bullet_to_item_spaces:      spaces from bullet (counting separator) to item [int] 
        bullet_to_item_spaces:      spaces from bullet to item [int]
        separator:                  between bullet and item [char]

        ### Exceptions ###

        title must be specified
        title_to_items_lines cannot be less than 1
        item_to_item_lines cannot be less than 1
        bullets &  separator length must be 1 [char]

        ### Recommendations ###

        title_indentation should not be negative
        items_identation should not be negative
        bullet_to_item_spaces should not be negative
        '''

        options = self.defaults | kwargs

        # invalid options exception
        for option in options:
            if option not in self.defaults:
                raise TypeError(f'{option} is not a valid parameter')

        # text settings
        self.title_text = options['title']
        self.bullets = options['bullets']
        self.capitalize_items = options['capitalize_items']
        # line jumps
        self.title_to_items_lines = self._line_jump(
            options['title_to_items_lines'])
        self.item_to_item_lines = self._line_jump(
            options['item_to_item_lines'])
        # spaces variables
        self.title_indentation = self._indentation(
            options['title_indentation'])
        self.item_indentation = self._indentation(
            options['items_identation'])
        self.bullet_to_item_spaces = self._indentation(
            options['bullet_to_item_spaces'])

        # check for empty bullets & separator
        if options['bullets'] == None:
            self.bullets = ''
        else:
            self.bullets = options['bullets']

        if options['separator'] == None:
            self.separator = ''
        else:
            self.separator = options['separator']

        self.menu_items = []
        self._exceptions()

    @ property
    def title(self):
        '''
        ### Indents each line of title ###

        retruns indented title [string]
        '''
        title = ''
        for line in range(len(self.title_text)):
            title += self.title_indentation + self.title_text[line]
            if line < len(self.title_text) - 1:
                title += '\n'
        return title

    @ property
    def items(self):
        '''
        Indents and add bullets & separators to each item in menu_items

        returns decorated items [string]
        '''

        # defines bullet list (if bullets in default, calls _default_bullet_list method)
        if self.bullets in self.bullets_defaults:
            bullet_list = self._default_bullet_list(self.bullets)
        else:
            bullet_list = self.bullets

        items = ''
        for i in range(len(self.menu_items)):
            items += '{0}{1}{2}{3}{4}'.format(
                self.item_indentation,
                bullet_list[i % len(self.menu_items)],
                self.separator,
                self.bullet_to_item_spaces,
                self.menu_items[i])

            # jump to next line if not in last item
            if i < (len(self.menu_items) - 1):
                items += self.item_to_item_lines
        return items

    def add_item(self, item):
        '''
        adds item to menu_items

        ### Params ###

        item:   [string]
        '''
        if self.capitalize_items:
            self.menu_items.append(item.capitalize())
        else:
            self.menu_items.append(item)

    def add_items(self, items):
        '''
        adds items to menu_items

        ### Params ###
        items:   [tuple/list]
        '''
        for item in items:
            if self.capitalize_items:
                self.menu_items.append(item.capitalize())
            else:
                self.menu_items.append(item)

    def _indentation(self, spaces):
        '''
        converts number of spaces [int] to string

        returns string with total spaces
        '''
        if spaces > 0:
            return ' ' * spaces
        else:
            return ''

    def _line_jump(self, jumps):
        '''
        converts number of jumps [int] to string

        returns string with total line jumps
        '''
        return '\n' * jumps

    def _default_bullet_list(self, option):
        '''
        returns corresponding default list of bullet

        ### Params ###
        option:     bullet in defaults bullet [string]
        '''
        if option == 'numbers':
            return [(i + 1) for i in range(len(self.menu_items))]

        elif option == 'alphabet':
            return [ascii_lowercase[i] for i in range(len(self.menu_items))]

    def _exceptions(self):
        # unespecified title
        if isinstance(self.title_text, type(None)):
            raise KeyError('title must be specified')

        # item_to_item & title_to_items_lines negative or zero
        if len(self.item_to_item_lines) < 1:
            raise ValueError('item_to_item_lines cannot be less than one')

        if len(self.title_to_items_lines) < 1:
            raise ValueError('title_to_items_lines cannot be less than one')
        # strings length exception
        if len(self.separator) > 1:
            raise ValueError('separator length cannot be grater than one')

    def __str__(self):
        menu = ''
        if self.title != None:
            menu += '{}{}'.format(self.title, self.title_to_items_lines)
        menu += self.items
        return menu
