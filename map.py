import wx

from DepartmentMap import DepartmentMapFrameExtension, LoadingFrame, OrgTree, \
    TreeOrganisation

try:
    from path import path
except ImportError:
    path = 'Stamdata3_FSI_AL.xml'


def add_children(org_parent: TreeOrganisation, gui_parent):
    for org in org_parent.children():
        child = frame.orgTree.AppendItem(gui_parent, '%s (%s)' % (org.name, org.id))
        add_children(org, child)


app = wx.App(False)
loading_frame = LoadingFrame(None)
loading_frame.Show(True)

frame = DepartmentMapFrameExtension(None)

print('Load tree from %s' % path)
tree = OrgTree(path)
print('Tree loaded')

org_root = tree.get_root()
gui_root = frame.orgTree.AddRoot('%s (%s)' % (org_root.name, org_root.id))

print('Add children')
add_children(org_root, gui_root)
print('Children added')
frame.orgTree.Expand(gui_root)

# show the main frame
loading_frame.Hide()
frame.Show(True)
# start the applications
app.MainLoop()
