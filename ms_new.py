# -*- encoding=utf8 -*-
__author__ = "Kyuu"

from airtest.core.api import *

auto_setup(__file__)

free_count = 0
check_triggle_count = 3
light_lock = False
wait_timeout = 1

auto_task_temp = Template(r"tpl1658164859868.png", record_pos=(-0.169, 0.228), resolution=(1280, 720))
auto_nav_temp = Template(r"tpl1658156262845.png", record_pos=(-0.087, -0.125), resolution=(1280, 720))
mission_temp = Template(r"tpl1658155662997.png", record_pos=(-0.427, -0.122), resolution=(1280, 720))
next_temp = Template(r"tpl1658155992222.png", record_pos=(0.448, 0.112), resolution=(1280, 720))
accept_temp = Template(r"tpl1658156074983.png", record_pos=(0.362, 0.045), resolution=(1280, 720))
finish_temp = Template(r"tpl1658156339504.png", record_pos=(0.362, 0.046), resolution=(1280, 720))
ok_temp = Template(r"tpl1658156596398.png", record_pos=(0.366, 0.047), resolution=(1280, 720))
award_temp = Template(r"tpl1658160944184.png", record_pos=(0.004, 0.22), resolution=(1280, 720))
auto_skill_temp = Template(r"tpl1658156481752.png", record_pos=(0.116, -0.009), resolution=(1280, 720))
auto_equip_temp = Template(r"tpl1658157013067.png", record_pos=(0.101, 0.026), resolution=(1280, 720))
light_temp = Template(r"tpl1658222839643.png", record_pos=(0.089, 0.075), resolution=(1280, 720))
maple_book_temp = Template(r"tpl1658159739966.png", record_pos=(0.151, 0.077), resolution=(1280, 720))
start_mission_temp = Template(r"tpl1658211983991.png", record_pos=(-0.176, 0.166), resolution=(1280, 720))
finish_mission_temp = Template(r"tpl1658212236510.png", record_pos=(-0.174, 0.166), resolution=(1280, 720))
hot_and_new_temp = Template(r"tpl1658248457448.png", record_pos=(-0.352, -0.227), resolution=(1280, 720))
map_loading_temp = Template(r"tpl1658249095159.png", record_pos=(0.333, -0.212), resolution=(1280, 720))
fuhuo_temp = Template(r"tpl1658388124543.png", record_pos=(-0.193, 0.129), resolution=(1280, 720))




while(True):
    #如果空置次数为0就重置灯泡点击事件
    if(light_lock == True and free_count == 0):
        print("重置灯泡点击锁定")
        light_lock = False
    
    #开局截图     
    screen = G.DEVICE.snapshot()
    
    auto_task_pos = auto_task_temp.match_in(screen)
    if(auto_task_pos):
        print("检测到正在执行自动任务 等待")
        sleep(wait_timeout)
        free_count = 0
        continue

    auto_nav_pos = auto_nav_temp.match_in(screen)
    if(auto_nav_pos):
        print("正在进行自动寻路")
        sleep(wait_timeout)
        free_count = 0
        continue

    map_loading_pos = map_loading_temp.match_in(screen)
    if(map_loading_pos):
        print("过图加载中。。。")
        sleep(wait_timeout)
        free_count = 0
        continue


    if(free_count >= check_triggle_count):
        #优先处理复活         
        fuhuo_pos = fuhuo_temp.match_in(screen)
        if(fuhuo_pos):
            touch(fuhuo_pos)
            print("角色挂了 点击回城")
            free_count = check_triggle_count
            sleep(wait_timeout)
            continue
            
        print("空置回数到达 %d 回 寻找新任务" %(free_count))
        mission_pos = mission_temp.match_in(screen)
        if(mission_pos):
            #直接点击第一栏任务区域
            touch([99,200])
            print("主动点击任务")
            free_count = 0
            continue

    next_pos = next_temp.match_in(screen)
    if(next_pos):
        touch(next_pos)
        print("点击下一步")
        sleep(wait_timeout)
        free_count = 0
        continue
    
    accept_pos = accept_temp.match_in(screen)
    if(accept_pos):
        touch(accept_pos)
        print("点击接受")
        free_count = 0
        sleep(wait_timeout)
        continue
        
    finish_pos = finish_temp.match_in(screen)
    if(finish_pos):
        touch(finish_pos)
        print("点击完成")
        free_count = 0
        sleep(wait_timeout)
        continue
    
    ok_pos = ok_temp.match_in(screen)
    if(ok_pos):
        touch(ok_pos)
        print("点击确认")
        free_count = 0
        sleep(wait_timeout)
        continue
        
    award_pos = award_temp.match_in(screen)

    if(award_pos):
        touch(award_pos)
        print("领取奖励")
        sleep(wait_timeout)
        continue

    
    auto_skill_pos = auto_skill_temp.match_in(screen)
    if(auto_skill_pos):
        touch(auto_skill_pos)
        free_count = 0
        print("自动加点")
        sleep(wait_timeout)
        continue
    
    auto_equip_pos = auto_equip_temp.match_in(screen)
    if(auto_equip_pos):
        touch(auto_equip_pos)
        print("自动装备")
        free_count = 0
        sleep(wait_timeout)
        continue
    
    light_pos = light_temp.match_in(screen)
    if(light_pos):
        if(light_lock):
            print("灯泡已经点过了 忽略这次点击")
        else:
            touch(light_pos)
            print("点击附近任务灯泡")
            light_lock = True
            free_count = 1
            sleep(wait_timeout)
            continue
        
    maple_book_pos = maple_book_temp.match_in(screen)
    if(maple_book_pos):
        touch(maple_book_pos)
        print("点击附近任务枫叶书")
        free_count = 0
        sleep(wait_timeout)
        continue
    
    start_mission_pos = start_mission_temp.match_in(screen)
    finish_mission_pos = finish_mission_temp.match_in(screen)
    if(finish_mission_pos):
        touch(finish_mission_pos)
        print("点击结束任务")
        sleep(wait_timeout)
        continue
        
    if(start_mission_pos):
        touch(start_mission_pos)
        print("多选任务开始")
        sleep(wait_timeout)
        continue
    
    hot_and_new_pos = hot_and_new_temp.match_in(screen)
    if(hot_and_new_pos):
        print("关闭广告 HOT & NEW")
        touch([1143,70])
        sleep(wait_timeout)
        continue
    
    free_count+=1
    print("空置 %d 回" %(free_count))

   
    
        
        





        