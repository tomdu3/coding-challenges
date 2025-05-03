# User creates a list of items
# Each item should include a name and a description
# Store the list in available_items.json file
# Randomly select one item from the list and display it
# Remove selected item from available_items.json file and put it in selected items.json file
import json
import time
import random
from pprint import pprint

list_items = [
    {
        'name': 'mug',
        'description': 'A very nice coffee mug I have on my desk.'
    },
    {
        'name': 'pen',
        'description': 'A very special pen I will use to sign my first contract.'
    },
    {
        'name': 'laptop',
        'description': 'My LG Gram 17 laptop. A gift from my friend Richard.'
    },
    {
        'name': 'notebook',
        'description': 'A leather-bound notebook for jotting down ideas and notes.'
    },
    {
        'name': 'desk lamp',
        'description': 'An adjustable desk lamp to brighten my workspace.'
    },
    {
        'name': 'wireless mouse',
        'description': 'A sleek wireless mouse for easier navigation.'
    },
    {
        'name': 'keyboard',
        'description': 'A mechanical keyboard with backlit keys.'
    },
    {
        'name': 'headphones',
        'description': 'Noise-canceling headphones for focused work.'
    },
    {
        'name': 'calendar',
        'description': 'A wall calendar to keep track of appointments.'
    },
    {
        'name': 'desk organizer',
        'description': 'A wooden desk organizer to keep stationery tidy.'
    },
    {
        'name': 'coffee beans',
        'description': 'A bag of premium Arabica coffee beans.'
    },
    {
        'name': 'phone charger',
        'description': 'A fast-charging cable for my smartphone.'
    },
    {
        'name': 'USB drive',
        'description': 'A 128GB USB flash drive for data storage.'
    },
    {
        'name': 'poster',
        'description': 'A motivational poster hanging on the wall.'
    },
    {
        'name': 'plant',
        'description': 'A small succulent plant to add some greenery.'
    },
    {
        'name': 'sticky notes',
        'description': 'Colorful sticky notes for reminders.'
    },
    {
        'name': 'calculator',
        'description': 'A scientific calculator for complex computations.'
    },
    {
        'name': 'bookmark',
        'description': 'A leather bookmark for my favorite book.'
    },
    {
        'name': 'clock',
        'description': 'A vintage alarm clock on my desk.'
    },
    {
        'name': 'glasses',
        'description': 'My reading glasses for close-up work.'
    }
]

def identical_lists(list1: list, list2: list):
    return sorted(list1, key=lambda x: x['name']) == sorted(list2, key=lambda x: x['name'])

def check_identical(list1, list2, file):
    if identical_lists(list1, list2):
        print(f'Original list and saved lists in "{file}" are identical.' )
    else:
        print(f'Original list and saved lists in "{file}" are different. Saved list has {len(list1) - len(list2)} less items than original.')
print('This is the list of items:')

pprint(list_items)
print()
time.sleep(1)

list_file = 'available_items.json'
selected_file = 'selected_items.json'

print('Saving the original list to a file')
time.sleep(1)

with open(list_file, 'w') as f:
    format_to_save = json.dumps(list_items, indent=4)
    f.write(format_to_save)
    print('Original list saved successfully!')

time.sleep(1)

# open the file 

file_list = None

with open(list_file, 'r') as f:
    content = f.read()
    file_list = json.loads(content)


check_identical(list_items, file_list, list_file)
print()
time.sleep(1)

random_selection = random.choice(file_list)

file_list.remove(random_selection)
print('Successfuly removed item:\n', random_selection)

time.sleep(1)
print()

with open(list_file, 'w') as f:
    content = json.dumps(file_list, indent=4)
    f.write(content)
    print(f'New "{list_file}" file created and new items list saved.')
    time.sleep(1)

with open(selected_file, 'w') as f:
    content = json.dumps(random_selection, indent=4)
    f.write(content)
    print(f'New "{selected_file}" file created and randomly selected item saved.')

time.sleep(1)
check_identical(list_items, file_list, list_file)
print()