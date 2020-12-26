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

        title:                      string
        title_indentation:     integer (spaces from border to title)
        capitalize_items:           bool
        items_identation:      integer
        bullets:                   'numbers', 'alphabet' or string
        bullet_to_item_spaces:      integer (spaces from bullet [counting separator] to item)
        bullet_to_item_spaces:      integer (spaces from bullet to item)
        separator:                  char between bullet and item

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
        self.title_indentation = options['title_indentation']
        self.item_indentation = self._indentation(
            options['items_identation'])
        self.bullet_to_item_spaces = self._indentation(
            options['bullet_to_item_spaces'])

        if options['bullets'] == None:
            self.bullets = ''
        else:
            self.bullets = options['bullets']
        # separator
        if options['separator'] == None:
            self.separator = ''
        else:
            self.separator = options['separator']

        self.menu_items = []
        self._exceptions()

    @property
    def title(self):
        return self.title_text.center(self.title_indentation)

    @property
    def items(self):
        '''returns each item which its bullet and separator'''

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

    def __str__(self):
        menu = ''
        if self.title != None:
            menu += '{}{}'.format(self.title, self.title_to_items_lines)
        menu += self.items
        return menu

    def add_item(self, item):
        if self.capitalize_items:
            self.menu_items.append(item.capitalize())
        else:
            self.menu_items.append(item)

    def add_items(self, items):
        for item in items:
            if self.capitalize_items:
                self.menu_items.append(item.capitalize())
            else:
                self.menu_items.append(item)

    def _indentation(self, spaces):
        if spaces > 0:
            return ' ' * spaces
        else:
            return ''

    def _line_jump(self, jumps):
        return '\n' * jumps

    def _default_bullet_list(self, option):
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


if __name__ == '__main__':
    m = Menu(title='Title1',
             title_indentation=100,
             items_identation=1,
             title_to_items_lines=2,
             item_to_item_lines=2,
             bullet_to_item_spaces=1,
             separator=')',
             bullets='alphabet')

    m.add_items(['option 1', 'option 2', 'option 3', 'option 4', 'option 5'])
    m.add_item('option 6')
    print(m)
    input('')
