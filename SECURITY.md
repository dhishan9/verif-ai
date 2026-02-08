# Security Policy

## Supported Versions
The following versions of Verif-AI are currently supported for security updates:

| Version | Supported |
| ------- | --------- |
| 1.0.x   | Yes       |
| < 1.0   | No        |

## Reporting a Vulnerability
If you discover a security vulnerability in Verif-AI, please do not disclose it publicly. 

Instead, report it responsibly by:
- Opening a Private Vulnerability Report on GitHub.
- Contacting the maintainers through the repository's official communication channels.

## Scope
This project is provided for educational and research purposes. 
While we aim to follow industry best practices, no absolute security guarantees are provided.

> [!CAUTION]
> **Security Warning regarding model.pkl**
>
> This project uses Python's `pickle` module to load machine learning model weights. 
> 
> **Never load a .pkl file from an untrusted or unknown source.** > A maliciously crafted pickle file can execute arbitrary code on your system during the loading process (`pickle.load()`).
>  Only use the `model.pkl` provided in this official repository or weights you have generated yourself using the `train_model.py` script.

We appreciate responsible disclosure and community efforts to keep this project secure.
