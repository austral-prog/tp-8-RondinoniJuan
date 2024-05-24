def get_coordinate(record):
    return (record[1])


def convert_coordinate(coordinate):
    x = coordinate[0]
    y = coordinate[1]
    return (x, y)


def create_record(azara_record, rui_record):
    x1 = azara_record[1]
    y1, y2 = rui_record[1]
    y3 = y1 + y2
    if x1 == y3:
        return (azara_record + rui_record)
    else:
        return "not a match"
