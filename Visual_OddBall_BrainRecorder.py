'''Brainwave recorder functions using 4-channel Muse-2 EEG'''
import numpy as np
import pandas as pd
from muselsl import record, stream, view, list_muses
from pylsl import StreamInlet, resolve_byprop 

if __name__ == "__main__":
    streams = resolve_byprop('type', 'EEG', timeout=5)
    if not streams:
        print('Could not connect to a muse device.')
    else:
        inlet = StreamInlet(streams[0], max_chunklen=12)
        eeg_time_correction = inlet.time_correction()

        info = inlet.info()
        description = info.desc()

        fs = int(info.nominal_srate())
        