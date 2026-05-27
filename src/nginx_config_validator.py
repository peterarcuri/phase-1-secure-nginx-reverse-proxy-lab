from pathlib import Path

REQUIRED_SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
]

REQUIRED_DIRECTIVES = [
    "proxy_pass",
    "proxy_set_header Host",
    "proxy_set_header X-Real-IP",
    "proxy_set_header X-Forwarded-For",
    "proxy_set_header X-Forwarded-Proto",
    "limit_req",
    "return 301 https://",
]


def validate_nginx_configs(config_dir="config"):
    config_path = Path(config_dir)

    combined_config = ""

    for file in config_path.glob("*.conf"):
        combined_config += file.read_text() + "\n"

    missing_headers = []
    missing_directives = []

    for header in REQUIRED_SECURITY_HEADERS:
        if header not in combined_config:
            missing_headers.append(header)

    for directive in REQUIRED_DIRECTIVES:
        if directive not in combined_config:
            missing_directives.append(directive)

    return {
        "passed": not missing_headers and not missing_directives,
        "missing_headers": missing_headers,
        "missing_directives": missing_directives
    }


if __name__ == "__main__":
    results = validate_nginx_configs()

    if results["passed"]:
        print("PASS: Secure Nginx configuration validated.")
    else:
        print("FAIL: Missing security controls detected.")

        if results["missing_headers"]:
            print("\nMissing Security Headers:")
            for header in results["missing_headers"]:
                print(f"- {header}")

        if results["missing_directives"]:
            print("\nMissing Directives:")
            for directive in results["missing_directives"]:
                print(f"- {directive}")