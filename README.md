# symmetric-secure-chat
A Python socket chat application demonstrating symmetric encryption and shared-key cryptography.
# Symmetric Secure Chat

A high-performance, secure client-server chat application built from scratch utilizing Python sockets and end-to-end symmetric encryption (AES). This project demonstrates the core fundamentals of network programming, shared-key cryptography, and high-throughput secure data transfer.

---

## Security Disclaimer
> **IMPORTANT:** This repository is created strictly for educational, research, and portfolio purposes. The cryptographic implementations contained herein are intended to demonstrate concepts of symmetric encryption and network communication under laboratory conditions. Do not deploy this software in untrusted or production environments.

---

## Features
* **Symmetric Encryption (AES):** Leverages strong symmetric ciphers (like AES-GCM or AES-CBC) for fast and secure data encryption and decryption using a pre-shared key.
* **High Throughput & Performance:** Demonstrates why symmetric cryptography is the industry standard for encrypting actual data payloads due to its low computational overhead.
* **Socket-Based Architecture:** Low-level network communication implemented via Python's standard `socket` and `threading` libraries to handle multiple concurrent connections.
* **Encrypted Payload:** All messages traveling through the server are fully encrypted; the server acts as a blind relay with zero knowledge of the plaintext content.

---

## Architecture & Data Flow

Symmetric encryption relies on a **Shared Secret** (the same key is used for both encryption and decryption). Below is the conceptual overview of the message relay:

[ Client A ]                              [ Server ]                              [ Client B ]
|                                         |                                       |
| -- [Possesses Pre-Shared Key]           |           [Possesses Pre-Shared Key]--|
|                                         |                                       |
| ---- 1. Encrypt msg with AES Key ------> |                                       |
|         (Plaintext -> Ciphertext)       |                                       |
|                                         | ---- 2. Relay Ciphertext (Raw bytes) ->|
|                                         |                                       |
|                                         |                                       | [ 3. Decrypts with ]
|                                         |                                       | [ identical AES Key]

---

## Tech Stack
* **Language:** Python 3.x
* **Core Modules:** `socket`, `threading`
* **Cryptography:** `cryptography` 
