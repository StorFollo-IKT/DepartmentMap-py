import wx

from DepartmentMap import DepartmentMapFrameExtension, OrgTree, TreeOrganisation

try:
    from path import path
except ImportError:
    path = 'Stamdata3_FSI_AL.xml'

print('Load tree from %s' % path)
tree = OrgTree(path)
print('Tree loaded')

app = wx.App(False)

frame = DepartmentMapFrameExtension(None)
org_root = tree.get_root()
gui_root = frame.orgTree.AddRoot('%s (%s)' % (org_root.name, org_root.id))


def add_children(org_parent: TreeOrganisation, gui_parent):
    for org in org_parent.children():
        child = frame.orgTree.AppendItem(gui_parent, '%s (%s)' % (org.name, org.id))
        add_children(org, child)


print('Add children')
add_children(org_root, gui_root)
print('Children added')
frame.orgTree.Expand(gui_root)

# show the frame
frame.Show(True)
# start the applications
app.MainLoop()
