import json

from PyFlow.Core import PinBase
from PyFlow.Core.Common import *


class NeuralOutput:
    pass


class NoneEncoder(json.JSONEncoder):
    def default(self, vec3):
        return None


class NoneDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super(NoneDecoder, self).__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, vec3Dict):
        return NeuralOutput()


class NeuralOutputPin(PinBase):
    """doc string for ImagePin"""

    def __init__(self, name, parent, direction, **kwargs):
        super(NeuralOutputPin, self).__init__(name, parent, direction, **kwargs)
        self.setDefaultValue(NeuralOutput())
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
        return ('ImagePin',)

    @staticmethod
    def pinDataTypeHint():
        return 'ImagePin', NeuralOutput()

    @staticmethod
    def color():
        return (200, 200, 50, 255)

    @staticmethod
    def internalDataStructure():
        return NeuralOutput

    @staticmethod
    def processData(data):
        return NeuralOutputPin.internalDataStructure()()
