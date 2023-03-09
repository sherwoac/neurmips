import numpy as np
import vedo 
from plane_geometry import orthonormal_basis_from_xy

def visualize_geometry(
    points,
    model,
    r:float=2,
    c:list=(0.5,0.5,0.5),
    alpha:float=0.5,
    screenshot_name:str=None
):
    objs = []
    points = points.cpu().numpy() 
    points = vedo.Points(points, r=r, c=c, alpha=1)
    objs.append(points)
    
    center = model.center.detach().cpu().numpy()
    xyz = orthonormal_basis_from_xy(model.xy.detach()).detach().cpu().numpy()
    wh = model.wh.detach().cpu().numpy()

    colors = np.random.rand(model.n_plane, 3)
    for i in range(model.n_plane):
        c = center[i]
        x, y = xyz[i,:,0], xyz[i,:,1]
        x_s, y_s = x*(wh[i, 0]/2), y*(wh[i, 1]/2)
        verts = [c+x_s+y_s, c-x_s+y_s, c-x_s-y_s, c+x_s-y_s]
        faces = [[0,1,2], [2,3,0]]
        plane = vedo.Mesh([verts, faces], c=colors[i], alpha=alpha)
        objs.append(plane)
        
    vedo.show(*objs ,axes=1)
    if screenshot_name:
        vedo.io.screenshot(screenshot_name)