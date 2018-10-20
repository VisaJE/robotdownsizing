

class Block_solver:

    def __init__(self,left_motor,right_motor,touch_sensor_right,touch_sensor_left):
        self.position=position
        self.left_motor=left_motor
        self.right_motor=right_motor
        self.touch_sensor_left=touch_sensor_left
        self.touch_sensor_right=touch_sensor_right


    def execute1():
        start=[0,0]
        preferred=[[20,100],[70,170],[55,320]]
        solver1=Pylvas_solver(self.left_motor,self.right_motor,self.touch_sensor_right,self.touch_sensor_left,start,preferred)
        solver1.execute()

    def execute2():
        start=[0,0]
        return
