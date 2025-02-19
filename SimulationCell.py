from collections.abc import Iterable

import numpy as np
import numpy.typing as npt

from ChemPy.AtomicSystems import Atom

# import globalConfigs
from ChemPy.VectorSpace import System


class SimulationCell:
    __slots__ = "system", "cellSize", "data"
    # cutoffRadii = globalConfigs.cutOff

    def __init__(
        self,
        system: System[Atom],
        cellSize: float,
        data: tuple[
            list[str],
            npt.NDArray[np.float64],
            npt.NDArray[np.float64],
            npt.NDArray[np.float64],
        ],
    ) -> None:
        self.system = system
        self.cellSize = cellSize
        self.data = data

    # def plot(self) -> None:
    #     fig: plt.Figure = plt.figure()
    #     ax = fig.add_subplot(projection="3d")
    #     ax.set_xlim(0, self.cellSize)
    #     ax.set_ylim(0, self.cellSize)
    #     ax.set_zlim(0, self.cellSize)

    #     colorList = [globalConfigs.colorAtom[atom.label] for atom in self.system]
    #     x = [atom.x + self.cellSize / 2 for atom in self.system]
    #     y = [atom.y + self.cellSize / 2 for atom in self.system]
    #     z = [atom.z + self.cellSize / 2 for atom in self.system]
    #     ax.scatter3D(x, y, z, c=colorList, s=100)
    #     plt.show()

    @classmethod
    def fromIterable(cls, atomIterable: Iterable[str], size: float = 0.0) -> "SimulationCell":
        atoms: list["Atom"] = []
        atomSymbols: list[str] = []
        xCoordinates: list[float] = []
        yCoordinates: list[float] = []
        zCoordinates: list[float] = []

        for atomLine in atomIterable:
            atom = Atom.fromStr(atomLine)
            atoms.append(atom)
            atomSymbols.append(atom.label)
            xCoordinates.append(float(atom.x))
            yCoordinates.append(float(atom.y))
            zCoordinates.append(float(atom.z))

        xArray = np.array(xCoordinates, dtype=float)
        yArray = np.array(yCoordinates, dtype=float)
        zArray = np.array(zCoordinates, dtype=float)
        atomicSystem = System[Atom](components=atoms)
        numpyArrays = (atomSymbols, xArray, yArray, zArray)
        return cls(atomicSystem, data=numpyArrays, cellSize=size)
