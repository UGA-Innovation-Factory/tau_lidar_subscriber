import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2, Image

from TauLidarCommon.frame import FrameType
from TauLidarCamera.camera import Camera
import cv2
import numpy as np
from cv_bridge import CvBridge


class LidarSubscriber(Node):
    def __init__(self):
        super().__init__('tau_lidar_subscriber')
        
        self.subscription_1 = self.create_subscription(
            Image,
            'Tau/depth',
            lambda img: cv2.imshow(img.data, 'depth'),
            10
        )

        self.subscription_2 = self.create_subscription(
            Image,
            'Tau/greyscale',
            lambda img: cv2.imshow(img.data, 'b&w'),
            10
        )


def main(args=None):
    rclpy.init(args=args)

    node = LidarSubscriber()

    rclpy.spin(node)

    # Destroy the timer attached to the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_timer(timer)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
