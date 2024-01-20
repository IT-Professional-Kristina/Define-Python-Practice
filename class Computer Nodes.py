# Greeting Function
def greet(any):
    return f"Welcome"


result = greet(any)
print(result)

greet_1 = input("How can I assist you please?")
print(greet_1)

greet_2 = input("I will be glad to help you define Computer Nodes")
print(greet_2)
# Defining  Class Computer Nodes
class Computer_Nodes:
    def __init__(self, name, Protocol, MAC_Address, IP_Address):
        self.name = name
        self.Protocol = Protocol
        self.MAC_Address = MAC_Address
        self.IP_Address = IP_Address
    def node_name(self):
         print(f"{self.name} is a node on the Museum Network")
    def node_Protocol(self, Protocol):
         print(f"{self.name} is using the {self.Protocol}.")
    def node_MAC_Address(self, MAC_Address):
         print(f"{self.name}, has a MAC_Address that is {self.MAC_Address}")
    def node_IP_Address(self, IP_Address):
         print(f"{self.name} IP Address is {self.IP_Address}")

node = Computer_Nodes("HP_Laptop", "TCP", "00:11:22:33:44:55", "192.168.10.2")
node2 = Computer_Nodes("Smartphone", "SMTP", "11:22:33:44:55:66", "178.219.1.0")
node3 = Computer_Nodes("Desktop", "HTTP", "22:33:44:55:66:77", "110.45.6.0")


node.node_name()
node.node_Protocol("TCP")
node.node_MAC_Address("00:11:22:33:44:55")
node2.node_name()
node2.node_Protocol("SMTP")
node2.node_MAC_Address("11:22:33:44:55:66")
node2.node_IP_Address("178.219.1.0")
node3.node_name()
node3.node_Protocol("HTTP")
node3.node_MAC_Address("22:33:44:55:66:77")
node3.node_IP_Address("110.45.6.0")
