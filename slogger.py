import serial
import logging
import datetime
import logging

class Slogger:
    def __init__(self, config):
        pass
    
    def ssh(self):
        pass
    
    def serial(self):
        pass


    
# Configure logging
logging.basicConfig(filename='serial_log.txt', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

# Serial port configuration
port = '/dev/ttyUSB0'  # Replace with your serial port
baudrate = 9600
timeout = 1

try:
    ser = serial.Serial(port, baudrate, timeout=timeout)
    logging.info("Serial port opened successfully")

    while True:
        line = ser.readline().decode('utf-8').strip() 
        if line:
            logging.info(line)

except serial.SerialException as e:
    logging.error(f"Error opening serial port: {e}")

finally:
    if ser.is_open:
        ser.close()
        logging.info("Serial port closed")
        




# Configure logging
logging.basicConfig(filename='ssh_log.txt', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def ssh_log(hostname, username, password, command):
    try:
        # Establish SSH connection
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, username=username, password=password)

        # Execute command
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode('utf-8')
        error = stderr.read().decode('utf-8')

        # Log output and errors
        logging.info(f"Command: {command}")
        logging.info(f"Output: {output}")
        if error:
            logging.error(f"Error: {error}")

    except Exception as e:
        logging.error(f"SSH connection failed: {e}")

    finally:
        ssh.close()

def main(args):
    pass


if __name__ == "__main__":
    main()        