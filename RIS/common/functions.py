#!/usr/bin/python
import prman


def drawTeapot(ri,x=0,y=0,z=0) :
  ri.TransformBegin()
  ri.Translate(x,y,z)
  ri.Rotate(45,0,1,0)
  ri.Rotate( -90, 1 ,0 ,0)
  ri.Scale( 0.2, 0.2, 0.2) 
  ri.Geometry( "teapot")
  ri.TransformEnd()  
