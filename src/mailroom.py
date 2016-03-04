# coding=utf-8
""" Create form email or report from donor list """
import io


def initial_prompt():
    prompt = input('Please select from the following options: '
    '\n\n  create report \n  send thank you \n  quit \n\n')
    if prompt == 'quit':
        quit()
    elif prompt == 'create report':
        create_report()
    elif prompt == 'send thank you':
        third_prompt()
    else:
        print('Not a valid option.\n')
        initial_prompt()


def second_prompt():
    prompt = input('\nquit or start again?\n')
    if prompt == 'quit':
        quit()
    elif prompt == 'start again':
        initial_prompt()
    else:
        print('That is not a valid option.\n')
        second_prompt()


def third_prompt():
    prompt = input('\nType donor name for a specific donor or "list" to see '
                   'a list of all donors.\n')
    if prompt == 'list':
        name_list()
    else:
        send_thanks(prompt)


def name_list():
    donors = donor_list(read_donors(), 'list')
    print('\nList of donors:\n')
    for name in donors:
        print(name[0])
    third_prompt()


def create_report():
    donors = donor_list(read_donors(), 'list')
    sorted_donors = sorted_list(donors)
    print('Your Donor Report:\n')
    for donor in sorted_donors:
        line = '{0} has donated a total of ${1} in {2} donations at ${3} per donation.'.format(donor[0], donor[1], donor[2], donor[3])
        print(line)
    second_prompt()


def donation_prompt(person):
    value = input('How much did {0} donate?\n'.format(person))
    try:
        int(value)
        return value
    except ValueError:
        print('Not a number')
        donation_prompt(person)


def send_thanks(person):
    donors = donor_list(read_donors(), 'dictionary')
    value = int(donation_prompt(person))
    if person in list(donors.keys()):
        donations = donors[person]
        new_donations = calculation(donations, value)
        donors.setdefault(person, new_donations)
    else:
        donors.setdefault(person, []).append(value, 1, value)
    generate_reply(person, donors(person))


def calculation(donations, value):
    donations[0] += value
    donations[1] += 1
    donations[2] = donations[0]/donations[1]
    return donations


def read_donors():
    openfile = io.open('src/donor_list.txt', encoding='utf-8')
    readfile = openfile.readlines()
    openfile.close()
    return readfile


def donor_list(readfile, choice):
    if choice == 'list':
        donor_list = []
    else:
        donor_list = {}
    for donor in readfile:
        temp = donor.split(':')
        name = temp[0]
        numbers = temp[1].split()
        if choice == 'list':
            donor_list.append((name, *numbers))
        else:
            donor_list.setdefault(name, numbers)
    return donor_list


def sorted_list(lst):
    sorted_list = sorted(lst, key=lambda donor: int(donor[1]))
    return sorted_list


if __name__ == '__main__':
    initial_prompt()
