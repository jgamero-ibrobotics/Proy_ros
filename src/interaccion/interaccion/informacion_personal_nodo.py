import rclpy #Biblioteca para crear nodos
from rclpy.node import Node
from custom_msg.msg import InfPersonalUsuario  # Asegúrate de ajustar el nombre del mensaje

class InformacionPersonalNodo(Node):
    def __init__(self): #Constructor de la clase
        super().__init__('informacion_personal_nodo')#Nombre específico del nodo

    def run(self):
        publisher = self.create_publisher(InfPersonalUsuario, 'inf_pers_topic', 10)#Creamos publicador 
        while rclpy.ok(): #Bucle en el cual se recopila la informacion a traves de teclado
            nombre = input("Ingrese el nombre del usuario: ")
            edad = int(input("Ingrese la edad del usuario: "))
            idiomas = input("Ingrese los idiomas que habla (separados por comas): ").split(',')

            # Publicar la información en un mensaje ROS
            msg = InfPersonalUsuario()
            msg.nombre = nombre
            msg.edad = edad
            msg.idiomas = idiomas

            publisher.publish(msg)
            self.get_logger().info("Información personal publicada")



def main(args=None):
    rclpy.init(args=args)

    informacion_personal_nodo = InformacionPersonalNodo()
    try:
        informacion_personal_nodo.run()
    except KeyboardInterrupt:
        pass
    finally:
        informacion_personal_nodo.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()