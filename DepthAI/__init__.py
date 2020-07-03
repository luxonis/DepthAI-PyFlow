PACKAGE_NAME = 'DepthAI'

from collections import OrderedDict
from PyFlow.UI.UIInterfaces import IPackage

# Class based nodes
from DepthAI.Nodes.Test.DemoNode import DemoNode
from DepthAI.Nodes.Test.MyProducer import MyProducer

from DepthAI.Nodes.Devices.BW1093 import BW1093
from DepthAI.Nodes.Devices.BW1097 import BW1097
from DepthAI.Nodes.Devices.BW1098 import BW1098

from DepthAI.Nodes.CustomNeuralNetwork.ClassificationNetworkNode import ClassificationNetworkNode
from DepthAI.Nodes.CustomNeuralNetwork.DetectorNetworkNode import DetectorNetworkNode
from DepthAI.Nodes.CustomNeuralNetwork.OCRNetworkNode import OCRNetworkNode
from DepthAI.Nodes.CustomNeuralNetwork.RawNetworkNode import RawNetworkNode
from DepthAI.Nodes.XLink.XLinkIn import XLinkIn
from DepthAI.Nodes.XLink.XLinkOut import XLinkOut
from DepthAI.Nodes.Global.GlobalPropertiesNode import GlobalPropertiesNode
from DepthAI.Nodes.Encodings.H264EncodingNode import H264EncodingNode
from DepthAI.Nodes.Encodings.H265EncodingNode import H265EncodingNode
from DepthAI.Nodes.FrameOps.ROICropNode import ROICropNode
from DepthAI.Nodes.FrameOps.DepthLocationNode import DepthLocationNode
from DepthAI.Nodes.FrameOps.ObjectTrackerNode import ObjectTrackerNode
from DepthAI.Nodes.FrameOps.DigitalZoomNode import DigitalZoomNode
from DepthAI.Nodes.FrameOps.BackgroundSubstractionNode import BackgroundSubstractionNode
from DepthAI.Nodes.ModelZoo.AgeGenderDetectionNode import AgeGenderDetectionNode
from DepthAI.Nodes.ModelZoo.EmotionsRecognitionNode import EmotionsRecognitionNode
from DepthAI.Nodes.ModelZoo.FaceDetectionAdas1Node import FaceDetectionAdas1Node
from DepthAI.Nodes.ModelZoo.FaceDetectionRetail4Node import FaceDetectionRetail4Node
from DepthAI.Nodes.ModelZoo.FacialLandmarksAdas2Node import FacialLandmarksAdas2Node
from DepthAI.Nodes.ModelZoo.FacialLandmarksRetail9Node import FacialLandmarksRetail9Node
from DepthAI.Nodes.ModelZoo.MobilenetSSDNode import MobilenetSSDNode
from DepthAI.Nodes.ModelZoo.OCRNode import OCRNode
from DepthAI.Nodes.ModelZoo.PedestrianDetectionAdas2Node import PedestrianDetectionAdas2Node
from DepthAI.Nodes.ModelZoo.PedestrianDetectionRetail13Node import PedestrianDetectionRetail13Node
from DepthAI.Nodes.ModelZoo.PersonVehicleBikeDetectionNode import PersonVehicleBikeDetectionNode
from DepthAI.Nodes.ModelZoo.VehicleDetectionAdas2Node import VehicleDetectionAdas2Node
from DepthAI.Nodes.ModelZoo.VehicleLicensePlateDetectionNode import VehicleLicensePlateDetectionNode

# Pins
from DepthAI.pins.FramePin import FramePin
from DepthAI.pins.BoundingBoxPin import BoundingBoxPin
from DepthAI.pins.DetectionLabelPin import DetectionLabelPin
from DepthAI.pins.NeuralTensorPin import NeuralTensorPin
from DepthAI.pins.DepthVectorPin import DepthVectorPin
from DepthAI.pins.MSenderPin import MSenderPin
from DepthAI.pins.SSenderPin import SSenderPin
from DepthAI.pins.H264FramePin import H264FramePin
from DepthAI.pins.H265FramePin import H265FramePin
from DepthAI.pins.TrackingInfoPin import TrackingInfoPin

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
    DemoNode, MyProducer, BW1093, BW1097, BW1098, VehicleLicensePlateDetectionNode, VehicleDetectionAdas2Node, XLinkIn,
    XLinkOut, GlobalPropertiesNode, ClassificationNetworkNode, H264EncodingNode, H265EncodingNode, ROICropNode,
    DetectorNetworkNode, DepthLocationNode, ObjectTrackerNode, DigitalZoomNode, BackgroundSubstractionNode,
    AgeGenderDetectionNode, EmotionsRecognitionNode, FaceDetectionAdas1Node, FaceDetectionRetail4Node, OCRNetworkNode,
    FacialLandmarksAdas2Node, FacialLandmarksRetail9Node, MobilenetSSDNode, OCRNode, PedestrianDetectionAdas2Node,
    PedestrianDetectionRetail13Node, PersonVehicleBikeDetectionNode, RawNetworkNode

]

for node in NODES_TO_ADD:
    _NODES[node.__name__] = node

PINS_TO_ADD = [
    FramePin, NeuralTensorPin, BoundingBoxPin, DetectionLabelPin, DepthVectorPin, MSenderPin, SSenderPin, H264FramePin,
    H265FramePin, TrackingInfoPin
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
