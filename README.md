# Color-to-black-and-white SVG converter
I was trying to convert [this periodic table SVG](https://commons.wikimedia.org/wiki/File:Periodic_table_large.svg) to an only black-and-white version so I could laser cut it. This wasn't perfect, but it got the file to a state where I could reasonably finish it by hand.

Caveats:
- There was one instance of "fill:" instead of "fill=" that I had to fix
- I chose not to run the "convert strokes to black" code on this file because there were some elements that used colored strokes to separate the name of the element from its symbol when they would overlap (for example, Hg/Mercury). I had to go through and manually change those strokes to white after fixing the rest of the file.
