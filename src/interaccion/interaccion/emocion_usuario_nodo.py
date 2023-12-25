import rclpy
from rclpy.node import Node
from custom_msg.msg import EmocionUsuario  # Asegúrate de ajustar el nombre del mensaje

class EmocionUsuarioNode(Node):
    def __init__(self):
        super().__init__('emocion_usuario_nodo')

    def run(self):
        publisher = self.create_publisher(EmocionUsuario, 'emocion_topic', 10)#Creamos el publicador
        while rclpy.ok():
            emocion = input("Ingrese como se siente: ")

            # Publicar la información en un mensaje ROS
            msg = EmocionUsuario()
            msg.emocion = emocion


            publisher.publish(msg)
            self.get_logger().info("Información personal publicada")

        
def main(args=None):
    rclpy.init(args=args)

    emocion_usuario_nodo = EmocionUsuarioNode()
    try:
        emocion_usuario_nodo.run()
    except KeyboardInterrupt:
        pass
    finally:
        emocion_usuario_nodo.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()