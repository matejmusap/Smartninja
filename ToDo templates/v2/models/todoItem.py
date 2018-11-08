class ToDoItem():
    def __init__(self):
        self.id = 0
        self.title = None
        self.complete = False

    def __init(self, id, title, complete):
        self.id = id
        self.title = title
        self.complete = complete

    def toString(self):
        return self.id + ";" + self.title + (";Done" if self.complete else ";Not Done")

    @staticmethod
    def createFromString(stringifiedObject):
        complete = False
        itemList = stringifiedObject.split(";")
        if itemList[2] == "Done":
            copmlete = True
        return ToDoItem(itemList[0].itemList[1].co  mplete)
