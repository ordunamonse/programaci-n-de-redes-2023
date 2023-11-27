'''
Conexion 
Fecha:24/11/2023
Nombre:Monserrat Orduña Basaldua
'''
from netmiko import ConnectHandler

sshCli  = ConnectHandler(
    device_type= 'cisco_ios',
    host='10.10.20.48',
    port=22,
    username ='developer',
    password ='C1sco12345'
)

salida = sshCli.send_command('show ip int brief')
print(salida)

config_commands = [
    'int loopback 1', 
    'ip address 2.2.2.2 255.255.255.0', 
    'description WHATEVER'
                  ] 

output = sshCli.send_config_set(config_commands)


salida_despues = sshCli.send_command('show ip int brief')
print(salida_despues)

config_commands_loopback2 = [
    'int loopback 2', 
    'ip address 3.3.3.3 255.255.255.0', 
    'description HATEVER'
]

output_loopback2 = sshCli.send_config_set(config_commands_loopback2)




