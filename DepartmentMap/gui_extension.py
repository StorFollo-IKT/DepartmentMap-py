from DepartmentMap import DepartmentMapFrame


class DepartmentMapFrameExtension(DepartmentMapFrame):
    def expandAll(self, event):
        self.orgTree.ExpandAll()

    def collapseAll(self, event):
        self.orgTree.CollapseAll()
        self.orgTree.Expand(self.orgTree.GetRootItem())
