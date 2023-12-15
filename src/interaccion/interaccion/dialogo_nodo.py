import rclpy
from rclpy.node import Node
from custom_msg.msg import Usuario  # Asegúrate de ajustar el nombre del mensaje

class DialogoNode(Node):
    def __init__(self):
        super().__init__('dialogo_nodo')
        self.subscription = self.create_subscription(Usuario, 'topic_dialogo', self.callback, 10)

    def callback(self, msg):
        self.get_logger().info("--------------Mensaje recibido--------------")
        self.get_logger().info(f"Nombre: {msg.infpersonal.nombre}")
        self.get_logger().info(f"Edad: {msg.infpersonal.edad}")
        self.get_logger().info(f"Idiomas: {msg.infpersonal.idiomas}")
        self.get_logger().info(f"Emoción: {msg.emocion}")
        self.get_logger().info(f"Posición (x, y, z): ({msg.posicion.x}, {msg.posicion.y}, {msg.posicion.z})")
        self.get_logger().info("--------------------------------------------")

def main(args=None):
    rclpy.init(args=args)

    dialogo_nodo = DialogoNode()

    try:
        rclpy.spin(dialogo_nodo)
    except KeyboardInterrupt:
        pass

    dialogo_nodo.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
