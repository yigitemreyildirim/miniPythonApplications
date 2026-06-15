import os


def log_and_check_proxy(func):
    def wrapper(*args, **kwargs):
        modul = args[0] 
        print(f"\n[PROXY CHANGER] Routing '{modul.moduleName}' through anonymous proxies...")
        print("[PROXY CHANGER] Status: Encryption Active. Proxy Chain: SECURE.")
        return func(*args, **kwargs)
    return wrapper

class TargetServer():
    def __init__(self, targetip, secLevel):
        self.ip = targetip
        self.security_level = secLevel
        self.isHacked = False

class AttackModule():
    def __init__(self, moduleName, requiredPower):
        self.moduleName = moduleName
        self.requiredPower = requiredPower

    @log_and_check_proxy
    def launchAttack(self, targetServer):
        print(f"[SYSTEM] {self.moduleName} module performs a general scanning of {targetServer.ip} operations.")

class BruteForceModule(AttackModule):
    def __init__(self, requiredPower, wordlistSize, moduleName="Brute Force Attack"):
        super().__init__(moduleName, requiredPower)
        self.wordlistSize = wordlistSize

    @log_and_check_proxy
    def launchAttack(self, targetServer):
        if targetServer.security_level > self.requiredPower:
            raise SystemExceptionDetected()
        else:
            targetServer.isHacked = True
            print(f"{self.requiredPower} power used.")
            print(f"[BRUTE FORCE] {self.moduleName} successfully tried {self.wordlistSize} combinations on {targetServer.ip}!")

class PhishingModule(AttackModule):
    def __init__(self, fakeSiteType, requiredPower, moduleName="Phishing Attack"):
        super().__init__(moduleName, requiredPower)
        self.fakeSiteType = fakeSiteType

    @log_and_check_proxy
    def launchAttack(self, targetServer):
        if targetServer.security_level > self.requiredPower:
            raise SystemExceptionDetected()    
        else:        
            print(f"[PHISHING] Sending trap emails with a fake {self.fakeSiteType} page to users on network {targetServer.ip}")
            print(f"{self.requiredPower} power used.")
            targetServer.isHacked = True    

class SystemExceptionDetected(Exception):
    def __init__(self, message="Attack Blocked! IDS system tracked your IP address."):
        super().__init__(message)


servers = [
    TargetServer("10.20.30.40", 5),   
    TargetServer("192.168.1.1", 12),  
    TargetServer("10.99.99.1", 50)]


print("--- SHADOWNET PENETRATION TERMINAL ACTIVE ---")
input("\npress enter to start")

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" + "="*40)
    print("1 -> List All Target Servers")
    print("2 -> Launch Brute Force Attack")
    print("3 -> Filter Weak Targets (Lambda)")
    print("4 -> Launch Phishing Attack")
    print("q -> Shutdown Terminal")
    print("="*40)

    userInput = input("Select an option: ").strip()

    if userInput.lower() == 'q':
        print("\n[SYSTEM] Terminal shutting down. Goodbye, operator.")
        break

    try:
        if userInput == '1':
            print("\n--- TARGET LIST ---")
            for i, server in enumerate(servers):
                print(f"[{i}] IP: {server.ip} | Sec Level: {server.security_level} | Hacked: {server.isHacked}")

        elif userInput == '2':
            print("\n--- CHOOSE TARGET TO ATTACK ---")
            for i, server in enumerate(servers):
                print(f"[{i}] IP: {server.ip} (Level {server.security_level})")

            server_index = input("Select server index: ")
            if server_index.isdigit() and int(server_index) < len(servers):
                selected_server = servers[int(server_index)]

                attackModule = BruteForceModule(requiredPower=15, wordlistSize=100)
                attackModule.launchAttack(selected_server)
            else:
                print("Invalid server selection!")

        elif userInput == '3':
            print("\n--- SCANNING FOR WEAK TARGETS (Sec Level < 15) ---")

            weak_servers = list(filter(lambda s: s.security_level < 15, servers))

            if not weak_servers:
                print("No weak targets found.")
            else:
                for ws in weak_servers:
                    print(f"Easy Target -> IP: {ws.ip} | Sec Level: {ws.security_level}")

        elif userInput == '4':
            print("\n--- CHOOSE TARGET FOR PHISHING ---")
            for i, server in enumerate(servers):
                print(f"[{i}] IP: {server.ip} (Level {server.security_level})")

            server_index = input("Select server index: ")
            if server_index.isdigit() and int(server_index) < len(servers):
                selected_server = servers[int(server_index)]

                attackModule = PhishingModule(fakeSiteType="bank login", requiredPower=15)
                attackModule.launchAttack(selected_server)
            else:
                print("Invalid server selection!")

        else:
            print("Invalid option. Try again.")

    except SystemExceptionDetected as e:
        print(f"\n[CRITICAL ALERT] Exception Caught: {e}")
        print("[SYSTEM] Proxy chain wiped. Subnet changed. Continuing operations")

    input("\n[press enter]")
