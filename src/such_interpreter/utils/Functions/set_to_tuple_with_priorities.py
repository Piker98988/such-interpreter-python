def ordered_set_to_tuple(original_set: set, priority_items: list):
    present_priority_items = [item for item in priority_items if item in original_set]
    priority_set = set(present_priority_items)
    remaining_items = list(original_set - priority_set)
    result = present_priority_items + remaining_items
    return tuple(result)
