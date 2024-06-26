from todo_app.data.item import Item


class ViewModel:
    def __init__(self, items: list[Item]):
        self._items = items
 
    @property
    def items(self):
        return self._items

    @property
    def todo_items(self):
        todo_items = []
        for item in self._items:
            if item.status == "To Do":
                todo_items.append(item)
        return todo_items
    
    @property
    def doing_items(self):
        doing_items = []
        for item in self._items:
            if item.status == "Doing":
                doing_items.append(item)
        return doing_items
    
    @property
    def done_items(self):
        done_items = []
        for item in self._items:
            if item.status == "Done":
                done_items.append(item)
        return done_items
    
