floors = 9
flats = 6
entrance = 4


def get_flat_address(flat_number):
    '''
    3.14. В жилом 9-этажном доме имеется 4 подъезда, на каждом
    этаже – 6 квартир. Определить:
    1) в каком подъезде находится квартира с заданным номером;
    2) на каком этаже этого подъезда она находится;
    3) какой по счету на этаже является эта квартира, если квар-
    тира с минимальным номером является первой на этаже.
    :param flat_number:
    :return:
    '''

    print('flat_number: ', flat_number)

    if flat_number not in range(1, 216):
        print('Flat number should be in range from 1 to 216')

    entrance_number = flat_number // (flats * floors) + 1
    print('Entrance number: ', entrance_number)

    flat_position = flat_number % (flats * floors)
    print('Flat position: ', flat_position)

    floor = flat_position // flats + 1
    print('Floor number: ', floor)

    flat = flat_position % flats
    print('Flat position:', flat)


get_flat_address(67)
get_flat_address(13)
get_flat_address(100)
get_flat_address(209)
get_flat_address(150)
get_flat_address(12)
get_flat_address(56)
get_flat_address(57)