import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import pyautogui

class TB3Controller(Node):

    def __init__(self):
        super().__init__('tb3_controller')

        self.cmd_subscription = self.create_subscription(String, '/cmd', self.cmd_cb, 10)

    def cmd_cb(self, msg):

        if msg.data == 'Forward':
            pyautogui.press('w')
        elif msg.data == 'Backward':
            pyautogui.press('x')
        elif msg.data == 'Left Turn':
            pyautogui.press('a')
        elif msg.data == 'Right Turn':
            pyautogui.press('d')
        elif msg.data == 'Stop':
            pyautogui.press('s')

def main(args=None):
    rclpy.init(args=args)
    tb3_controller = TB3Controller()
    try:
        rclpy.spin(tb3_controller)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()