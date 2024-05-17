from todo_app.data.item import Item
from todo_app.data.view_model import ViewModel


def test_view_model_todo_property_only_shows_item_iff_status_is_todo():
    # arrange
    items = [
        Item(1,"not started","To Do"),
        Item(2, "started", "Doing"),
        Item(3, "completed", "Done")
    ]
    
    # act
    returned_items = view_model.todo_items
    
    # assert
    assert len(returned_items) == 1

    single_item = returned_items[0]

    assert single_item.status == "To Do"

def test_view_model_doing_property_only_shows_item_iff_status_is_doing():
    # arrange
    items = [
        Item(1,"not started","To Do"),
        Item(2, "started", "Doing"),
        Item(3, "completed", "Done")
    ]
    view_model = ViewModel(items)

    # act
    returned_items = view_model.doing_items

    # assert
    assert len(returned_items) == 1

    single_item = returned_items[0]

    assert single_item.status == "Doing"

def test_view_model_done_property_only_shows_item_iff_status_is_done():
    # arrange
    items = [
        Item(1,"not started","To Do"),
        Item(2, "started", "Doing"),
        Item(3, "completed", "Done")
    ]
    view_model = ViewModel(items)

    # act
    returned_items = view_model.done_items

    # assert
    assert len(returned_items) == 1

    single_item = returned_items[0]

    assert single_item.status == "Done"
