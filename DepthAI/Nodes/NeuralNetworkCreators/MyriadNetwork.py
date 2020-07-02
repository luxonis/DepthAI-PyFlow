from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper

from DepthAI.pins.NeuralNetworkPin import NeuralNetwork


class MyriadNetwork(NodeBase):
    def __init__(self, name):
        super(MyriadNetwork, self).__init__(name)
        self.model = self.createOutputPin('model', 'NeuralNetworkPin')
        self.model.enableOptions(PinOptions.AllowMultipleConnections)
        self.blob_path = self.createInputPin('blob_path', 'StringPin')
        self.config_path = self.createInputPin('config_path', 'StringPin')

    @staticmethod
    def pinTypeHints():
        helper = NodePinsSuggestionsHelper()
        helper.addInputDataType('StringPin')
        helper.addOutputDataType('NeuralNetworkPin')
        helper.addOutputStruct(StructureType.Multi)
        return helper

    @staticmethod
    def category():
        return "Neural Network Creators"

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return "Description in rst format."

    def compute(self, *args, **kwargs):
        self.model.setData(NeuralNetwork())
