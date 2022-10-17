import sys


def fields_gen():
    try:
        fields = list(map(lambda x: x.strip(','), sys.argv[1:]))

        if fields == []:
            arguments = input('Enter fields to take: ').split(',')
            fields = list(map(lambda x: x.strip(), arguments))

    except IndexError:
        arguments = input('Enter fields to take: ').split(',')
        fields = list(map(lambda x: x.strip(), arguments))

    return fields
