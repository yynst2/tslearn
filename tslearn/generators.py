import numpy

__author__ = 'Romain Tavenard romain.tavenard[at]univ-rennes2.fr'


def random_walks(n_ts=100, sz=256, d=1, mu=0., std=1.0):
    """Random walk time series generator.
    Generate `n_ts` time series of size `sz` and dimensionality `d`.
    Generated time series follow the model:
    ts[t] = ts[t - 1] + a
    where a is drawn from a normal distribution of mean `mu` and standard deviation 
    `std`."""
    ts = numpy.empty((n_ts, sz, d))
    rnd = numpy.random.randn(n_ts, sz, d) * std + mu
    ts[:, 0, :] = rnd[:, 0, :]
    for t in range(1, sz):
        ts[:, t, :] = ts[:, t - 1, :] + rnd[:, t, :]
    return ts


def random_walk_blobs(n_ts_per_blob=100, sz=256, d=1, n_blobs=2, noise_level=1.0):
    """Blob-based random walk time series generator.
    Generate `n_ts_per_blobs`*`n_blobs` time series of size `sz` and dimensionality `d`.
    Generated time series follow the model:
    ts[t] = ts[t - 1] + a
    where a is drawn from a normal distribution of mean `mu` and standard deviation `std`.
    
    Each blob contains time series derived from a same seed time series with added white 
    noise at level `noise_level`."""
    base_ts = random_walks(n_ts=n_blobs, sz=sz, d=d, std=1.0)
    rnd = numpy.random.randn(n_ts_per_blob * n_blobs, sz, d) * noise_level
    ts = numpy.repeat(base_ts, repeats=n_ts_per_blob, axis=0)
    y = numpy.repeat(range(n_blobs), repeats=n_ts_per_blob)
    return ts + rnd, y
