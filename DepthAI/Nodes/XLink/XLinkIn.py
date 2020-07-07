from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper

from DepthAI.Pins.FramePin import Frame


class XLinkIn(NodeBase):
    def __init__(self, name):
        super(XLinkIn, self).__init__(name)
        self.streamName = self.createInputPin('streamName', 'StringPin')
        self.out = self.createOutputPin('out', 'MSenderPin')
        self.out.enableOptions(PinOptions.AllowMultipleConnections)

    @staticmethod
    def pinTypeHints():
        helper = NodePinsSuggestionsHelper()
        helper.addInputDataType('StringPin')
        helper.addInputStruct(StructureType.Single)
        helper.addOutputDataType('MSenderPin')
        helper.addOutputStruct(StructureType.Multi)
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
        self.out.setData(Frame())
