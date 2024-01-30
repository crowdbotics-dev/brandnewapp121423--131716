## Django Paypal backend configuration and information

## Module description

This module facilitates integration with the PayPal API, focusing on creating and managing checkout orders as per the PayPal Orders V2 API documentation. It acts as a convenient wrapper around PayPal's Python SDK, offering Django-specific utilities for easier integration within Django projects.

The following are the scope features for this module:
- Create an order
- Capture order payment
- Authorize order payment
- Show order details
- List orders

## Features

- [ ] This module includes migrations.
- [x] This module includes environment variables.
- [ ] This module requires manual configurations.
- [ ] This module can be configured with module options.

## Environment variables

```dotenv
PAYPAL_CLIENT_ID="Your PayPal Client ID",
PAYPAL_CLIENT_SECRET="Your PayPal Client Secret",
PAYPAL_MODE="sandbox" # or 'live' for production use
```

## 3rd party setup

Setup involves configuring your PayPal developer account to obtain the client ID and secret, and determining the environment (sandbox for testing, live for production).

## Dependencies

This setup requires the paypalrestsdk package.

## API details

This module exposes endpoints that map directly to PayPal's Orders V2 API, allowing for actions such as creating, capturing, and authorizing payments for orders, as well as retrieving order details.