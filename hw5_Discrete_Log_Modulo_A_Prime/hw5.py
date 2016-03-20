import gmpy2
from gmpy2 import mpz
#gmpy2.get_context().precision = 1100
def mypowmod(a, b, N):
    ret = 1
    while b > 0:
        if b & 1 == 1:
            ret = gmpy2.mul(ret,a)
            ret = gmpy2.f_mod(ret,N)
        a = gmpy2.mul(a,a)
        a = gmpy2.f_mod(a,N)
        b = b >> 1
    return gmpy2.f_mod(ret,N)
p=13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171
g=11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568
h=3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333
B=1<<20
h_g=dict()
for x1 in range(0,B+1):
    g_x1=mypowmod(g,x1,p)
    _g_x1=gmpy2.divm(1,g_x1,p)
    h_gx1=gmpy2.mul(h,_g_x1)
    h_gx1=gmpy2.f_mod(h_gx1,p)
    h_g[h_gx1]=x1

g_B=mypowmod(g,B,p)


for x0 in range(0,B+1):
    gB_x0=mypowmod(g_B,x0,p)
    if gB_x0 in h_g:
        x1=h_g[gB_x0]
        print x0, x1
        x0_B=gmpy2.mul(B,x0)
        print gmpy2.add(x0_B,x1)
        break
