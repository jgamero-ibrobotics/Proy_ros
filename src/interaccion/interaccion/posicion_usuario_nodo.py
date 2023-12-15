import rclpy
from rclpy.node import Node
from custom_msg.msg import PosicionUsuario  # Asegúrate de ajustar el nombre del mensaje

class PosicionUsuarioNode(Node):
    def __init__(self):
        super().__init__('posicion_usuario_nodo')

    def run(self):
        publisher = self.create_publisher(PosicionUsuario, 'pos_usuario_topic', 10)
        while rclpy.ok():
            x = input("Ingrese su coordenada x: ")
            y = input("Ingrese su coordenada y: ")
            z = input("Ingrese su coordenada z: ")


            # Publicar la información en un mensaje ROS
            msg = PosicionUsuario()
            msg.x = int(x)
            msg.y = int(y)
            msg.z = int(z)


            publisher.publish(msg)
            self.get_logger().info("Información personal publicada")

        


def main(args=None):
    rclpy.init(args=args)

    posicion_usuario_nodo = PosicionUsuarioNode()
    try:
        posicion_usuario_nodo.run()
    except KeyboardInterrupt:
        pass
    finally:
        posicion_usuario_nodo.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()