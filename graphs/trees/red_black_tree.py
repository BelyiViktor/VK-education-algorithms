class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1


class RedBlackTree:
    def __init__(self):
        # Мы делаем один лист, чтобы экономить память.
        self.NULL = Node(0)
        self.NULL.color = 0
        self.NULL.left = None
        self.NULL.right = None
        self.root = self.NULL

    def search(self, node, key):
        if node is self.NULL:
            return None
        elif node.val == key:
            return node
        elif node.val > key:
            return self.search(node.left, key)
        else:
            return self.search(node.right, key)

    def fixinsert(self, node):
        # Проверим, есть ли какие-то проблемы.
        if node.parent is None or node.parent.parent is None:
            # Мы попали в корень или его ребёнка - проблем больше нет.
            return

        grand_dad = node.parent.parent
        dad = node.parent
        if node.color == dad.color:
            # У нас проблемы - нужно их решать, ведь нельзя допустить,
            # чтобы у красной вершины был красный родитель.
            if grand_dad.val > dad.val:
                # В левом поддереве деда.
                # Можем тогда сказать, что дядя - правый потомок деда.
                uncle = grand_dad.right
                # В левом поддереве отца.
                if dad.color == uncle.color:
                    # Если дядя тоже красного цвета,
                    # необходимо просто перекрасить вершины.
                    dad.color = 0
                    uncle.color = 0
                    grand_dad.color = 1
                elif dad.val > node.val:
                    # Узел - левый ребёнок отца.
                    # Также папа и дядя разных цветов - нужен поворот.
                    self.right_rotate(dad)
                    grand_dad.color = 1
                    dad.color = 0
                    return
                else:
                    # Узел - правый ребёнок отца.
                    # Папа и дядя разных цветов - нужен двойной поворот.
                    # Поворачиваем сначала налево.
                    self.left_rotate(node)
                    dad, node = node, dad
                    # Приходим к варианту с одним поворотом направо.
                    self.right_rotate(dad)
                    grand_dad.color = 1
                    dad.color = 0
                    return
            else:
                # В правом поддереве деда.
                # Можем тогда сказать, что дядя - левый потомок деда.
                uncle = grand_dad.left
                # В левом поддереве отца.
                if dad.color == uncle.color:
                    # Если дядя тоже красного цвета,
                    # необходимо просто перекрасить вершины.
                    dad.color = 0
                    uncle.color = 0
                    grand_dad.color = 1
                elif dad.val > node.val:
                    # Узел - левый ребёнок отца.
                    # Также папа и дядя разных цветов - нужны
                    # 2 поворота и перекраска.
                    self.right_rotate(node)
                    dad, node = node, dad
                    # А также левый поворот.
                    self.left_rotate(dad)
                    grand_dad.color = 1
                    dad.color = 0
                    return
                else:
                    # Узел - правый ребёнок отца.
                    # Папа и дядя разных цветов - нужен поворот и перекраска.
                    self.left_rotate(dad)
                    grand_dad.color = 1
                    dad.color = 0
                    return
            # Мы можем создать новые проблемы.
            self.fixinsert(grand_dad)
        else:
            # У нас нет проблем, закончим их решение.
            return

    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.val = key
        node.left = self.NULL
        node.right = self.NULL
        # Новый узел всегда красный.
        node.color = 1

        new_parent_node = None
        # Указатель на узел, по которому
        # будем спускаться по дереву.
        cur = self.root

        # Ищем лист, в который нужно вставить узел.
        while cur != self.NULL:
            # Запоминаем значение, чтобы
            # оно потом стало отцом
            new_parent_node = cur
            if node.val < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        node.parent = new_parent_node
        # Если отца нет, новый узел и есть корень
        if new_parent_node is None:
            self.root = node
        # Теперь нам нужно понять, это правый потомок
        # или левый. Мы всё-таки ещё не поместили узел
        # в дерево
        elif node.val < new_parent_node.val:
            new_parent_node.left = node
        else:
            new_parent_node.right = node
        # Определим цвет - если родитель у нашего узла
        # так и не определился, значит - это корень, а
        # корень всегда чёрный. Раз корень - заканчиваем
        # вставку
        if node.parent is None:
            node.color = 0
            return
        # Нет деда - заканчиваем вставку
        if node.parent.parent is None:
            return
        # Иначе необходимо вернуть дереву свойства
        self.fixinsert(node)

    def transplant(self, replaceable, replacement):
        """Функция замены одной вершины на другую
        с заменой ссылки на родителя"""
        if replaceable.parent is None:
            self.root = replacement
        elif replaceable == replaceable.parent.left:
            replaceable.parent.left = replacement
        else:
            replaceable.parent.right = replacement
        # Не забываем поменять родителя.
        replacement.parent = replaceable.parent

    def delete_node(self, node, key):
        needle_node = self.NULL
        while node != self.NULL:
            # Ищем элемент и сохраняем
            # его в переменную needle_node.
            if node.val == key:
                needle_node = node
                break
            if node.val < key:
                node = node.right
            else:
                node = node.left
        if needle_node == self.NULL:
            print('Tree has no such key')
            return
        tmp_needle_node = needle_node
        # сохраняем отдельно цвет нашего узла
        tmp_needle_node_original_color = tmp_needle_node.color
        if needle_node.left is self.NULL:
            # Если левый потомок отсутствует, запоминаем правого
            # потомка в переменной fix_node. Именно с правым потомком
            # у нас произойдёт замена.
            fix_node = needle_node.right
            # Правый потомок нашего узла становиться на место удаляемого
            self.transplant(needle_node, needle_node.right)
        elif needle_node.right is self.NULL:
            # Правый потомок отсутствует.
            # Необходимо запомнить левого.
            fix_node = needle_node.left
            self.transplant(needle_node, needle_node.left)
        else:
            # Кейс с двумя детьми.
            tmp_needle_node = self.minimum(needle_node.right)
            # Сохраняем цвет.
            tmp_needle_node_original_color = tmp_needle_node.color
            # Запоминаем правого потомка в переменной fix_node
            fix_node = tmp_needle_node.right
            if tmp_needle_node.parent == needle_node:
                # Если удаляемый элемент родитель минимума.
                fix_node.parent = tmp_needle_node
            else:
                self.transplant(tmp_needle_node, tmp_needle_node.right)
                tmp_needle_node.right = needle_node.right
                tmp_needle_node.right.parent = tmp_needle_node

            # Меняем местами удаляемый с минимальным
            self.transplant(needle_node, tmp_needle_node)
            # Не забываем сменить указатели
            tmp_needle_node.left = needle_node.left
            tmp_needle_node.left.parent = tmp_needle_node
            tmp_needle_node.color = needle_node.color
        # Если в результате удаления меняется чёрная высота,
        # запускаем процесс балансирования.
        if tmp_needle_node_original_color == 0:
            self.fix_delete(fix_node)

    def fix_delete(self, x):
        while x != self.root and x.color == 0:
            # Если наш узел - левый ребёнок,
            # необходимо найти правого брата:
            if x == x.parent.left:
                sibling = x.parent.right
                # Если брат красный,
                if sibling.color == 1:
                    # Перекрашиваем в чёрный
                    sibling.color = 0
                    # Перекрашиваем отца в красный
                    sibling.parent.color = 1
                    # Делаем левое вращение для отца
                    self.left_rotate(x.parent)
                    # Записываем новое значение для брата
                    sibling = x.parent.right
                if sibling.left.color == 0 and sibling.right.color == 0:
                    # Если два ребёнка у брата чёрные,
                    # перекрашиваем брата в красный
                    sibling.color = 1
                    # Поднимаем наш элемент вверх
                    x = x.parent
                else:
                    if sibling.right.color == 0:
                        # Если правый ребёнок барата чёрный,
                        # перекрашиваем левого потомка брата в чёрный
                        sibling.left.color = 0
                        # Сам брат становится красным
                        sibling.color = 1
                        # Вызываем вращение вокруг брата
                        self.right_rotate(sibling)
                    sibling = x.parent.right
                    # Перекрашиваем брата в родительский цвет
                    sibling.color = x.parent.color
                    # Родителя перекрашиваем в чёрный
                    x.parent.color = 0
                    # Делаем левый поворот для родителя
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                # Симметричная ситуация
                sibling = x.parent.left
                if sibling.color == 1:
                    sibling.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    sibling = x.parent.left
                if sibling.right.color == 0 and sibling.right.color == 0:
                    sibling.color = 1
                    x = x.parent
                else:
                    if sibling.left.color == 0:
                        sibling.right.color = 0
                        sibling.color = 1
                        self.left_rotate(sibling)
                        sibling = x.parent.left
                    sibling.color = x.parent.color
                    x.parent.color = 0
                    sibling.left.color = 0
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 0

    def minimum(self, node):
        if node.left is self.NULL:
            return node
        self.minimum(node.left)

    def maximum(self, node):
        pass

    def left_rotate(self, node):
        dad = node.parent
        if dad is not self.root:
            grand_parent = node.parent.parent
            left_child = node.left
            node.left = dad
            dad.right = left_child

            if grand_parent.val > dad.val:
                grand_parent.left = node
            else:
                grand_parent.right = node
        else:
            left_child = node.left
            node.left = dad
            dad.right = left_child
            self.root = node

    def right_rotate(self, node):
        dad = node.parent
        if dad is not self.root:
            grand_parent = node.parent.parent
            right_child = node.right
            node.right = dad
            dad.left = right_child
            if grand_parent.val > dad.val:
                grand_parent.left = node
            else:
                grand_parent.right = node
        else:
            right_child = node.right
            node.right = dad
            dad.left = right_child
            self.root = node


rbt = RedBlackTree()
rbt.insert(3)
rbt.insert(2)
rbt.insert(1)
print(rbt.root.val)
rbt.delete_node(rbt.root, 1)
print(rbt.root.left.val)