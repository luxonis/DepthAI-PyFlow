from DepthAI.Nodes.Encodings.H264EncodingNode import H264EncodingNode
from DepthAI.Nodes.Encodings.H265EncodingNode import H265EncodingNode
from DepthAI.Nodes.FrameOps.ROICropNode import ROICropNode
from DepthAI.pins.H264FramePin import H264FramePin
from DepthAI.pins.H265FramePin import H265FramePin

PACKAGE_NAME = 'DepthAI'

from collections import OrderedDict
from PyFlow.UI.UIInterfaces import IPackage

# Class based nodes
from DepthAI.Nodes.Test.DemoNode import DemoNode
from DepthAI.Nodes.Test.MyProducer import MyProducer

from DepthAI.Nodes.Cameras.ColorCamera import ColorCamera
from DepthAI.Nodes.Cameras.MonoCamera import MonoCamera

from DepthAI.Nodes.NeuralNetworkCreators.MyriadNetwork import MyriadNetwork
from DepthAI.Nodes.NeuralNetworkCreators.CaffeNetwork import CaffeNetwork
from DepthAI.Nodes.NeuralNetworkCreators.ModelZooNetwork import ModelZooNetwork
from DepthAI.Nodes.NeuralNetworkCreators.TensorflowNetwork import TensorflowNetwork
from DepthAI.Nodes.NeuralNetworkInference.ObjectDetectionNode import ObjectDetectionNode
from DepthAI.Nodes.XLink.XLinkIn import XLinkIn
from DepthAI.Nodes.XLink.XLinkOut import XLinkOut
from DepthAI.Nodes.Global.GlobalPropertiesNode import GlobalPropertiesNode

# Pins
from DepthAI.pins.FramePin import FramePin
from DepthAI.pins.BoundingBoxPin import BoundingBoxPin
from DepthAI.pins.DetectionLabelPin import DetectionLabelPin
from DepthAI.pins.NeuralNetworkPin import NeuralNetworkPin
from DepthAI.pins.DepthVectorPin import DepthVectorPin
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
    XLinkIn, XLinkOut, GlobalPropertiesNode, ObjectDetectionNode, H264EncodingNode, H265EncodingNode, ROICropNode
]

for node in NODES_TO_ADD:
    _NODES[node.__name__] = node

PINS_TO_ADD = [
    FramePin, NeuralNetworkPin, BoundingBoxPin, DetectionLabelPin, DepthVectorPin, MSenderPin, SSenderPin, H264FramePin,
    H265FramePin
]

for pin in PINS_TO_ADD:
    _PINS[pin.__name__] = pin


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
