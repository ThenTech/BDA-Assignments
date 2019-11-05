def does_intersect(x1,y1,w1,h1,x2,y2,w2,h2):
   return function(x1,x1+w1,x2,x2+w2,y1,y1+h1,y2,y2+h2)
def function(x1min,x1max,x2min,x2max,y1min,y1max,y2min,y2max):
   if x1max <= x2min or x2max <= x1min:
      return False
   if y1max <= y2min or y2max <= y1min:
      return False
   return True