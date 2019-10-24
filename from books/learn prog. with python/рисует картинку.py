from turtle import *

color('black', 'orange')
begin_fill()
while True:
    forward(250)
    left(165)
    if abs(pos()) < 1:
        break
end_fill()
done()