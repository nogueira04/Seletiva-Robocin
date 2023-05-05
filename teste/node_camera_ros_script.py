import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class ImagePublisher(Node):

    def __init__(self):
        super().__init__('image_publisher')
        self.get_logger().info("enviando..")
        self.publisher_ = self.create_publisher(Image, '/camera/image_raw', 10)
        self.timer_ = self.create_timer(0.05, self.publish_image)

        self.bridge_ = CvBridge()
        self.cap = cv2.VideoCapture(0)


    def publish_image(self):
    
        ignore, frame =  self.cap.read()

        image = cv2.resize(frame, (640, 480))

        msg = self.bridge_.cv2_to_imgmsg(image, "bgr8")

        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = ImagePublisher()
    node.publish_image()
    rclpy.spin(node)
    rclpy.shutdown()

main()