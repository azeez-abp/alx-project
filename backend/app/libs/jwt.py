import jwt  # type: ignore
from cryptography.hazmat.primitives import serialization  # type: ignore
from app import root_folder


def encodes_(user_id: str, email: str) -> str:

    payload_data = {
        "id": user_id,
        "email": email,
    }

    # my_secret = getenv("SECRET")
    paths = f'{root_folder}app\\libs\\.ssh\\id_rsa'
    private_key = open(paths,  'r').read()
    key = serialization.load_ssh_private_key(private_key.encode(),
                                             password=b'abp')
    token = jwt.encode(
        payload=payload_data,
        key=key,
        algorithm='RS256'
    )

    return token




def decode_(token):
    paths = f'{root_folder}app\\libs\\.ssh\\id_rsa.pub'
    public_key = open(paths,  'r').read()
    # key = serialization.load_ssh_private_key(public_key.encode(),
    #                                          password=b'abp')
    key = serialization.load_ssh_public_key(public_key.encode())

    data  = jwt.decode(jwt=token, key=key, algorithms=['RS256', ])

    print(data)