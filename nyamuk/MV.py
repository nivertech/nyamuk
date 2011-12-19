'''
@author Iwan Budi Kusnanto
'''
class MV:
    '''
    MQTT Variable and Constanta
    '''
    UNKNOWN_VAL = -1
    
    PROTOCOL_NAME = "MQIsdp"
    PROTOCOL_VERSION = 3
    
    CONNECT = 0x10
    
    #CLIENT_STATE
    CS_NEW = 0
    CS_CONNECTED = 1
    CS_DISCONNECTING = 2
    
    #socket
    INVALID_SOCKET = -1
    KEEPALIVE_VAL = 60

    #ERROR
    ERR_SUCCESS = 0
    ERR_NO_MEM = 1
    ERR_PROTOCOL = 2
    ERR_INVAL = 3
    ERR_NO_CONN = 4
    ERR_CONN_REFUSED = 5
    ERR_NOT_FOUND = 6
    ERR_CONN_LOST = 7
    ERR_SSL = 8
    ERR_PAYLOAD_SIZE = 9
    ERR_NOT_SUPPORTED = 10
    ERR_UNKNOWN = 13
    
    #COMMAND
    CMD_CONNECT = 0x10
    CMD_CONNACK = 0x20
    CMD_PUBLISH = 0x30
    CMD_PUBACK = 0x40
    CMD_PUBREC = 0x50
    CMD_PUBREL = 0x60
    CMD_PUBCOMP = 0x70
    CMD_SUBSCRIBE = 0x80
    CMD_SUBACK = 0x90
    CMD_UNSUBSCRIBE = 0xA0
    CMD_UNSUBACK = 0xB0
    CMD_PINGREQ = 0xC0
    CMD_PINGRESP = 0xD0
    CMD_DISCONNECT = 0xE0
    
    #OTHER
    MESSAGE_RETRY = 20
    
    #DIRECTION
    DIRECTION_NONE = -1
    DIRECTION_IN = 0
    DIRECTION_OUT = 1
    
    #MESSAGE STATE
    MS_INVALID = 0
    MS_WAIT_PUBACK = 1
    MS_WAIT_PUBREC = 2
    MS_WAIT_PUBREL = 3
    MS_WAIT_PUBCOMP = 4
    
    def __init__(self):
        pass
    