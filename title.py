class Title:
    defaults = {
        'text': 'Title',
        'background': ' ',
        'border': '#',
        'width': 3,
        'height': 2,
        'bg_height': 0,
        'bg_width': 1}

    def __init__(self, **kwargs):
        '''
        ### Params ###

        text:               string displayed in title
        border:             char of title frame
        width:              frame's side width
        height:             frame's top and bottom lines
        bg_width:           background size from text to sides
        bg_height:          background size from text to top and bottom

        ### Exceptions ###

        must specify text
        border & background length must be 1
        width & height cannot be less than 1
        bg_width cannot be larger than width
        bg_height cannot be larger than height
        '''
        options = self.defaults | kwargs

        # invalid options exception
        for option in options:
            if option not in self.defaults:
                raise TypeError(f'{option} is not a valid parameter')

        self.text = options['text']
        self.bg = options['background']
        self.border = str(options['border'])
        self.width = options['width']
        self.height = options['height']
        self.bg_height = options['bg_height']
        self.bg_width = options['bg_width']
        self.border_len = len(self.text) + \
            (self.width + self.bg_width) * 2
        self._exceptions()

    def _exceptions(self):
        # string length exceptions
        if len(self.text) == 0:
            raise ValueError('text length must be grater than 1')
        if len(self.border) < 1 or len(self.border) > 1:
            raise ValueError('border length must be 1')

        if len(self.bg) < 1 or len(self.bg) > 1:
            raise ValueError('background length must be 1')

        # frame and background negative sizes
        if self.width < 0 or self.height < 0:
            raise ValueError('frame size cannot be negative')

        if self.bg_width < 0 or self.bg_height < 0:
            raise ValueError('backgorund size cannot be negative')

        # backgorund dimension bigger than frame dimension
        if (self.bg_width >= self.width) and self.width > 0:
            raise ValueError(
                'frame width must be grater than background width')

        if (self.bg_height >= self.height) and self.height > 0:
            raise ValueError(
                'frame height must be grater than background height')

        # background size greater than 0 when frame size == 0
        if (self.width == 0 and self.bg_width > 0) or (self.height == 0 and self.bg_height):
            raise ValueError('cannot add background while frame size is zero')

    @property
    def border_top_and_bot(self):
        result = ''
        for i in range(self.height - self.bg_height):
            result += self.border * (self.border_len - (self.bg_width * 2))
            # if not in last execution, jump to new line
            if i < (self.height - self.bg_height - 1):
                result += '\n'
        return result

    @ property
    def border_sides(self):
        return self.border * (self.width - self.bg_width)

    @ property
    def frame_center(self):
        # text
        left = '{0}{1}'.format(
            self.border_sides,
            self.bg * (self.bg_width)
        )
        right = left[::-1]

        # top and bottom of frame_center
        top = ''
        for i in range(self.bg_height):
            top += '{0}{1}{0}\n'.format(
                self.border_sides,
                self.bg * (len(self.text) + (self.bg_width * 2)))
        bot = top[::-1]

        return '{0}{1}{2}{3}{4}'.format(top, left, self.text, right, bot)

    def __str__(self):
        return '{0}\n{1}\n{0}'.format(self.border_top_and_bot, self.frame_center)
