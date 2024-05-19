from enum import Enum
from recouse_set import all


from abc import ABC, abstractmethod

# 抽象请求单位类
class AbstractReqUnit(ABC):
    @abstractmethod
    def allocate(self):
        pass

# 具体连续分配请求单位类
class ContinuousReqUnit(AbstractReqUnit):
    def __init__(self) -> None:
        super(AbstractReqUnit, self).__init__()
        self.bandType = 0
        self.subFrameType = SubFrameType.ENUM_SUBFRAME_TYPE_DEFOUT
    def allocate(self):
        return "Allocating resources continuously for request unit."

# 具体原子分配请求单位类
class AtomicReqUnit(AbstractReqUnit):
    def __init__(self) -> None:
        super(AbstractReqUnit, self).__init__()
        self.bandType = 0
        self.subFrameType = SubFrameType.ENUM_SUBFRAME_TYPE_DEFOUT
    def allocate(self):
        return "Allocating resources atomically for request unit."