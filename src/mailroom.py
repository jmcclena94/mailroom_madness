# coding=utf-8
"""Create form email or report from donor list."""
import io

if hasattr(__builtins__, 'raw_input'): # Found on stackoverflow
      input=raw_input  # http://stackoverflow.com/questions/4960208/python-2-7-getting-user-input-and-manipulating-as-string-without-quotations


def initial_prompt():
    """Prompt user for action selection."""
    prompt = input('Please select from the following options: '
                   '\n\n  Create Report \n'
                   '  Send Thank You \n  Quit \n\n').lower()
    if prompt == 'quit' or prompt == 'q':
        quit()
    elif prompt == 'create report' or prompt == 'create':
        create_report()
    elif prompt == 'send thank you' or prompt == 'send':
        donor_list_prompt()
    else:
        print('Not a valid option.\n')
        initial_prompt()


def quit_prompt():
    """Prompt user for quit program or reinitialize program imput."""
    prompt = input('\nQuit or start again?\n').lower()
    if prompt == 'quit' or prompt == 'q':
        quit()
    elif prompt == 'start again' or prompt == 'start':
        initial_prompt()
    else:
        print('That is not a valid option.\n')
        quit_prompt()


def donor_list_prompt():
    """Prompt user for a name or to view donor list."""
    prompt = input('\nType donor name for a specific donor or "list" to see '
                   'a list of all donors. Type "quit" to quit.\n')
    if prompt == 'list' or prompt == 'List':
        name_list()
    elif prompt == 'quit' or prompt == 'q':
        initial_prompt()
    else:
        update_donations(prompt)


def name_list():
    """Return and print a list of donors."""
    donors = donor_list(read_donors(), 'list')
    print('\nList of donors:\n')
    for name in donors:
        print(name[0])
    donor_list_prompt()


def create_report():
    """Return and print ordered list of donor stats."""
    donors = donor_list(read_donors(), 'list')
    sorted_donors = sorted_list(donors)
    print('Your Donor Report:\n')
    for donor in sorted_donors:
        line = ('{0} has donated a total of ${1} in {2} donations at ${3} per '
                'donation.'.format(donor[0], donor[1], donor[2], donor[3]))
        print(line)
    quit_prompt()


def donation_prompt(person):
    """Prompt and return an integer from user."""
    value = input('How much did {0} donate?\nType q to quit\n'.format(person))
    if value == 'quit' or value == 'q':
        initial_prompt()
    else:
        try:
            int(value)
            return value
        except ValueError:
            print('Not a number')
            donation_prompt(person)


def update_donations(person):
    """Update donor values and save list execute email reply."""
    donors = donor_list(read_donors(), 'dictionary')
    value = int(donation_prompt(person))
    if person in list(donors.keys()):
        donations = donors[person]
        new_donations = calculation(donations, value)
        donors.setdefault(person, new_donations)
    else:
        donors.setdefault(person, [value, 1, value])
    val = donors[person]
    write_file(generate_text(donors))
    generate_email(person, val[0])


def generate_text(donors):
    """Return list of donors as a block of strings."""
    people = list(donors.keys())
    text_string = ''
    for donor in people:
        values = donors[donor]
        temp_string = ('{0}:{1} {2} '
                       '{3}\n'.format(donor, values[0], values[1], values[2]))
        text_string = text_string + temp_string
    return text_string


def write_file(text):
    """Write donor list text to text file."""
    newfile = io.open('src/donor_list.txt', 'w', encoding='utf-8')
    newfile.write(text)
    newfile.close()


def generate_email(person, donations):
    """Print email response for selected donor."""
    print('\nDear {0},\n Thank you for your donation of ${1}.  '
          'We appreciate your chairty.'.format(person, donations))
    quit_prompt()


def calculation(donations, value):
    """Return new donation values."""
    donations[0] = int(donations[0]) + value
    donations[1] = int(donations[1]) + 1
    donations[2] = int(donations[0]) / int(donations[1])
    return donations


def read_donors():
    """Return donor file text."""
    openfile = io.open('src/donor_list.txt', encoding='utf-8')
    readfile = openfile.readlines()
    openfile.close()
    return readfile


def donor_list(readfile, choice):
    """Return list or dictionary based on choice type."""
    if choice == 'list':
        donor_list = []
    else:
        donor_list = {}
    for donor in readfile:
        temp = donor.split(':')
        name = temp[0]
        numbers = temp[1].split()
        if choice == 'list':
            donor_list.append(tuple([name] + numbers))
        else:
            donor_list.setdefault(name, numbers)
    return donor_list


def sorted_list(lst):
    """Return sorted list of donors highest to lowest of total donation."""
    sorted_list = sorted(lst, key=lambda donor: int(donor[1]), reverse=True)
    return sorted_list


if __name__ == '__main__':
    initial_prompt()
