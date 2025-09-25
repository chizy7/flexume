# Security Policy

## Supported Versions

We release patches for security vulnerabilities in the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

The Flexume team takes security bugs seriously. We appreciate your efforts to responsibly disclose your findings, and will make every effort to acknowledge your contributions.

### How to Report a Security Vulnerability

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them via one of the following methods:

1. **Email**: Send details to [chizy@chizyhub.com](mailto:chizy@chizyhub.com)
2. **GitHub Security Advisories**: Use GitHub's private vulnerability reporting feature by going to the [Security tab](https://github.com/chizy7/flexume/security/advisories/new) in our repository
3. **Direct Contact**: Reach out to the maintainers directly:
   - Chizy: [@chizy7](https://github.com/chizy7) or [@Chizyization](https://x.com/Chizyization)
   - Rumeza: [@rumezaa](https://github.com/rumezaa) or [@rumezaft](https://x.com/rumezaft)

### What to Include

When reporting a vulnerability, please include:

- Type of issue (e.g., buffer overflow, SQL injection, cross-site scripting, etc.)
- Full paths of source file(s) related to the manifestation of the issue
- The location of the affected source code (tag/branch/commit or direct URL)
- Any special configuration required to reproduce the issue
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue, including how an attacker might exploit it

### Response Timeline

- **Acknowledgment**: We will acknowledge receipt of your vulnerability report within 48 hours
- **Initial Assessment**: We will provide an initial assessment within 5 business days
- **Updates**: We will keep you informed of our progress throughout the investigation
- **Resolution**: We aim to resolve critical vulnerabilities within 90 days

### Disclosure Policy

- We follow coordinated disclosure principles
- Security vulnerabilities will be disclosed publicly only after:
  - A fix has been developed and tested
  - The fix has been released
  - Sufficient time has passed for users to update (typically 2 weeks)

### Security Best Practices for Contributors

When contributing to Flexume, please follow these security guidelines:

#### Data Handling
- Never log or store sensitive user data (resume content, personal information)
- Implement proper data sanitization for all user inputs
- Use secure file upload practices with proper validation

#### AI/ML Security
- Validate all inputs to AI models
- Implement rate limiting for AI-powered features
- Sanitize responses from AI models before displaying to users

#### Dependencies
- Keep all dependencies up to date
- Run security audits regularly (`pip audit`, `safety check`)
- Use dependabot for automated security updates

#### Code Quality
- Follow secure coding practices
- Use static analysis tools to catch potential security issues
- Implement proper error handling without exposing system details

### Vulnerability Disclosure Recognition

We believe in giving credit where credit is due. Security researchers who responsibly report vulnerabilities will be:

- Acknowledged in our security advisories (unless you prefer to remain anonymous)
- Listed in our `CONTRIBUTING.md` file under a security researchers section
- Mentioned in release notes when the vulnerability is patched

### Security-Related Configuration

For users deploying Flexume:

- Always use HTTPS in production
- Keep your Python environment and dependencies updated
- Use environment variables for sensitive configuration
- Implement proper access controls and authentication
- Regular backup and recovery procedures
- Monitor logs for suspicious activity

### Known Security Considerations

As an AI-powered resume analysis tool, Flexume handles potentially sensitive data:

- **Resume Content**: Contains personal and professional information
- **AI Processing**: Resume data is processed by AI models
- **File Uploads**: Users upload documents that need secure handling
- **Conversational Data**: Chat history may contain sensitive context

We are committed to implementing robust security measures to protect user data throughout the application lifecycle.

### Security Updates

Security updates and advisories will be published:
- On our [GitHub Security Advisories](https://github.com/chizy7/flexume/security/advisories) page
- In our release notes
- Via our communication channels

---

Thank you for helping keep Flexume and our users safe!