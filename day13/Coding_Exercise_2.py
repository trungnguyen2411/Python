members = "john,lisa, teresa"


def get_nr_items(members):
    members_list = members.split(",")
    numbers_of_members_list = len(members_list)
    return numbers_of_members_list


print(get_nr_items(members))


# Solution:
def get_nr_items(user_input):
    items = user_input.split(',')
    return len(items)
