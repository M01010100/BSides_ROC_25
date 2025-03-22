from Crypto.Cipher import AES


open('flag.png.enc', 'wb').write(
    AES.new(b"sup3rrr s3cr3ttt").decrypt(open('flag.png', 'rb').read())
)