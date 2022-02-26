import clr
clr.AddReference('RevitAPI')

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

def get_selected_elements(doc):
    """API change in Revit 2016 makes old method throw an error"""
    try:
        # Revit 2016
        return [doc.GetElement(id)
                for id in __revit__.ActiveUIDocument.Selection.GetElementIds()]
    except:
        # old method
        return list(__revit__.ActiveUIDocument.Selection.Elements)

selection = get_selected_elements(doc)

sum_length = 0

for element in selection:
    try:
        length = float(element.LookupParameter('Длина').AsValueString()) / 1000
        sum_length += length
    except:
        print element.Category.Name, ' - нет параметра "Длина"'

print '- - - - - - - - - - - - - '
print sum_length
