from scene import Scene

class SceneHandler:
    def __init__(self):
        self.scenes = {}
        self.current_scene = None
        self.previous_scene = None

    def set_scene(self, key_name: str):
        if not self.current_scene == None:
            self.previous_scene = self.current_scene

        self.current_scene = self.scenes[key_name]
        self.current_scene.init()
    
    def set_previous_scene(self):
        if self.previous_scene == None:
            return
        
        new_prev_scene = self.current_scene
        self.current_scene = self.previous_scene
        self.previous_scene = new_prev_scene
        self.current_scene.init()

    def add_scene(self, key_name: str, scene: Scene):
        # TODO Check wether the scene exists or not first
        self.scenes[key_name] = scene
    
    def check_events(self):
        if self.current_scene == None:
            return
        
        self.current_scene.check_events()

    def draw(self):
        if self.current_scene == None:
            return
        
        self.current_scene.draw()