import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from std_srvs.srv import Trigger

class MonitorNode(Node):
	def __init__(self):
		super().__init__('monitor_node')
		self.sub = self.create_subscription(Float32, '/battery_level', self.sub_callback, 10)
		self.client = self.create_client(Trigger, 'recharge')
		self.recharge_request = False

	def sub_callback(self, msg):
		battery_level = msg.data
		if battery_level >= 20:
			self.get_logger().info(f'Battery Level: {battery_level}')
		else:
			self.get_logger().warn(f'Low Battery! Battery Level: {battery_level}')
			if battery_level < 5 and not self.recharge_request:
				self.get_logger().warn('Battery Ending')
				self.battery_upload()

	def battery_upload(self):
		self.recharge_request = True
		request = Trigger.Request()
		future = self.client.call_async(request)
		future.add_done_callback(self.response_callback)

	def response_callback(self, future):
		response = future.result()
		self.get_logger().info(f'response: {response.message}, success: {response.success}')
		self.recharge_request = False

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
