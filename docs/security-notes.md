# Security Notes — Secure Nginx Reverse Proxy Lab

## Overview

This project simulates a hardened Nginx reverse proxy deployment commonly used in modern DevSecOps and cloud-native environments.

The lab focuses on:

- reverse proxy security
- TLS/SSL enforcement
- secure HTTP configuration
- attack surface reduction
- backend application protection
- Layer 7 traffic handling

---

# Reverse Proxy Architecture

Client requests flow through Nginx before reaching the backend Flask application.

```text
Client
   ↓
Nginx Reverse Proxy
   ↓
Flask Backend Application