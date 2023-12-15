import rclpy
from rclpy.node import Node
from custom_msg.msg import InfPersonalUsuario  # Asegúrate de ajustar el nombre del mensaje
from custom_msg.msg import EmocionUsuario  # Asegúrate de ajustar el nombre del mensaje
from custom_msg.msg import PosicionUsuario  # Asegúrate de ajustar el nombre del mensaje
from custom_msg.msg import Usuario  # Asegúrate de ajustar el nombre del mensaje


class EmpaquetadorNodo(Node):
    def __init__(self):
        super().__init__('empaquetador_nodo')
        self.subscriber1 = self.create_subscription(InfPersonalUsuario, 'inf_pers_topic', self.callback_nodo1, 10)
        self.subscriber2 = self.create_subscription(EmocionUsuario, 'emocion_topic', self.callback_nodo2, 10)
        self.subscriber3 = self.create_subscription(PosicionUsuario, 'pos_usuario_topic', self.callback_nodo3, 10)

        self.dialogo_publisher = self.create_publisher(Usuario, 'topic_dialogo', 10)
        self.reset_message()

    def reset_message(self):
        self.msg = Usuario()
        # self.msg.infpersonal.nombre = None
        self.msg.infpersonal.edad = -1
        # self.msg.infpersonal.idiomas = None
        # self.msg.emocion = None
        self.msg.posicion.x = -1
        self.msg.posicion.y = -1
        self.msg.posicion.z = -1

    def callback_nodo1(self, msg):
        self.msg.infpersonal.nombre = msg.nombre
        self.msg.infpersonal.edad = msg.edad
        self.msg.infpersonal.idiomas = msg.idiomas
        self.try_publish_message()

    def callback_nodo2(self, msg):
        self.msg.emocion = msg.emocion
        self.try_publish_message()

    def callback_nodo3(self, msg):
        self.msg.posicion.x = msg.x
        self.msg.posicion.y = msg.y
        self.msg.posicion.z = msg.z
        self.try_publish_message()

    def try_publish_message(self):
        if not (self.msg.infpersonal.nombre == '' or self.msg.infpersonal.edad == -1 or self.msg.infpersonal.idiomas == '' or
            self.msg.emocion == '' or self.msg.posicion.x == -1 or self.msg.posicion.y == -1 or self.msg.posicion.z == -1):

            self.dialogo_publisher.publish(self.msg)
            self.get_logger().info("Mensaje enviado al nodo dialogo_nodo")
            self.reset_message()

def main(args=None):
    rclpy.init(args=args)

    empaquetador_nodo = EmpaquetadorNodo()

    try:
        rclpy.spin(empaquetador_nodo)
    except KeyboardInterrupt:
        pass

    empaquetador_nodo.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
