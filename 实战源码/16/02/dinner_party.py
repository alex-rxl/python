from threading import Thread
import random
import time
def get_organizers():
    '''获取组局者'''
    count = len(name_lists)
    num = random.randint(0,count-1)
    organizer = name_lists[num]
    print('组局者是：%s' % (organizer,))
    name_lists.pop(num)  # 将组局者从列表中删除

def get_participants():
    '''获取参者'''
    time.sleep(0.5) # 设置休眠时间，单位是秒
    print('参与者是:' , name_lists)

if __name__ == "__main__":
    name_lists = ['搜狐董事长张朝阳','小米CEO雷军','新美大CEO王','华为高级副总裁余承东','百度总裁张亚勤','360董事长周鸿祎',
                  '微软全球执行副总裁沈向洋','联想CEO杨元庆','红杉资本全球执行合伙人沈南鹏','宽带资本董事长田溯宁',
                  '京东CEO刘强东','爱奇艺CEO龚宇','滴滴出行CEO程维','58同城CEO姚劲波','高瓴资本张磊']
    t1 = Thread(target=get_organizers)   # 创建线程1
    t2 = Thread(target=get_participants) # 创建线程2
    t1.start() # 开启线程1
    t2.start() # 开启线程2
    t1.join()  # 等待线程1结束
    t2.join()  # 等待线程2结束