from xml.etree import ElementTree

# словарь суммарной ценности для кубиков различных цветов
colors = {"red": 0, "green": 0, "blue": 0}
#  создает дерево элементов из строки, содержащей XML
root = ElementTree.fromstring(input())
value = 1


def valueCalculation(root, value):
    ''' Подсчет ценности цветов для текущего уровня. '''
    colors[root.get("color")] += value
    for child in root:
        valueCalculation(child, value+1)


valueCalculation(root, value)

# вывод ценности всех цветов
print(colors["red"], colors["green"], colors["blue"])
