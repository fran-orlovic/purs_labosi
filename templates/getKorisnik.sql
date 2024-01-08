SELECT * FROM korisnik WHERE
password = UNHEX(SHA2('{{passwd}}', 256))
AND username = '{{user}}';