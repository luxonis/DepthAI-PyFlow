from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper

from DepthAI.pins.NeuralNetworkPin import NeuralNetwork


class CaffeNetwork(NodeBase):
    def __init__(self, name):
        super(CaffeNetwork, self).__init__(name)
        self.model = self.createOutputPin('model', 'NeuralNetworkPin')
        self.model.enableOptions(PinOptions.AllowMultipleConnections)
        self.model_path = self.createInputPin('model_path', 'StringPin')
        self.proto_path = self.createInputPin('proto_path', 'StringPin')

    @staticmethod
    def pinTypeHints():
        helper = NodePinsSuggestionsHelper()
        helper.addInputDataType('StringPin')
        helper.addOutputDataType('NeuralNetworkPin')
        helper.addOutputStruct(StructureType.Multi)
        return helper

    @staticmethod
    def category():
        return 'Neural Network Creators'

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return "Description in rst format."

    def compute(self, *args, **kwargs):
        self.model.setData(NeuralNetwork())
