# ACME HTTP-01 Challenge Support

This Django project includes support for ACME HTTP-01 challenges, which are used by Let's Encrypt and other Certificate Authorities for domain validation during SSL certificate issuance.

## Implementation

### View Function
- **Location**: `devsearch/views.py`
- **Function**: `acme_challenge(request, token)`
- **Purpose**: Serves ACME challenge files from `/opt/portfolio-project/devsearch/staticfiles/.well-known/acme-challenge/`

### URL Configuration
- **Pattern**: `/.well-known/acme-challenge/<str:token>`
- **Location**: `devsearch/urls.py`
- **Name**: `acme_challenge`

### Directory Structure
The ACME challenge files should be placed in:
```
/opt/portfolio-project/devsearch/staticfiles/.well-known/acme-challenge/
```

## Security Features

- **Path Traversal Protection**: The view prevents access to files outside the ACME challenge directory
- **File Validation**: Only files that exist and are readable are served
- **Content Type**: Files are served with `text/plain` content type as required by ACME specification

## Usage

When Let's Encrypt needs to validate domain ownership, it will:

1. Request a specific URL like: `http://yourdomain.com/.well-known/acme-challenge/TOKEN`
2. The Django view will look for the file at: `/opt/portfolio-project/devsearch/staticfiles/.well-known/acme-challenge/TOKEN`
3. If found, the file contents are returned with `text/plain` content type
4. If not found or inaccessible, a 404 error is returned

## Testing

To test the functionality:

1. Create a test file in the ACME challenge directory
2. Access the URL `/.well-known/acme-challenge/filename`
3. Verify the file contents are returned

Example:
```bash
# Create test file
echo "test-content" > /opt/portfolio-project/devsearch/staticfiles/.well-known/acme-challenge/test-token

# Test endpoint
curl http://yourdomain.com/.well-known/acme-challenge/test-token
```