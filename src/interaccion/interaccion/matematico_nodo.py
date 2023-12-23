from custom_msg.srv import Multiplicador

import rclpy# Importa la biblioteca cliente Python de ROS 2
from rclpy.node import Node

class MatematicoNodo(Node):
    def __init__(self):
        
        super().__init__('matematico_nodo')
        self.srv = self.create_service(Multiplicador, 'servicio_multiplicador', self.multiplicador_callback)
    
    def multiplicador_callback(self, request, response):
        response.resultado = request.entrada*2
        self.get_logger().info('Incoming request\n: %d ' % (request.entrada))
        return response
    
def main(args=None):
    rclpy.init(args=args)
    matematico_nodo = MatematicoNodo()
    # Mantiene corriendo el bucle interno del nodo para poder gestionar las
    # peticiones del cliente
    try:
        rclpy.spin(matematico_nodo)
    except KeyboardInterrupt:
        pass
    
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()        