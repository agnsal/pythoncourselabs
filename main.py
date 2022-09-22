import numpy
# import dictExplorer  # from dictExplorer import *  # 1
from dictExplorer import esplora2  # 2
from dictExplorer import esplora2 as e  # 3
# from dictExplorer import esplora, esplora2

if __name__ == "__main__":
    x = {'test': 'ciao', 'y': {'z': [1, 2, 3]}}
    # dictExplorer.esplora(x)  # 1
    # esplora2(x)  # 2
    e(x)  # 3

    # Callable
    print(e, id(e))
    funzioneCallable = e
    print(funzioneCallable, id(funzioneCallable))
    funzioneCallable(x)

