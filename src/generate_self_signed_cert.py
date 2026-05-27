
from pathlib import Path
import subprocess


def generate_self_signed_certificate():
    """
    Generates a self-signed TLS certificate for local
    Nginx reverse proxy testing.
    """

    cert_dir = Path("config/certs")
    cert_dir.mkdir(parents=True, exist_ok=True)

    cert_file = cert_dir / "localhost.crt"
    key_file = cert_dir / "localhost.key"

    openssl_command = [
        "openssl",
        "req",
        "-x509",
        "-nodes",
        "-days",
        "365",
        "-newkey",
        "rsa:2048",
        "-keyout",
        str(key_file),
        "-out",
        str(cert_file),
        "-subj",
        "/CN=localhost"
    ]

    try:
        subprocess.run(openssl_command, check=True)

        print("\nSelf-signed certificate generated successfully.")
        print(f"Certificate: {cert_file}")
        print(f"Private Key: {key_file}")

    except subprocess.CalledProcessError as error:
        print("\nFailed to generate certificate.")
        print(error)


if __name__ == "__main__":
    generate_self_signed_certificate()

