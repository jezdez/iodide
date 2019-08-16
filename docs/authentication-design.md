The Iodide authentication system is designed to support two use cases:
an internal system for use by organizations (e.g. Mozilla) and a public web
site. In either case, it is chiefly designed to delegate authentication and
identity access for users to trusted third parties -- Iodide does not hold or
manage any credentials itself.

In the case of a public facing system, no permissions or authentication are
required to *view* any resource provided the API. This currently includes
lists of notebooks, notebooks themselves (and their revisions), and files.
Write access is currently limited to the user which created the resource.

On an internal system, read access is also limited to those users with
an authenticated session and/or authentication token.

There are three ways a user may identify themselves to the Iodide system:

* Session-based authentication
* JWT-token based authentication
* AuthToken-based authentication

## Session-based authentication

This is based on [Django's authentication
system](https://docs.djangoproject.com/en/2.2/topics/auth/).  Currently there
are two options for this system of authentication: Github authentication (via
the django social authentication system) and OpenIDC (via an internal set of
openidc middleware).

### GitHub authentication

GitHub authentication is fairly straightforward, simply using the existing
facilities provided by [python social auth](https://python-social-auth.readthedocs.io/en/latest/).
Configuration on the server may be accomplished simply by [specifying
environment variables](server-admin-overview.md#important-configuration-variables) corresponding to a GitHub key and secret.

### OpenIDC

If using OpenIDC, it is assumed that a web server fronting the Django
system will authenticate any request coming in and provide an HTTP
header to identify the user (`HTTP_X_FORWARDED_USER`).

By default, Mozilla's OpenIDC service will expire a user's session after
a short period of inactivity. To allow an Iodide notebook to continue
to access the API (e.g. to allow the user to continue saving their changes),
as well as allowing headless services to access the iodide server, if
OpenIDC is configured you may specify a set of regular expressions (via the
`OPENIDC_AUTH_WHITELIST` configuration variable) where this checking is
skipped, and we fall back to the jwt and/or authtoken middleware (which has
its own expiry and renewal policy). By default just `/api/` is included.

It is critical that you do not leave any endpoints open without
authentication and specification in the `OPENIDC_AUTH_WHITELIST`, as this will
allow any client to arbitrarily create any number of users on the system.

## JWT-token based authentication

JWT-based authentication is based on the Django Rest Framework [simple jwt
plugin](https://github.com/davesque/django-rest-framework-simplejwt/). The
basic model is to allow a client to get a JWT token via session authentication
(via the `/token/` endpoint) and thereafter use JWT to identify to any
endpoint server under `/api/`.

## AuthToken-based authentication

This is yet another alternative, currently designed to support the use case of
a 3rd party service being able to create iodide notebooks. This allows
authentication using a unique key (secret) generated by an administrator on
the Iodide server. Internally, this is implemented through Django Rest
Framework's
[TokenAuthentication](https://www.django-rest-framework.org/topics/api-clients/#token-authentication_1)
class. Usage is documented in the [common server
tasks](common-server-tasks.md) section.