from scene import Scene

class SceneHandler:
    def __init__(self):
        self.scenes = {}
        self.current_scene = None
        self.previous_scene = None

    def set_scene(self, key_name: str):
        '''Set the current scene
        key_name: the scenes name given when added'''
        if not self.current_scene == None:
            self.previous_scene = self.current_scene

        self.current_scene = self.scenes[key_name]
        self.current_scene.init()
    
    def set_previous_scene(self):
        '''Change the current scene to the previous scene'''
        if self.previous_scene == None:
            return
        
        new_prev_scene = self.current_scene
        self.current_scene = self.previous_scene
        self.previous_scene = new_prev_scene
        self.current_scene.init()

    def add_scene(self, key_name: str, scene: Scene):
        '''Add a scene to list of scenes with a name for identification'''
        self.scenes[key_name] = scene
    
    def check_events(self):
        '''Call the current scenes check_event method'''
        if self.current_scene == None:
            return
        
        self.current_scene.check_events()

    def draw(self):
        '''Call the current scenes draw method'''
        if self.current_scene == None:
            return
        
        self.current_scene.draw()