import json
from pathlib import Path

from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
from PyFlow.UI.Tool.Tool import ShelfTool
from Qt import QtGui
from Qt.QtWidgets import QFileDialog, QMessageBox

from DepthAI.Nodes.Global.GlobalPropertiesNode import GlobalPropertiesNode


def node_id(node: NodeBase):
    return node.uid.int >> 64


def get_node_by_uid(nodes, uid):
    for node in nodes:
        if str(node.uid) == str(uid):
            return node


def get_pin_value(pins, name):
    for pin in pins:
        if pin.name == name:
            return pin.currentData()


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
        return QtGui.QIcon(str((Path(__file__).parent / Path('res/export.png')).resolve().absolute()))

    @staticmethod
    def name():
        return "ExportPipeline"

    def do(self):
        try:
            rootGraph = self.pyFlowInstance.graphManager.get().findRootGraph()
            nodes = []
            connections = []
            global_config = {}
            for node in rootGraph.getNodesList():
                if node.name == GlobalPropertiesNode.__name__:
                    global_config["pipeline_version"] = "test"
                    global_config["Leon OS frequency [kHz]"] = get_pin_value(node.inputs.values(), 'leon_os_freq')
                node, node_connections = export_node(node, rootGraph.getNodesList())
                nodes.append(node)
                connections += node_connections

            export = json.dumps({
                "globalProperties": global_config,
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

