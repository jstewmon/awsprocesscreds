'''
Entrypoint for pyinstaller packaging.

1. python3 -m venv .venv
2. source ./venv/bin/activate
3. pip install . && pip install pyinstaller
4. pyinstaller --name awsprocesscreds-saml pyinstaller-entrypoint.py
5. (cd dist && zip -r awsprocesscreds-saml .)
6. distribute zip
7. unzip -d /usr/local/lib awsprocesscreds-saml.zip
8. ln -s /usr/local/lib/awsprocesscreds-saml/awsprocesscreds-saml /usr/local/bin/
'''

from awsprocesscreds.cli import saml
if __name__ == '__main__':
    saml()
