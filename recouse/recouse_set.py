from recouse_unit import AtomResUint
from recouse_unit import WidthOfBandTpyeDict
from recouse_unit import FreqBandResUint

#这个地方需要加个功能，申请用户少于等于4的时候，哪怕高等级手机也能拿到，只要保障总数量不变。 也需要换个地方注册 当前使用全局变量
NumOfPhoneTpyeDict = {
    'HiSilicon_Mate30': 30,
    'HiSilicon_Mate50': 20,
    'Qualcomm_xiaomi':20
}
NumOfCarTpyeDict = {
    'He': 1,
    'deng': 1,
}


class TestResourcesUnit:
    def __init__(self, timeSector):
        self.weekTimeSector = timeSector
        self.FreqResList = []
        for key in WidthOfBandTpyeDict.keys():
            self.FreqResList.append(FreqBandResUint(key))
        self.atomResdict = {
            'phone' : AtomResUint('phone', NumOfPhoneTpyeDict),
            'car': AtomResUint('car', NumOfCarTpyeDict)
        }
        return

class TestResourcesSet:
    DAY_TIME_SECTOR = ['morn', 'afternoon', 'night']
    def __init__(self, weekDay:list):
        self.weekRes = {{}}
        for dayItem in weekDay:
            for timeSector in TestResourcesSet.DAY_TIME_SECTOR:
                self.weekRes[dayItem][timeSector] = TestResourcesUnit(timeSector)