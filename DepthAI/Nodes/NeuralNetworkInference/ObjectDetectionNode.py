from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper

from DepthAI.pins.BoundingBoxPin import BoundingBox
from DepthAI.pins.DepthVectorPin import DepthVector
from DepthAI.pins.DetectionLabelPin import DetectionLabel


class ObjectDetectionNode(NodeBase):
    def __init__(self, name):
        super(ObjectDetectionNode, self).__init__(name)
        self.frame = self.createInputPin('frame', 'FramePin')
        self.frame.enableOptions(PinOptions.AllowMultipleConnections)
        self.nnet = self.createInputPin('nnet', 'NeuralNetworkPin')
        self.threshold = self.createInputPin('threshold', 'FloatPin')
        self.bbox = self.createOutputPin('bbox', 'BoundingBoxPin')
        self.bbox.enableOptions(PinOptions.AllowMultipleConnections)
        self.label = self.createOutputPin('label', 'DetectionLabelPin')
        self.label.enableOptions(PinOptions.AllowMultipleConnections)
        self.depth = self.createOutputPin('depth', 'DepthVectorPin')
        self.depth.enableOptions(PinOptions.AllowMultipleConnections)

    @staticmethod
    def pinTypeHints():
        helper = NodePinsSuggestionsHelper()
        helper.addInputDataType('FramePin')
        helper.addInputDataType('NeuralNetworkPin')
        helper.addOutputDataType('BoundingBoxPin')
        helper.addOutputDataType('DetectionLabelPin')
        helper.addOutputDataType('DepthVectorPin')
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
        self.bbox.setData(BoundingBox())
        self.label.setData(DetectionLabel())
        self.depth.setData(DepthVector())
