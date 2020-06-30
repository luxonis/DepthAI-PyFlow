PACKAGE_NAME = 'DepthAI'

from collections import OrderedDict
from PyFlow.UI.UIInterfaces import IPackage

# Class based nodes
from DepthAI.Nodes.Test.DemoNode import DemoNode
from DepthAI.Nodes.Test.MyProducer import MyProducer

from DepthAI.Nodes.Cameras.ColorCamera import ColorCamera
from DepthAI.Nodes.Cameras.MonoCamera import MonoCamera

from DepthAI.Nodes.NeuralNetworks.MyriadNetwork import MyriadNetwork
from DepthAI.Nodes.NeuralNetworks.CaffeNetwork import CaffeNetwork
from DepthAI.Nodes.NeuralNetworks.ModelZooNetwork import ModelZooNetwork
from DepthAI.Nodes.NeuralNetworks.TensorflowNetwork import TensorflowNetwork
from DepthAI.Nodes.XLink.XLinkIn import XLinkIn
from DepthAI.Nodes.XLink.XLinkOut import XLinkOut

# Pins
from DepthAI.pins.FramePin import FramePin
from DepthAI.pins.NeuralOutputPin import NeuralOutputPin
from DepthAI.pins.MSenderPin import MSenderPin
from DepthAI.pins.SSenderPin import SSenderPin

# Tools
from DepthAI.Tools.ExportTool import ExportTool

# Factories

_FOO_LIBS = {}
_NODES = {}
_PINS = {}
_TOOLS = OrderedDict()
_PREFS_WIDGETS = OrderedDict()
_EXPORTERS = OrderedDict()

NODES_TO_ADD = [
    DemoNode, MyProducer, ColorCamera, MonoCamera, MyriadNetwork, CaffeNetwork, ModelZooNetwork, TensorflowNetwork,
    XLinkIn, XLinkOut
]

for node in NODES_TO_ADD:
    _NODES[node.__name__] = node

_PINS[FramePin.__name__] = FramePin
_PINS[NeuralOutputPin.__name__] = NeuralOutputPin
_PINS[MSenderPin.__name__] = MSenderPin
_PINS[SSenderPin.__name__] = SSenderPin

_TOOLS[ExportTool.__name__] = ExportTool


class DepthAI(IPackage):
    def __init__(self):
        super(DepthAI, self).__init__()

    @staticmethod
    def GetExporters():
        return _EXPORTERS

    @staticmethod
    def GetFunctionLibraries():
        return _FOO_LIBS

    @staticmethod
    def GetNodeClasses():
        return _NODES

    @staticmethod
    def GetPinClasses():
        return _PINS

    @staticmethod
    def GetToolClasses():
        return _TOOLS
