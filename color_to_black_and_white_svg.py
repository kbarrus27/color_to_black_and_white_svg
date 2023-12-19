#Convert a color SVG to black and white
#Change all instances of fill= in SVG to 'fill="#ffffff"'
#Doesn't work for fill: yet
#Can also be used to convert all outlines to black, although proceed with caution (in some circumstances you may need to convert them to white)

#Open file
svg_file_name = "insert_file_name_here.svg"
color_file = open(svg_file_name, "r", encoding='utf-8')
svg = ""
for line in color_file:
    svg += line
color_file.close()

#Convert all fills to white
#Split list at fills (this will give a bunch of chunks that all start with the hexidecimal color)
fill_removed_list = svg.split('fill="#')

#Get rid of the old hexidecimal code
new_list=[]
for i in range(1, len(fill_removed_list)):
    #This slice omits the first line of each chunk, which is the hexidecimal code
    new_list.append("\n".join(fill_removed_list[i].split("\n")[1:]))
new_list.insert(0, fill_removed_list[0])
#Now we have a list of chunks without fill codes
#Let's add those back in
final_svg_string = 'fill="#ffffff"\n'.join(new_list) #change this to white_fills = if also converting outlines to black

'''
#Convert all outlines to black
stroke_removed_list = white_fills.split('stroke="#')

final_svg_list = []
for i in range(1, len(stroke_removed_list)):
    final_svg_list.append("\n".join(stroke_removed_list[i].split("\n")[1:]))
final_svg_list.insert(0, stroke_removed_list[0])
final_svg_string = 'stroke="#000000"\n'.join(final_svg_list)
'''
black_and_white_file = open(svg_file_name[:-4] + "_black_and_white.svg", "a", encoding="utf-8")
black_and_white_file.write(final_svg_string)
black_and_white_file.close()
