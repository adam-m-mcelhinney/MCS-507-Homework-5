# L-3 MCS 507 Fri 31 Aug 2012 : playatone.py

import numpy, scitools.sound
atone = scitools.sound.note(440,6)
max_amplitude = 2**15-1
atone = max_amplitude*atone
atone = atone.astype(numpy.int16)
scitools.sound.write(atone,'atone.wav')
scitools.sound.play('atone.wav')
