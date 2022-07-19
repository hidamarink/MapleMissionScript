# -*- encoding=utf8 -*-
__author__ = "Kyuu"

from airtest.core.api import *

auto_setup(__file__)

free_count = 0

while(True):
    
    auto_task_pos = exists(Template(r"tpl1658164859868.png", record_pos=(-0.169, 0.228), resolution=(1280, 720)))
    if(auto_task_pos):
        print("检测到正在执行自动任务 等待")
        sleep(2)
        free_count = 0
        continue

    
    auto_nav_pos = exists(Template(r"tpl1658156262845.png", record_pos=(-0.087, -0.125), resolution=(1280, 720)))
    if(auto_nav_pos):
        print("正在进行自动寻路")
        sleep(2)
        free_count = 0
        continue



    if(free_count >= 5):
        print("空置回数到达 %d 回 寻找新任务" %(free_count))
        mission_pos = exists(Template(r"tpl1658155662997.png", record_pos=(-0.427, -0.122), resolution=(1280, 720)))

        if(mission_pos):
            touch(mission_pos)
            print("主动点击任务")
            free_count = 0
            continue
            
    next_pos = exists(Template(r"tpl1658155992222.png", record_pos=(0.448, 0.112), resolution=(1280, 720)))
    if(next_pos):
        touch(next_pos)
        print("点击下一步")
        free_count = 0
        continue
    
    accept_pos = exists(Template(r"tpl1658156074983.png", record_pos=(0.362, 0.045), resolution=(1280, 720)))
    if(accept_pos):
        touch(accept_pos)
        print("点击接受")
        free_count = 0
        continue
        
    finish_pos = exists(Template(r"tpl1658156339504.png", record_pos=(0.362, 0.046), resolution=(1280, 720)))
    if(finish_pos):
        touch(finish_pos)
        print("点击完成")
        free_count = 0
        continue
    
    ok_pos =  exists(Template(r"tpl1658156596398.png", record_pos=(0.366, 0.047), resolution=(1280, 720)))
    if(ok_pos):
        touch(ok_pos)
        print("点击确认")
        free_count = 0
        continue
        
    award_pos = exists(Template(r"tpl1658160944184.png", record_pos=(0.004, 0.22), resolution=(1280, 720)))

    if(award_pos):
        touch(award_pos)
        print("领取奖励")
        sleep(2)

    
    auto_skill_pos = exists(Template(r"tpl1658156481752.png", record_pos=(0.116, -0.009), resolution=(1280, 720)))
    if(auto_skill_pos):
        touch(auto_skill_pos)
        free_count = 0
        print("自动加点")
        continue
    
    auto_equip_pos = exists(Template(r"tpl1658157013067.png", record_pos=(0.101, 0.026), resolution=(1280, 720)))
    if(auto_equip_pos):
        touch(auto_equip_pos)
        print("自动装备")
        free_count = 0
        continue
    
    light_pos = exists(Template(r"tpl1658217184714.png", record_pos=(-0.337, 0.041), resolution=(1280, 720)))


    if(light_pos):
        touch(light_pos)
        print("点击附近任务灯泡")
        free_count = 0
        continue
        
    maple_book_pos = exists(Template(r"tpl1658159739966.png", record_pos=(0.151, 0.077), resolution=(1280, 720)))
    if(maple_book_pos):
        touch(maple_book_pos)
        print("点击附近任务枫叶书")
        free_count = 0
        continue
    
    start_mission_pos = exists(Template(r"tpl1658211983991.png", record_pos=(-0.176, 0.166), resolution=(1280, 720)))
    finish_mission_pos = exists(Template(r"tpl1658212236510.png", record_pos=(-0.174, 0.166), resolution=(1280, 720)))
    if(finish_mission_pos):
        touch(finish_mission_pos)
        continue
    if(start_mission_pos):
        touch(start_mission_pos)
        continue
    
    
    free_count+=1
    print("空置 %d 回" %(free_count))

   
    
        
        





        