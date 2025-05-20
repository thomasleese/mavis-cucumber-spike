def parse_datatable(datatable):
    keys = datatable[0]
    return [dict(zip(keys, row)) for row in datatable[1:]]
