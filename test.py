from stree import *

print "Castle", string_match("Castle.2009.S05E18.HDTV.x264-LOL.mp4", "Castle")
print " World", string_match(" Hello World", "Hello Universe")
print "Castle", string_match("Castle ", "Castle")
print "World", string_match("Hello 0 Universe", "Hello & Universe")