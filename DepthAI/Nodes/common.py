import json

from PyFlow.Core import NodeBase
from jsonschema import RefResolver


def node_id(node: NodeBase):
    return node.uid.int >> 64


def get_node_by_uid(nodes, uid):
    for node in nodes:
        if str(node.uid) == str(uid):
            return node


def get_pin_by_index(pins, index):
    for pin in pins:
        if pin.pinIndex == index:
            return pin


class ExportableNode:
    def export(self):
        if not isinstance(self, NodeBase):
            raise ValueError("Cannot export node if not an instance of NodeBase")

        nodes = self.getWrapper().canvasRef().graphManager.findRootGraph().getNodesList()
        node_data = {
            "id": node_id(self),
            "name": self.name,
            "properties": {
                prop.name: prop.currentData()
                for prop in self.inputs.values()
                if not prop.hasConnections()
            },
        }
        connections = [
            {
                "node1Id": node_id(self),
                "node2Id": node_id(get_node_by_uid(nodes, link['rhsNodeUid'])),
                "node1Output": out.name,
                "node2Input": get_pin_by_index(get_node_by_uid(nodes, link['rhsNodeUid']).pins, link['inPinId']).name
            }
            for out in self.outputs.values()
            for link in out.linkedTo
        ]
        return node_data, connections


class SchemaPropertiesNode:
    def get_properties_file(self):
        raise NotImplementedError()

    def add_properties(self):
        if not isinstance(self, NodeBase):
            raise ValueError("Cannot export node if not an instance of NodeBase")

        with open(self.get_properties_file(), 'r') as f:
            data = json.load(f)

        for key, value in data['properties'].items():
            if 'type' not in value:
                continue
            pin = self._resolve_pin(key, value['type'])
            if pin is None:
                continue
            if 'default' in value:
                pin.setData(value['default'])
            setattr(self, key, pin)

    def _resolve_pin(self, value_name, value_type):
        if value_type == "string":
            return self.createInputPin(value_name, 'StringPin')
        elif value_type == "number":
            return self.createInputPin(value_name, 'FloatPin')
        elif value_type == "integer":
            return self.createInputPin(value_name, 'IntPin')
        elif value_type == "boolean":
            return self.createInputPin(value_name, 'BoolPin')
        else:
            return None
