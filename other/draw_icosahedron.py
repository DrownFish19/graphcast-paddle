import vtk

import graphtype


def draw_vtk():
    # 创建一个正二十面体
    icosahedron = vtk.vtkPlatonicSolidSource()
    icosahedron.SetSolidTypeToIcosahedron()

    # 创建映射器和演员
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(icosahedron.GetOutputPort())
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    # 创建渲染器和渲染窗口
    renderer = vtk.vtkRenderer()
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.AddRenderer(renderer)

    # 创建渲染窗口交互器
    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # 添加演员到渲染器
    renderer.AddActor(actor)
    renderer.SetBackground(0.1, 0.2, 0.4)  # 设置背景颜色

    # 开始渲染
    renderWindow.Render()

    # 启动交互器
    renderWindowInteractor.Start()


def draw_vtk_define(polyhedron):
    # 创建点（顶点）
    points = vtk.vtkPoints()
    for idx in range(polyhedron.vertices.shape[0]):
        vertex = polyhedron.vertices[idx]
        points.InsertNextPoint([vertex[0], vertex[1], vertex[2]])

    # 创建面
    triangles = vtk.vtkCellArray()
    for idx in range(polyhedron.faces.shape[0]):
        face = polyhedron.faces[idx]
        triangle = vtk.vtkTriangle()
        triangle.GetPointIds().SetId(0, face[0])
        triangle.GetPointIds().SetId(1, face[1])
        triangle.GetPointIds().SetId(2, face[2])
        triangles.InsertNextCell(triangle)

    # 创建多边形数据
    polydata = vtk.vtkPolyData()
    polydata.SetPoints(points)
    polydata.SetPolys(triangles)

    # 创建映射器和演员
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(polydata)
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    # 创建渲染器和渲染窗口
    renderer = vtk.vtkRenderer()
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.AddRenderer(renderer)

    # 创建渲染窗口交互器
    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # 添加演员到渲染器
    renderer.AddActor(actor)
    renderer.SetBackground(0.1, 0.2, 0.4)  # 设置背景颜色

    # 开始渲染
    renderWindow.Render()

    # 启动交互器
    renderWindowInteractor.Start()


icosahedron = graphtype.get_icosahedron()
polyhedrons = graphtype.get_hierarchy_of_triangular_meshes_for_sphere(6)
draw_vtk_define(polyhedrons[5])
