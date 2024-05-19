from enum import Enum

##########资源初始化
DEFOUT_3700_FREQ_WIDTH = 200
DEFOUT_4900_FREQ_WIDTH = 60
DEFOUT_UPON_6G_FREQ_WIDTH = 400

DEFOUT_PHONE_NUM = 2
DEFOUT_CAR_NUM = 2

class SubFrameType(Enum):
    ENUM_SUBFRAME_TYPE_41_S2 = 0
    ENUM_SUBFRAME_TYPE_82_S54 = 1
    ENUM_SUBFRAME_TYPE_73_SS52 = 2
    ENUM_SUBFRAME_TYPE_DEFOUT = 3


WidthOfBandTpyeDict = {
    '3.7': DEFOUT_3700_FREQ_WIDTH,
    '4.9':DEFOUT_4900_FREQ_WIDTH,
    'upon6G':DEFOUT_UPON_6G_FREQ_WIDTH
}

class RecouseUint:
    def __init__(self) -> None:
        pass

    def CheckRsdRecCanMeetReq(req):
        return
    
    def OccupyRecouseByReq(req):
        return
    
    def FreeConflitOccupiedRecouse(req):
        return 


class DetachableResUint(RecouseUint):
    def __init__(self, name) -> None:
        super(RecouseUint, self).__init__()
        self.name = name
    
class FreqBandResUint(DetachableResUint):
    def __init__(self, bandType) -> None:
        super(DetachableResUint, self).__init__(bandType)
        self.freqBandWidth = WidthOfBandTpyeDict[bandType]
        self.usedFreqBand = 0
        self.rsvdFreqBand = []
        self.subFrameType = SubFrameType.ENUM_SUBFRAME_TYPE_DEFOUT


class AtomResUint(RecouseUint):
    def __init__(self, type, numOfType:dict) -> None:
        super(RecouseUint, self).__init__()
        self.type = type
        self.totalNum = 0
        self.usedNum = 0
        self.totalNumDict = numOfType
        self.rsvNumDict = {}
        for key in numOfType.keys():
            self.rsvNumDict[key] = 0
            self.totalNum = self.totalNum + numOfType[key]
        self.rsvdNum = self.totalNum

class ReqResourcesUnit(RecouseUint):
    def __init__(self) -> None:
        super(RecouseUint, self).__init__()
        self.bandType = 0
        self.subFrameType = SubFrameType.ENUM_SUBFRAME_TYPE_DEFOUT