# Security Policy

## Supported Versions

We currently support the following versions with security updates:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Reporting a Vulnerability

We take the security of Career-bot seriously. If you believe you have found a security vulnerability, please report it to us as described below.

### How to Report

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please send an email to: **guruprasadsa@example.com**

Please include the following information in your report:
- Type of issue (e.g. buffer overflow, SQL injection, cross-site scripting, etc.)
- Full paths of source file(s) related to the manifestation of the issue
- The location of the affected source code (tag/branch/commit or direct URL)
- Any special configuration required to reproduce the issue
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue, including how an attacker might exploit the issue

### What to Expect

After you submit a report, we will:

1. **Acknowledge** your email within 48 hours
2. **Investigate** the issue and determine its impact
3. **Provide** regular updates on our progress
4. **Fix** the issue and release a security update
5. **Publicly acknowledge** your responsible disclosure (if desired)

### Security Update Process

When we receive a security bug report, we will:

1. Confirm the problem and determine the affected versions
2. Audit code to find any potential similar problems
3. Prepare fixes for all releases still under maintenance
4. Release new versions and notify users

## Security Best Practices

When contributing to Career-bot, please follow these security guidelines:

### Backend (Django)
- Never commit secrets or API keys to the repository
- Use environment variables for sensitive configuration
- Validate and sanitize all user inputs
- Use Django's built-in security features
- Keep dependencies up to date

### Frontend (React)
- Sanitize user inputs to prevent XSS attacks
- Use HTTPS for all API communications
- Don't store sensitive data in localStorage
- Validate data received from APIs

### General
- Follow the principle of least privilege
- Use strong authentication mechanisms
- Implement proper error handling
- Log security events appropriately

## Known Security Considerations

### Current Implementation Notes

1. **API Keys**: Ensure all API keys are properly secured in environment variables
2. **Authentication**: The system uses session-based authentication
3. **File Uploads**: Counselor document uploads are stored locally - consider cloud storage for production
4. **CORS**: Currently allows all origins in development - restrict in production
5. **Database**: Uses SQLite for development - use PostgreSQL for production

### Recommended Production Security Measures

1. **HTTPS**: Always use HTTPS in production
2. **Database**: Use a production database with proper access controls
3. **Secrets Management**: Use a proper secrets management service
4. **Rate Limiting**: Implement rate limiting on API endpoints
5. **Input Validation**: Comprehensive input validation and sanitization
6. **File Upload Security**: Implement secure file upload with virus scanning
7. **Regular Updates**: Keep all dependencies updated

## Vulnerability Disclosure Policy

We believe that working with security researchers across the globe is crucial to identifying weaknesses in our technology. If you believe you've found a security issue in our product or service, we encourage you to notify us.

### Guidelines

- Please provide detailed reports with reproducible steps
- If the report is not detailed enough to reproduce the issue, we may ask for additional information
- Please allow reasonable time for us to respond before making any information public
- Make a good faith effort to avoid privacy violations, destruction of data, and interruption or degradation of our service

Thank you for helping keep Career-bot and our users safe!