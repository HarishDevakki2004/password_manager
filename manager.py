from storage import load_vault, save_vault
from crypto_utils import encrypt_password, decrypt_password


class PasswordManager:

    def __init__(self):
        self.vault = load_vault()

    def add_password(self, site, password):
        encrypted = encrypt_password(password)
        self.vault[site] = encrypted
        save_vault(self.vault)
        print("Password saved.")

    def get_password(self, site):
        if site not in self.vault:
            print("No password found.")
            return

        decrypted = decrypt_password(self.vault[site])
        print(f"{site} password: {decrypted}")

    def delete_password(self, site):
        if site in self.vault:
            del self.vault[site]
            save_vault(self.vault)
            print("Password deleted.")
        else:
            print("Site not found.")

    def list_sites(self):
        if not self.vault:
            print("Vault is empty.")
            return

        for site in self.vault:
            print(site)