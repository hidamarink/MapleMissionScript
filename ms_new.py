# -*- encoding=utf8 -*-
__author__ = "xiake"

from airtest.core.api import *

auto_setup(__file__)

while(True):
    auto_nav_pos = exists(Template(r"tpl1658156262845.png", record_pos=(-0.087, -0.125), resolution=(1280, 720)))
    if(auto_nav_pos):
        print("正在进行自动寻路")
        sleep(2)
        continue



#     mission_pos = exists(Template(r"tpl1658155662997.png", record_pos=(-0.427, -0.122), resolution=(1280, 720)))

#     if(mission_pos):
#         touch(mission_pos)
    next_pos = exists(Template(r"tpl1658155992222.png", record_pos=(0.448, 0.112), resolution=(1280, 720)))
    if(next_pos):
        touch(next_pos)
        continue
    
    accept_pos = exists(Template(r"tpl1658156074983.png", record_pos=(0.362, 0.045), resolution=(1280, 720)))
    if(accept_pos):
        touch(accept_pos)
        continue
        
    finish_pos = exists(Template(r"tpl1658156339504.png", record_pos=(0.362, 0.046), resolution=(1280, 720)))
    if(finish_pos):
        touch(finish_pos)
        continue
    
    ok_pos =  exists(Template(r"tpl1658156596398.png", record_pos=(0.366, 0.047), resolution=(1280, 720)))
    if(ok_pos):
        touch(ok_pos)
        continue
        
    award_pos = exists(Template(r"tpl1658155757756.png", record_pos=(-0.003, 0.221), resolution=(1280, 720)))
    if(award_pos):
        touch(award_pos)
        sleep(2)

    
    auto_skill_pos = exists(Template(r"tpl1658156481752.png", record_pos=(0.116, -0.009), resolution=(1280, 720)))
    if(auto_skill_pos):
        touch(auto_skill_pos)
    
    auto_equip_pos = exists(Template(r"tpl1658157013067.png", record_pos=(0.101, 0.026), resolution=(1280, 720)))
    if(auto_equip_pos):
        touch(auto_equip_pos)
    
    light_pos = exists(Template(r"tpl1658157548248.png", record_pos=(-0.001, 0.084), resolution=(1280, 720)))
    if(light_pos):
        touch(light_pos)


        
        




        