import numpy as np
import numpy.lib.recfunctions as rfn
from scipy.spatial.distance import cdist
import os
import numba

import strax
#from amstrax import Peaks

export, __all__ = strax.exporter()

@export
class Peaks(strax.Plugin):
    """
    Self-Organizing Maps (SOM)
    https://xe1t-wiki.lngs.infn.it/doku.php?id=xenon:xenonnt:lsanchez:unsupervised_neural_network_som_methods
    For peaklet classification. We this pluggin will provide 2 data types, the 'type' we are
    already familiar with, classifying peaklets as s1, s2 (using the new classification) or
    unknown (from the previous classification). As well as a new data type, SOM type, which
    will be assigned numbers based on the cluster in the SOM in which they are found. For
    each version I will make some documentation in the corrections repository explaining
    what I believe each cluster represents.

    This correction/plugin is currently on the testing phase, feel free to use it if you are
    curious or just want to test it or try it out but note this is note ready to be used in
    analysis.
    """
    depends_on = ('peak_waveforms','peaks_som')
    data_kind = 'peaks'
    # parallel = 'process'
    provides = ('peaks')
    rechunk_on_save = True
    __version__ = "0.2.0"

    def infer_dtype(self):
        dtype = super().infer_dtype()
        return dtype
    def compute(self, peak_waveforms, peaks_som):
        peaks = super().compute(peak_waveforms)
        peaks_som = super().compute(peaks_som)
        return strax.merged_dtype(peaks, peaks_som)
