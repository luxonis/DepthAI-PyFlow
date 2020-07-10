from pathlib import Path

from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper

from DepthAI.Nodes.common import ExportableNode, SchemaPropertiesNode


class XLinkOut(NodeBase, ExportableNode, SchemaPropertiesNode):
    def get_properties_file(self):
        return str((Path(__file__).parent / Path('XLinkOut.properties.schema.json')).resolve().absolute())

    def __init__(self, name):
        super(XLinkOut, self).__init__(name)
        self.add_properties()
        self.inp = self.createInputPin('inp', 'AnyPin')
        self.inp.enableOptions(PinOptions.AllowMultipleConnections)

    @staticmethod
    def pinTypeHints():
        helper = NodePinsSuggestionsHelper()
        helper.addInputDataType('StringPin')
        helper.addInputDataType('AnyPin')
        helper.addInputStruct(StructureType.Multi)
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
        _ = self.inp.getData()
