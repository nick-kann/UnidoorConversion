import trimesh

prepath = 'car/car1/texture_dae/'

mesh = trimesh.load(prepath + 'car-board.dae')

mesh.export('board.stl')

mesh = trimesh.load(prepath + 'car-door.dae')

mesh.export('frame.stl')

mesh = trimesh.load(prepath + '9968001-handle.dae')

mesh.export('9968001.stl')
