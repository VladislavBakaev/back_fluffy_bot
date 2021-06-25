from fluffy_bot.movement_sequence import NewMovement

class MotionControlManager():
    def __init__(self):
        self.control = NewMovement()
    
    def play_emotion(self, name):
        self.control.play_emotion(name)
    
    def get_emation_name(self):
        names = self.control.get_all_motion_name()
        return names
    
    def stop_move(self):
        self.control.stop_emotion()
    
    def save_emotion(self, emotion):
        self.control.sequence = emotion
        self.control.save_move()

motionControlManager = MotionControlManager()