import numpy as np

class Section():
    def __init__(self, coords):
        self.coords = coords
        self.lons, self.lats = np.array([lon for (lon, lat) in coords]), np.array([lat for (lon, lat) in coords])

    def __repr__(self):
        return self.coords