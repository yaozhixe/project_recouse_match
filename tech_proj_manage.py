###实例运行
from project_set import TestProjectSet
from recouse_set import TestResourcesSet
from algrithom_match import all
weekDayInput = {1,2, 3, 4, 5}

class TechProjectResManage():
    def __init__(self) -> None:
        pass

    def run():
        ##初始化资源
        caseSet = TestResourcesSet(weekDayInput)
        #初始化项目
        projectSet = TestProjectSet()
        #刷新项目优先级
        projectSet.RefreshAllProjectPrioQueue()
        #执行匹配 
        MatchAlg = MatchAlg(caseSet, projectSet)
        MatchAlg.run()
       #发布结果
        MatchAlg.publish()
        
if __name__=="__main__":
    rstManage = TechProjectResManage()
    rstManage.run()