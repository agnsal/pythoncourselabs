'''
Dict explorer
'''
def esplora(d):
    assert(isinstance(d, dict))
    for k in d:
        if isinstance(d[k], dict):
            esplora(d[k])
        else:
            print(f"Key: {k} - Val: {d[k]}")


def esplora2(d):
    assert(isinstance(d, dict))
    for k, v in d.items():
        if isinstance(v, dict):
            esplora2(v)
        else:
            print(f"Key: {k} - Val: {v}")
