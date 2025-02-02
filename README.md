# Blockchain Portal - Automated Testing Suite

## Overview
This repository contains an automated testing suite for the [Blockchain Portal](https://xaltsocnportal.web.app), a CRUD web application that allows users to create requests to add nodes to a common blockchain or initiate requests to create new private blockchains. The tests ensure the robustness, reliability, and security of user interactions within the portal.

## Features Tested
The test suite covers the following core functionalities:

1. **Sign Up** - Creating a new account with an email ID and password.
2. **Sign In** - Logging in with an existing account.
3. **Submit Request to Onboard Nodes to an Existing Blockchain**:
   - Adding node details (Node ID and Public IP)
   - Adding wallet details (Wallet address and permission type)
   - Reviewing and submitting the request
4. **Submit Request to Create a New Private Blockchain**:
   - Providing network details
   - Adding nodes and wallets
   - Reviewing and submitting the request
5. **Sign Out** - Logging out securely from the system.

## Installation & Setup
### Prerequisites
- Python 3.7+
- Selenium WebDriver
- PyTest
- Google Chrome & ChromeDriver (for Selenium)

## Test Plan
This test suite includes:
### 1. Functional Testing
- **Sign Up**: Valid and invalid credentials, email format validation, password constraints.
- **Sign In**: Correct and incorrect credentials, account lockout scenarios.
- **Sign Out**: Ensuring session termination and restricted access post-logout.

### 2. UI Testing
- Validating the presence and functionality of form elements, buttons, and navigation.

### 3. API Testing
- Verifying backend responses for sign-up, sign-in, and request submissions.

### 4. Performance Testing
- Load testing sign-up and sign-in functionality.

## Reporting Bugs & Issues
If you encounter any issues, feel free to create an issue on this repository with:
- Steps to reproduce
- Expected vs actual results
- Screenshots (if applicable)

## Contributors
- **Indulekha Mahilamoni**

## License
This project is licensed under the MIT License.

