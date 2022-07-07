def writeSvg(file_name, all_layer_curve_set, color="#000000", shift=0.0, diff_str=""):
    s = ""

    s += '<?xml version="1.0" encoding="UTF-8" standalone="no"?>' + "\n"
    s += '<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">' + "\n"
    s += '<!-- Created with Vectornator (http://vectornator.io/) -->' + "\n"
    s += '<svg height="100%" stroke-miterlimit="10" style="fill-rule:nonzero;clip-rule:evenodd;stroke-linecap:round;stroke-linejoin:round;" version="1.1" viewBox="0 0 1000 1440" width="100%" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:vectornator="http://vectornator.io" xmlns:xlink="http://www.w3.org/1999/xlink">' + "\n"
    s += '<defs/>' + "\n"
    s += diff_str
    s += all_layer_curve_set.to_svg_str(color=color, shift=shift)
    s += "</svg>"
    with open(file_name, "w") as output:
        output.write(s) 
    #end with
#end