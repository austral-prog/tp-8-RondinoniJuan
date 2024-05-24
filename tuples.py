def get_coordinate(record):
    record = ("Scrimshawed Whale Tooth", "2A")
    return (record[1])


def convert_coordinate(coordinate):
    x = coordinate[0]
    y = coordinate[1]
    return (x, y)


def create_record(azara_record, rui_record):
    azara_record = ("Scrimshawed Whale Tooth", "2A")
    rui_record = ("Deserted Docks", "2A"  "Blue")
        if azara_record[1] == rui_record[1]:
            return (azara_record + rui_record)
        else:
            return "no coincide"
