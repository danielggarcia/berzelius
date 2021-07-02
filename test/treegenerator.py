import sys
import os

def getObjectNames(schemas_path):
    '''

    :param schemas_path:
    :return:
    '''
    objects = {}
    for filename in os.listdir(schemas_path):
        if filename.endswith(".json"):
            objects[filename[:filename.rindex(".")]] = []
            with open(os.path.join(schemas_path, filename), 'r', encoding='utf-8') as reader:
                for line in reader.readlines():
                    if "\"class\"" in line and "." in line:
                        objects[filename[:filename.rindex(".")]].append(line.split("\"")[3])
    return objects

def generateCounts(pofs):
    counts = {}
    for pof in pofs:
        apariciones = 0
        for innerPof in pofs:
            if pof in pofs[innerPof]:
                apariciones += 1
        counts[pof] = apariciones
    return counts

def generateTree(objects, counts, tree=None, currentBranch=None):
    if tree is None:
        tree = {}
        # Get root nodes
        for o in counts:
            if counts[o] == 0:
                tree[o] = {}
                tree[o] = generateTree(objects, counts, tree[o], o)
    else:
        # Generate branch
        children = objects[currentBranch]
        if len(children) > 0:
            for child in children:
                tree[child] = {}
                tree[child] = generateTree(objects, counts, tree[child], child)
    return tree


def getPaths(tree, breadCrumb = [], arrayBreadCrumbs = []):
    # Recorremos el árbol
    for key in tree:
        subtree = tree[key]
        breadCrumb.append(key)
        currentBreadCrumb = []
        for crumb in breadCrumb:
            currentBreadCrumb.append(crumb)
        arrayBreadCrumbs.append(currentBreadCrumb)
        getPaths(subtree, breadCrumb, arrayBreadCrumbs)
        breadCrumb.pop()

    return arrayBreadCrumbs

def isLastOrOnlyChild(breadCrumb, tree):
    subtree = tree
    for i in range(0, len(breadCrumb) -1):
        subtree = subtree[breadCrumb[i]]
    siblings = list(subtree.keys())
    if len(siblings) == 0:
        return True
    isOnlyChild = len(siblings) == 1
    isLastChild = siblings[-1] == breadCrumb[-1]
    return isOnlyChild or isLastChild

def drawLine(breadCrumb, tree):
    elbow = "  └─ "
    tee = "  ├─ "
    pipe = "  │  "
    space = "    "
    line = ""
    for i in range(0, len(breadCrumb)):

        # If we have reached the last element of the breadcrumb, return it
        if i == len(breadCrumb) - 1:
            # If the element is only child or last child, add an elbow
            if isLastOrOnlyChild(breadCrumb, tree):
                return line + elbow + breadCrumb[i]
            else:
                return line + tee + breadCrumb[i]
        # Intermediate nodes
        else:
            if isLastOrOnlyChild(breadCrumb[0:i+1], tree):
                line += space
            else:
                line += pipe

def generatePOFTree(schemas_path, destination_file="schema.txt"):
    if not (os.path.isdir(schemas_path) and os.path.exists(schemas_path)):
        print("No se ha encontrado la ruta de esquemas '{}'.".format(schemas_path))
        exit(3)

    objects = getObjectNames(schemas_path)
    counts = generateCounts(objects)
    tree = generateTree(objects, counts)
    paths = getPaths(tree)
    lines = ["MAIN\n"]
    for breadCrumb in paths:
        lines.append(drawLine(breadCrumb, tree) + "\n")
    with open(destination_file, 'w', encoding='utf-8') as dfile:
        dfile.writelines(lines)


if __name__ == '__main__':
    from Dict2ASCIITree import Dict2ASCIITree
    mapper = Dict2ASCIITree()
    f = mapper.__load_json__('file.json')
    tree = mapper.__json2treedict__(f)
    print(tree)
    '''
    if len(sys.argv) < 2:
        print("Sintaxis: {} <ruta de la carpeta src>")
        exit(1)

    src_path = sys.argv[1]
    if not (os.path.isdir(src_path) and os.path.exists(src_path)):
        print("La ruta '{}' no existe.".format(src_path))
        exit(2)

    schemas_path = os.path.join(src_path, "main", "resources")
    generatePOFTree(schemas_path, ".\\schema.txt")
    '''