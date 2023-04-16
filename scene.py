from model import *


class Scene:
    def __init__(self, app):
        self.moving_cube = None
        self.app = app
        self.objects = []
        self.load()
        # skybox
        self.skybox = SkyBox(app)

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        n, s = 30, 3
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(app, pos=(x, -s, z)))

        # moving cube
        self.moving_cube = MovingCube(app, pos=(0, 6, 8), scale=(3, 3, 3), tex_id=1)
        add(self.moving_cube)

        add(Cat(app, pos=(0, -2, -10)))

    def render(self):
        self.update()
        for obj in self.objects:
            obj.render()
        self.skybox.render()

    def update(self):
        self.moving_cube.rot.xyz = self.app.time
