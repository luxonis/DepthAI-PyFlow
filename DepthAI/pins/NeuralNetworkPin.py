import json

from PyFlow.Core import PinBase
from PyFlow.Core.Common import *


class NeuralNetwork:
    pass


class NoneEncoder(json.JSONEncoder):
    def default(self, vec3):
        return None


class NoneDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super(NoneDecoder, self).__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, vec3Dict):
        return NeuralNetwork()


class NeuralNetworkPin(PinBase):
    """doc string for ImagePin"""

    def __init__(self, name, parent, direction, **kwargs):
        super(NeuralNetworkPin, self).__init__(name, parent, direction, **kwargs)
        self.setDefaultValue(NeuralNetwork())
        self.disableOptions(PinOptions.Storable)

    @staticmethod
    def jsonEncoderClass():
        return NoneEncoder

    @staticmethod
    def jsonDecoderClass():
        return NoneDecoder

    @staticmethod
    def IsValuePin():
        return True

    @staticmethod
    def supportedDataTypes():
        return ('NeuralNetworkPin',)

    @staticmethod
    def pinDataTypeHint():
        return 'NeuralNetworkPin', NeuralNetwork()

    @staticmethod
    def color():
        return (200, 200, 50, 255)

    @staticmethod
    def internalDataStructure():
        return NeuralNetwork

    @staticmethod
    def processData(data):
        return NeuralNetworkPin.internalDataStructure()()
