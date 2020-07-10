from pathlib import Path

from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper

from DepthAI.Nodes.common import ExportableNode, SchemaPropertiesNode
from DepthAI.Pins.FramePin import Frame


class XLinkIn(NodeBase, ExportableNode, SchemaPropertiesNode):
    def get_properties_file(self):
        return str((Path(__file__).parent / Path('XLinkIn.properties.schema.json')).resolve().absolute())

    def __init__(self, name):
        super(XLinkIn, self).__init__(name)
        self.add_properties()
        self.out = self.createOutputPin('out', 'MSenderPin')
        self.out.enableOptions(PinOptions.AllowMultipleConnections)

    @staticmethod
    def pinTypeHints():
        helper = NodePinsSuggestionsHelper()
        helper.addInputDataType('StringPin')
        helper.addInputStruct(StructureType.Single)
        helper.addOutputDataType('MSenderPin')
        helper.addOutputStruct(StructureType.Multi)
        return helper

    @staticmethod
    def category():
        return 'XLink'

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return "Description in rst format."

    def compute(self, *args, **kwargs):
        self.out.setData(Frame())
