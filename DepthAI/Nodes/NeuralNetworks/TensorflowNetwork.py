from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper

from DepthAI.pins.NeuralOutputPin import NeuralOutput


class TensorflowNetwork(NodeBase):
    def __init__(self, name):
        super(TensorflowNetwork, self).__init__(name)
        self.inp = self.createInputPin('inp', 'FramePin')
        self.inp.enableOptions(PinOptions.AllowMultipleConnections)
        self.out = self.createOutputPin('out', 'NeuralOutputPin')
        self.out.enableOptions(PinOptions.AllowMultipleConnections)
        self.model_path = self.createInputPin('model_path', 'StringPin')

    @staticmethod
    def pinTypeHints():
        helper = NodePinsSuggestionsHelper()
        helper.addInputDataType('FramePin')
        helper.addOutputDataType('NeuralOutputPin')
        helper.addInputStruct(StructureType.Multi)
        helper.addOutputStruct(StructureType.Multi)
        return helper

    @staticmethod
    def category():
        return 'Neural Networks'

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return "Description in rst format."

    def compute(self, *args, **kwargs):
        _ = self.inp.getData()
        self.out.setData(NeuralOutput())
