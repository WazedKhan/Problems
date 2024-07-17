import pytest

from HackerRank.linked_list_insert_position import LinkedList


def test_insert_item():
    linked_list = LinkedList()
    linked_list.insert("A")
    linked_list.insert("B")
    linked_list.insert("C")
    linked_list.insertNodeAtPosition("D", 2)
    result = linked_list.print_nodes()
    assert result == ["A", "B", "D", "C"]
