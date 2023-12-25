
from custom_msg.msg import Usuario  # Asegúrate de ajustar el nombre del mensaje
from custom_msg.srv import Multiplicador
import rclpy
from rclpy.node import Node

class DialogoNode(Node):
    def __init__(self):
        super().__init__('dialogo_nodo')
        self.subscription = self.create_subscription(Usuario, 'user_topic', self.callback, 10)
        self.cli = self.create_client(Multiplicador, 'servicio_multiplicador')
       
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        
        # Crea la variable que almacenará los datos que se enviarán en la petición
        # al servicio
        self.req = Multiplicador.Request()
        self.edad = None
        
        
    def callback(self, msg):
        self.get_logger().info("--------------Mensaje recibido--------------")
        self.get_logger().info(f"Nombre: {msg.infpersonal.nombre}")
        self.get_logger().info(f"Edad: {msg.infpersonal.edad}")
        self.get_logger().info(f"Idiomas: {msg.infpersonal.idiomas}")
        self.get_logger().info(f"Emoción: {msg.emocion}")
        self.get_logger().info(f"Posición (x, y, z): ({msg.posicion.x}, {msg.posicion.y}, {msg.posicion.z})")
        self.get_logger().info("--------------------------------------------")
        self.edad = msg.infpersonal.edad
        self.send_request(msg.infpersonal.edad)

    def send_request(self, entrada):#Mandamos peticion con la edad
        self.req.entrada = entrada
        self.future = self.cli.call_async(self.req).add_done_callback(self.servicio_callback)#Configuramos un callback para manejar la respuesta del servicio
        
    def servicio_callback(self, future):#Maneja la respuesta del servicio una vez está disponible
        try:
         response = future.result()
         self.get_logger().info('Resultado de la multiplicacion: %d * 2 = %d' % (self.edad,response.resultado))
                
        except Exception as e:
            self.get_logger().info(f'Error en el servicio: {e}')
         
            
def main(args=None):
    rclpy.init(args=args)

    dialogo_nodo = DialogoNode()
    try:
        rclpy.spin(dialogo_nodo)#Bucle principal
    except KeyboardInterrupt:
        pass
    finally:
        dialogo_nodo.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
