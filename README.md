# prettymenu
Python package for creating amazing ASCII titles and menus.<br/><br/>

***Classes:***<br/>
- Title
- Menu


# Menu



## Methods:

#### ***add_item:***
- **Description:** adds item to _menu_items_.<br/>
- **Parameters:** item.<br/>

#### ***add_items:***
- **Description:** adds items to _menu_items_.<br/>
- **Parameters:** items [list/tuple].<br/>

#### ***str:***
- **Description:** returns menu.<br/>

## Parameters:

#### ***title:***
- **Description:** menu's title<br/>
- **Type:** tuple/list.<br/>
- **Default value:** None.

#### ***title_indentation:***
- **Type:** int.<br/>
- **Default value:** 0.

#### ***title_to_items_lines:***
- **Description:** empty lines between title and items<br/>
- **Type:** int.<br/>
- **Default value:** 2.

#### ***item_to_item_lines:***
- **Description:** empty lines between title and items<br/>
- **Type:** int.<br/>
- **Default value:** 1.

#### ***capitalize_items:***
- **Type:** bool.<br/>
- **Default value:** True.

#### ***items_indentation:***
- **Type:** int.<br/>
- **Default value:** 0.

#### ***bullets:***
- **Description:** string at item beginning<br/>
- **Type:** string.<br/>
- **Special Values**: _numbers_ & _alphabet_.
- **Default value:** _numbers_.

#### ***bullet_to_item_spaces:***
- **Description:** distance between bullet (including the separator) and item<br/>
- **Type:** int.<br/>
- **Default value:** 1.

#### ***separator:***
- **Description:** char between bullet and item<br/>
- **Type:** char.<br/>
- **Default value:** None.



# Title


## Methods:


#### ***title_lines:***
- **Description:** returns tuple with each line of the 2D title.

#### ***str:***
- **Description:** returns title.


### Description:
Creates a personalized title.


## Parameters:

#### ***text:***
- **Description:** string displayed in title.<br/>
- **Type:** string.<br/>
- **Default value:** 'Title'.


#### ***width:***
- **Description:** frame's width.<br/>
- **Type:** int.<br/>
- **Default value:** 3.


#### ***hieght:***
- **Description:** frame's height.<br/>
- **Type:** int.<br/>
- **Default value:** 2.


#### ***border:***
- **Description:** frame's edge.<br/>
- **Type:** char.<br/>
- **Default value:** '#'.


#### ***background:***
- **Description:** space between _title_ and _border_.<br/>
- **Type:** char.<br/>
- **Default value:** _space_ (' ').


#### ***bg_width:***
- **Description:** background width.<br/>
- **Type:** int.<br/>
- **Default value:** 1.


#### ***bg_height:***
- **Description:** background height.<br/>
- **Type:** int.<br/>
- **Default value:** 0.
