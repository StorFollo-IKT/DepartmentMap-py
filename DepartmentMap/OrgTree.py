from xml.etree import ElementTree

from stamdata3.Organisation import Organisation


class OrgTree:
    root = None

    def __init__(self, file):
        tree = ElementTree.parse(file)
        self.root = tree.getroot()

    def get_root(self, key='900000'):
        org = TreeOrganisation(self.root.find('Organisations/Organisation/Id[.="%s"]/..' % key),
                               self.root)
        return org


class TreeOrganisation(Organisation):
    root = None

    def __init__(self, data, root):
        super().__init__(data)
        self.root = root

    def children(self):
        elements = self.root.findall('Organisations/Organisation/ParentId[.="%s"]/..' % self.id)
        return map(lambda element: TreeOrganisation(element, self.root), elements)
