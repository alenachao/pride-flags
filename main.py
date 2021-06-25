import turtle
f = turtle.Turtle() 

f.penup() 
f.goto(-175,130)

# draw a rectangle
def rectangle(w, h, color):
  f.pendown() 
  f.color(color) 
  f.begin_fill() 
  for i in range(2):
    f.forward(w)
    f.right(90) 
    f.forward(h)
    f.right(90)
  f.end_fill()
  f.penup() 
  f.sety(f.ycor() - h)

# combine rectangles into flag, input different flag h and w and a list of colors depending on which flag you want to draw
def flag(w, h, colors): 
  block_height = h // len(colors)
  for color in colors:
    rectangle(w, block_height, color) 

# standard pride flag: flag(360, 240, ["#e40303",	"#ff8c00",	"#ffed00",	"#008026",	"#004dff",	"#750787"])

# transgender flag: flag(360, 240, ["#55CDFC",	"#F7A8B8",	"#FFFFFF",	"#F7A8B8", "#55CDFC"])

# nonbinary flag: flag(360, 240, ["#FFF430",	"#FFFFFF",	"#9C59D1",	"#000000"])

# asexual flag: flag(360, 240, ["#000000",	"#A4A4A4",	"#FFFFFF",	"#810081"])

# bisexual flag: flag(360, 240, ["#D00070", "#D00070",	"#8C4799",	"#0032A0", "#0032A0"])

# pansexual flag: flag(360, 240, ["#FF1B8D",	"#FFDA00",	"#1BB3FF"])

# lesbian flag: flag(420, 280, ["#d52d00",	"#ef7627",	"#ff9a56",	"#ffffff",	"#d162a4",	"#b55690",	"#a30262"])

# gay men flag: flag(420, 280, ["#078d70", "#27ceaa",	"#98e8c1",	"#ffffff",	"#7bade2",	 "#5049cc",	"#3d1a78"])
