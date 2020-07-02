from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper

from DepthAI.pins.DetectionLabelPin import DetectionLabel


class ImageClassificationNode(NodeBase):
    def __init__(self, name):
        super(ImageClassificationNode, self).__init__(name)
        self.frame = self.createInputPin('frame', 'FramePin')
        self.frame.enableOptions(PinOptions.AllowMultipleConnections)
        self.nnet = self.createInputPin('nnet', 'NeuralNetworkPin')
        self.threshold = self.createInputPin('threshold', 'FloatPin')
        self.label = self.createOutputPin('label', 'DetectionLabelPin')
        self.label.enableOptions(PinOptions.AllowMultipleConnections)

    @staticmethod
    def pinTypeHints():
        helper = NodePinsSuggestionsHelper()
        helper.addInputDataType('FramePin')
        helper.addInputDataType('NeuralNetworkPin')
        helper.addOutputDataType('DetectionLabelPin')
        helper.addInputStruct(StructureType.Multi)
        helper.addOutputStruct(StructureType.Multi)
        return helper

    @staticmethod
    def category():
        return 'Neural Network Inference'

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return "Description in rst format."

    def compute(self, *args, **kwargs):
        _ = self.frame.getData()
        _ = self.nnet.getData()
        _ = self.threshold.getData()
        self.label.setData(DetectionLabel())
