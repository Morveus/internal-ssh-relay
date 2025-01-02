# SSH Command Executor

A containerized Flask server that executes remote SSH commands using sshpass. This server is designed for controlled environments where SSH key validation is not required.

## 🚨 Security Notice

This application deliberately disables SSH security features and uses password authentication. It is intended **only** for controlled environments and should not be used in production or exposed to the public internet.

## 🚀 Quick Start

### Prerequisites

- Docker installed on your system
- Remote SSH server details (hostname, username, password)

### How to use

Run the docker image
```
docker run -d -p 5000:5000 --name ssh-command-executor morveus/internal-ssh-relay
```

Call the service to relay commands to SSH servers

```
curl -X POST http://localhost:4567/execute \
        -H "Content-Type: application/json" \
        -d '{
    "ssh_host": "10.11.12.13",
    "ssh_user": "user",
    "ssh_password": "password",
    "command": "reboot"
    }'
```