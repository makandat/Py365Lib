#!/usr/bin/python3
from Py365Lib import SVG, Common

name = "No Name"
Common.esc_print("bold", "SVG class test")
if Common.count_args() == 0 :
  name = Common.readline("Enter test name")
else :
  name = Common.args(0)
svg = SVG.SVG(640, 480, name)
if name == "line" :
  svg.line(0, 0, 639, 479)
elif name == "circle" :
  svg.circle(320, 240, 100)
elif name == "ellipse" :
  svg.ellipse(320, 240, 180, 90)
elif name == "rect" :
  svg.stroke = "#000000"
  svg.fill = "#e0e0e0"
  svg.stroke_width =3
  svg.rectangle(240, 160, 120, 100)
elif name == "dashline":
  svg.dashline(10, 240, 630, 240, "2")
elif name == "polyline":
  svg.polyline([[20, 200], [320, 20], [620, 390], [330, 430]])
elif name == "polygon":
  svg.polygon([[100, 100], [320, 100], [620, 300], [330, 430]])
elif name == "path" :
  svg.path(["M100 100", "h 120", "v 80"])
elif name == "text" :
  svg.drawtext(200, 200, "SVG draw text.")
else :
  Common.stop("Error: bad name.")
# Show Result
print(svg.toXml())
svg.save("/home/user/temp/" + name + ".svg")

