import json
import colorsys
input_file = input("file here: ")
file = open(input_file, "r")
obj = json.loads(file.read())
file.close()

def convert_to_gd_hsv(red, green, blue, sChecked, vChecked):
    hsv = colorsys.rgb_to_hsv(red/float(255), green/float(255), blue/float(255))
    gd_hsv = f"{hsv[0]*360}a{hsv[1]}a{hsv[2]}"
    if sChecked:
        gd_hsv += "a1"
    else:
        gd_hsv += "a0"
    if vChecked:
        gd_hsv += "a1"
    else:
        gd_hsv += "a0"
    return gd_hsv

output_file = open("./geometrize.spwn", "w")
output_file.write("extract obj_props\n") # get the thingies so we can place objects

OBJ_ID = "1764" # circle id
z_order = 2


for shape in obj['shapes']:
    # do cool stuff idk im not a programmer
    if shape['type'] != 32: # if u are not circle GTFO rn
        continue
    hvs = convert_to_gd_hsv(shape['color'][0], shape['color'][1], shape['color'][2], True, True)
    spwn = "{OBJ_ID: " + OBJ_ID + ", X: " + str(shape['data'][0]) + ", Y: " + str(shape['data'][1]) + ", SCALING: " + str(shape['data'][2]*.25) + ", HVS: \"" + hvs + "\", HVS_ENABLED: true, Z_ORDER: " + str(z_order) + "}"
    obj = f"$.add(obj {spwn})\n"
    output_file.write(obj)
    z_order += 1

output_file.close() # bye bye :sunglasses: