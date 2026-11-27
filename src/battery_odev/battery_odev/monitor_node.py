import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class MonitorNode(Node):
	def __init__(self):
		super().__init__('monitor_node')
		self.sub = self.create_subscription(Float32, '/battery_level', self.sub_callback, 10)

	def sub_callback(self, msg):
		battery_level = msg.data
		if battery_level >= 20:
			self.get_logger().info(f'Battery Level: {battery_level}')
		else:
			self.get_logger().warn(f'Low Battery! Battery Level: {battery_level}')

def main(args=None):
	rclpy.init(args=args)
	monitor_node = MonitorNode()
	try:
		rclpy.spin(monitor_node)
	except KeyboardInterrupt:
			pass
	finally:
		monitor_node.destroy_node()
		if rclpy.ok():
			rclpy.shutdown()

if __name__ == '__main__':
	main()
