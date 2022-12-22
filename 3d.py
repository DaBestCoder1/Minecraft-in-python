from ursina import*
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

grass_block = load_texture('assets/mcgrass.jpeg')
stone_block = load_texture('assets/stone.png')
brick_block = load_texture('assets/brick.jpg')
dirt_block = load_texture('assets/dirt.jpg')
planks_block = load_texture('assets/planks.png')
diamond_block = load_texture('assets/diamond.jpeg')
block_pick = 1

def update():
    global block_pick


    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4
    if held_keys['5']: block_pick = 5
    if held_keys['6']: block_pick = 6




class Voxel(Button):
    def __init__(self, position = (0, 0, 0), texture = grass_block):
        super().__init__(
            Sky(),
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = texture,
            color = color.white,
            highlight_color = color.light_gray,
            scale = 1
        )

    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = grass_block)
                if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = stone_block)
                if block_pick == 3: voxel = Voxel(position = self.position + mouse.normal, texture = brick_block)
                if block_pick == 4: voxel = Voxel(position = self.position + mouse.normal, texture = dirt_block)
                if block_pick == 5: voxel = Voxel(position = self.position + mouse.normal, texture = planks_block)
                if block_pick == 6: voxel = Voxel(position = self.position + mouse.normal, texture = diamond_block)
            if key == 'right mouse down':
                destroy(self)
            if key == 'q':
                quit()


for z in range(30):
    for x in range(30):
        voxel = Voxel(position = (x, 0, z))
player = FirstPersonController()

app.run()