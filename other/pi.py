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

    #print('flat_number: ', flat_number)

    result = dict()

    if flat_number not in range(1, 216):
        result['error'] = 1
        result['message'] = 'Flat number should be in range from 1 to 216'

    entrance_number = flat_number // (flats * floors) + 1
    result['Entrance number'] = entrance_number

    flat_position = flat_number % (flats * floors)
    result['Flat position'] = flat_position

    floor = flat_position // flats + 1
    result['Floor number'] = floor

    flat = flat_position % flats
    result['Flat position'] = flat

    return result

