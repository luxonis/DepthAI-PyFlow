from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper

from DepthAI.pins.FramePin import Frame


class XLinkOut(NodeBase):
    def __init__(self, name):
        super(XLinkOut, self).__init__(name)
        self.streamName = self.createInputPin('streamName', 'StringPin')
        self.inp = self.createInputPin('inp', 'MSenderPin')
        self.inp.enableOptions(PinOptions.AllowMultipleConnections)

    @staticmethod
    def pinTypeHints():
        helper = NodePinsSuggestionsHelper()
        helper.addInputDataType('StringPin')
        helper.addInputDataType('MSenderPin')
        helper.addInputStruct(StructureType.Multi)
        helper.addInputStruct(StructureType.Single)
        return helper

    @staticmethod
    def category():
        return 'XLink'

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return "Description in rst format."

    def compute(self, *args, **kwargs):
        _ = self.inp.getData()
