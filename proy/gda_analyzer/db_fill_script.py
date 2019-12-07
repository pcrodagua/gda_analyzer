from gda.models import *
import pandas
data = pandas.read_excel('excel_file.xlsx')
numRows = data.shape[0]
for rowIndex in range(3, numRows):
    dataRow = data.iloc[rowIndex]
    rowList = dataRow.tolist()
    producto = Producto()
    setattr(producto, "nombre", rowList[1])
    setattr(producto, "grasa_saturada", rowList[10])
    setattr(producto, "otras_grasas", rowList[9] - rowList[10])
    setattr(producto, "azucar_total", rowList[7])
    setattr(producto, "sodio", rowList[45])
    setattr(producto, "energia", rowList[4])
    producto.save()
