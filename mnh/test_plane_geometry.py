import torch
from plane_geometry import PlaneGeometry
from utils_visualize import visualize_geometry

def test(): 
    points = torch.randn(1000, 3)
    model = PlaneGeometry(10)
    model.initialize(points, 20)
    planes_points, planes_idx = model.sample_planes_points(2000)
    visualize_geometry(planes_points, model)

if __name__ == '__main__':
    test()