from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper


class FramePreviewNode(NodeBase):
    def __init__(self, name):
        super(FramePreviewNode, self).__init__(name)
        self.frame = self.createInputPin('frame', 'FramePin')
        self.bbox = self.createInputPin('bbox', 'BoundingBoxPin')
        self.label = self.createInputPin('label', 'StringPin')
        self.frame.enableOptions(PinOptions.AllowMultipleConnections)

    @staticmethod
    def pinTypeHints():
        helper = NodePinsSuggestionsHelper()
        helper.addInputDataType('FramePin')
        helper.addInputDataType('BoundingBoxPin')
        helper.addInputDataType('StringPin')
        helper.addInputStruct(StructureType.Multi)
        return helper

    @staticmethod
    def category():
        return 'Debug'

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return "Description in rst format."

    def compute(self, *args, **kwargs):
        pass
