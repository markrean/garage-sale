# -*- coding: utf-8 -*-
import sys
p=sys.argv[1]; s=open(p,encoding='utf-8').read()
def rep(old,new):
    global s
    assert s.count(old)==1,(p,old[:60],s.count(old)); s=s.replace(old,new)
rep('n:"2 יחידות Kallax"','n:"2 יחידות מדפים כוורת Kallax"')
rep('n:"2 стеллажа Kallax"','n:"2 стеллажа с ячейками Kallax"')
rep('n:"2× Kallax shelving units"','n:"2× Kallax cube shelving units"')
open(p,'w',encoding='utf-8').write(s); print("kallax name updated in", p)
