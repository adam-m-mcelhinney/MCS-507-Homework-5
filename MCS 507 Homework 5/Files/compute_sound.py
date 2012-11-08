# L-3 MCS 507 Fri 31 Aug 2011 : compute_sound.py

import numpy as np
r = 44100; f = 440; m = 6; A = 1
t = np.linspace(0,m,m*r)
s = A*np.sin(2*np.pi*f*t)

delay = np.zeros(r)
echo = 0.5*s[0:len(s)/2]
sound = np.concatenate((s,delay,echo))

max_amplitude = 2**15-1
sound = max_amplitude*sound
sound = sound.astype(np.int16)

import scitools.sound
scitools.sound.write(sound,'atone.wav')
scitools.sound.play('atone.wav')
