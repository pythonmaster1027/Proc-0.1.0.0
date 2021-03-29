
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DIVIDE EQUAL IF1 IF2 LKAKKO LNAMI MINUS NAME NUMBER PLUS RKAKKO STA TIMESexpr : NAME NAME EQUAL NAMEexpr : NAME NAME EQUAL NAME PLUS NAMEexpr : NAME NAME EQUAL NAME MINUS NAMEexpr : NAME NAME EQUAL NAME DIVIDE NAMEexpr : NAME NAME EQUAL NAME TIMES NAMEexpr : NAME NAME MINUS SENTexpr : NAME NAMESENT : exprexpr : NAME NAME LKAKKO NAME RKAKKO LNAMIexpr : NAME NAME IF1 NAME LNAMIexpr : NAME NAME IF2 NAME LNAMIexpr : NAME NAME EQUAL EQUAL NAME LNAMIexpr : NAME NAME LNAMIexpr : NAME LKAKKO NAME RKAKKOexpr : NUMBER'
    
_lr_action_items = {'NAME':([0,2,5,6,7,8,10,11,14,21,22,23,24,],[2,4,12,13,2,17,18,19,25,29,30,31,32,]),'NUMBER':([0,7,],[3,3,]),'$end':([1,3,4,9,13,15,16,20,27,28,29,30,31,32,33,34,],[0,-15,-7,-13,-1,-6,-8,-14,-10,-11,-2,-3,-4,-5,-12,-9,]),'LKAKKO':([2,4,],[5,8,]),'EQUAL':([4,6,],[6,14,]),'MINUS':([4,13,],[7,22,]),'IF1':([4,],[10,]),'IF2':([4,],[11,]),'LNAMI':([4,18,19,25,26,],[9,27,28,33,34,]),'RKAKKO':([12,17,],[20,26,]),'PLUS':([13,],[21,]),'DIVIDE':([13,],[23,]),'TIMES':([13,],[24,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expr':([0,7,],[1,16,]),'SENT':([7,],[15,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expr","S'",1,None,None,None),
  ('expr -> NAME NAME EQUAL NAME','expr',4,'p_mov','main.py',81),
  ('expr -> NAME NAME EQUAL NAME PLUS NAME','expr',6,'p_addandmov','main.py',92),
  ('expr -> NAME NAME EQUAL NAME MINUS NAME','expr',6,'p_subandmov','main.py',101),
  ('expr -> NAME NAME EQUAL NAME DIVIDE NAME','expr',6,'p_divandmov','main.py',109),
  ('expr -> NAME NAME EQUAL NAME TIMES NAME','expr',6,'p_timandmov','main.py',115),
  ('expr -> NAME NAME MINUS SENT','expr',4,'p_sub','main.py',121),
  ('expr -> NAME NAME','expr',2,'p_msg','main.py',128),
  ('SENT -> expr','SENT',1,'p_SENT','main.py',136),
  ('expr -> NAME NAME LKAKKO NAME RKAKKO LNAMI','expr',6,'p_define','main.py',141),
  ('expr -> NAME NAME IF1 NAME LNAMI','expr',5,'p_if','main.py',155),
  ('expr -> NAME NAME IF2 NAME LNAMI','expr',5,'p_if2','main.py',162),
  ('expr -> NAME NAME EQUAL EQUAL NAME LNAMI','expr',6,'p_if3','main.py',169),
  ('expr -> NAME NAME LNAMI','expr',3,'p_while','main.py',176),
  ('expr -> NAME LKAKKO NAME RKAKKO','expr',4,'p_call','main.py',183),
  ('expr -> NUMBER','expr',1,'p_expr2NUM','main.py',188),
]
