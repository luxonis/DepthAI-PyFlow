import json
from pathlib import Path

from PyFlow.Core import NodeBase
from PyFlow.Core.Common import Direction
from PyFlow.UI.Tool.Tool import ShelfTool
from Qt import QtGui
from datetime import datetime
from Qt.QtWidgets import QFileDialog
from Qt.QtWidgets import QMessageBox

from PyFlow import getRawNodeInstance
from PyFlow.Core.Common import *
from PyFlow.UI.UIInterfaces import IDataExporter
from PyFlow import getRawNodeInstance
from PyFlow.Core.version import Version
from PyFlow.Core.PyCodeCompiler import Py3CodeCompiler

temp = {"globalProperties": {"Leon OS frequency [kHz]": 600000, "pipeline_version": "test"},
        "nodes": [{"id": "5aa09e0c", "name": "XLinkIn", "properties": {"streamName": "test"}},
                  {"id": "8ff0eadc", "name": "XLinkOut", "properties": {"streamName": "test2"}}],
        "connections": [{"node1Id": "5aa09e0c", "node2Id": "8ff0eadc", "node1Output": "out", "node2Input": "in"}]}


def node_id(node: NodeBase):
    return node.uid.int >> 64


def get_node_by_uid(nodes, uid):
    for node in nodes:
        if str(node.uid) == str(uid):
            return node


def export_node(node: NodeBase, nodes):
    node_data = {
        "id": node_id(node),
        "name": node.name,
        "properties": {
            prop.name: prop.currentData()
            for prop in node.inputs.values()
            if not prop.hasConnections()
        },
    }
    connections = [
        {
            "node1Id": node_id(node),
            "node2Id": node_id(get_node_by_uid(nodes, link['rhsNodeUid'])),
            "node1Output": out.name,
            "node2Input": list(get_node_by_uid(nodes, link['rhsNodeUid']).pins)[link['outPinId']].name
        }
        for out in node.outputs.values()
        for link in out.linkedTo
    ]
    return node_data, connections


class ExportTool(ShelfTool):
    """docstring for AlignBottomTool."""

    def __init__(self):
        super(ExportTool, self).__init__()

    @staticmethod
    def toolTip():
        return "Export Pipeline Configuration as JSON"

    @staticmethod
    def getIcon():
        return QtGui.QIcon(str((Path(__file__).parent / Path('res/export.jpg')).resolve().absolute()))

    @staticmethod
    def name():
        return "ExportPipeline"

    def do(self):
        try:
            rootGraph = self.pyFlowInstance.graphManager.get().findRootGraph()
            nodes = []
            connections = []
            for node in rootGraph.getNodesList():
                node, node_connections = export_node(node, rootGraph.getNodesList())
                nodes.append(node)
                connections += node_connections

            export = json.dumps({
                "globalProperties": {"Leon OS frequency [kHz]": 600000, "pipeline_version": "test"},
                "nodes": nodes,
                "connections": connections
            })

            outFilePath, filterString = QFileDialog.getSaveFileName(filter="Pipeline config (*.json)")
            if outFilePath != "":
                with open(outFilePath, 'w') as f:
                    f.write(export)
            print("saved!")
        except Exception as e:
            QMessageBox.warning(self.pyFlowInstance, "Warning", str(e))

