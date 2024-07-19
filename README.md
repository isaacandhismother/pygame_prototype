# Description:
This is a prototype of a major project written in python and inspired by The Binding of Isaac and Factorio games and was about to be ported on c++ and ended up being frozen,
but you can stil see what I made in that language on my other repository named testapp. This prototype contains a lot of basic features that can be used
in the further projects.

# Features:
## 1.Menu system with bindable buttons.
This was my first experience of making a fully functional menu with bindable buttons and I think I did it well. The description provided next can also be seen in
my c++ project. Menus work here by rendering the last element of the menulsist, and buttons just add a new menu into a menulist or remove the last, pretty simple
and effective way of keeping sequence of menus opened and navigating through them. What need to be reworked though is a element editing syntax, I still can't make 
something easy and comfortable, but tried to make something similar to CSS. There is also no plane text lable placement, only menu with the background and buttons with text.

## 2. 2d tile based world system.
So basically the world is divided by two layers which are background layer and objects layer. All those layers have a 2d lists of tiles that are not rendered and updated
altogether, but only tiles, that are visible. Also this system supports object placing and destroying with object hovering that considers layers, so if flower is placed
on a higher level than a dirt tile, and a player will hover a flower to destroy it, the flower will actually be destroyed.

## 3. World generation system.
So like a file loading and saving in c++ my biggest pride is the world generation system, or to be honest, the algorythm itself. I think the world generation system should
be changed anyway but the core principle will stay there. So what is so special about it? Well maybe the fact that it uses the most misunderstood world generation concepts
in the world? For sure! My world generator uses fully functional "Perlin noise generatior" in order to create a perfect, beautiful shaped landscape. If you  look at the actual
world of my game, you would notice that its kinda sharp, and I will agree, it really needs to be smoothed. So what the Perlin noise generrator does, it creates couple 2d noise 
lists filled with numbers from -1 to 1 and what we need to do in order to conver that information to tiles, we assign a specific range to a specific block and fill the other
vector with this information. It's hard isn't it?)) So thought I and still think the same.

## 4.Json based world save-load system.
In python, I could do nothing better, but to make file saving and loading in Json format, since it's easier to read and debug, it's still not perfect, but anyway it contains not
that nuch space on disk.
