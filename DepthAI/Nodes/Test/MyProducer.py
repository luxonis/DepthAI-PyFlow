from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper

from DepthAI.pins.FramePin import Frame


class MyProducer(NodeBase):
    def __init__(self, name):
        super(MyProducer, self).__init__(name)
        self.message = self.createInputPin('message', 'StringPin')
        self.processor = self.createInputPin('processor', 'StringPin')
        self.out = self.createOutputPin('out', 'MSenderPin')
        self.out.enableOptions(PinOptions.AllowMultipleConnections)

    @staticmethod
    def pinTypeHints():
        helper = NodePinsSuggestionsHelper()
        helper.addInputDataType('StringPin')
        helper.addOutputDataType('MSenderPin')
        helper.addOutputStruct(StructureType.Multi)
        helper.addInputStruct(StructureType.Single)
        return helper

    @staticmethod
    def category():
        return 'Test'

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return "Description in rst format."

    def compute(self, *args, **kwargs):
        self.out.setData(Frame())
