from Crypto.Util.number import long_to_bytes

def inverse_mod(a, m):
    # Extended Euclidean Algorithm to find modular inverse
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def recover_flag(n, e, c):
    # Compute Euler's totient function of n
    phi_n = n - 1
    # Compute the modular inverse of e mod phi_n
    d = inverse_mod(e, phi_n)
    # Decrypt the ciphertext c to recover the plaintext flag
    flag = pow(c, d, n)
    return long_to_bytes(flag)

# Given values
n = 22914764349697556963541692665721076425490063991574936243571428156261302060328685591556514036751777776065771167330244010708082147401402002914377904950080486799957005111360365028092884367373338454223568447811216200859660057226322801828334633020895296785582519610777820724907394060126570265818769159991752144783469338557691407102432786644694590118176582000965124360500257946304028767088296724907062561163478654995994205065812479605136088813543435895840276066683243706020091519857275219422246006137390619897086478975872204136389082598585864385077220265194919486850918633328368814287347732293510186569121425821644289329813
e = 65537
c = 11189917160698738647911433493693285101538131455035611550077950709107429331298329502327358588774261161674422351739941120882289954400477590502272629693853242116507000433761914368814656180874783594812260498542390500221519883099478550863172147588922341571443502449435143090576514228274833316274013491937919397957017546671325357027765817692571583998487352090789855980131184451611087822399088669705683765370510052781742383736278295296012267794429263720509724794426552010741678342838319060084074826713065120930332229122961216786019982413982114571551833129932338204333681414465713448112309599140515483842800125894387412148599

# Recover the flag
flag = recover_flag(n, e, c)
print("Flag:", flag.decode())
