# This file was automatically created by FeynRules 2.0.6
# Mathematica version: 8.0 for Linux x86 (64-bit) (October 10, 2011)
# Date: Tue 7 Apr 2015 19:45:59



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

lam1Norm = Parameter(name = 'lam1Norm',
                     nature = 'external',
                     type = 'real',
                     value = 0.1,
                     texname = '\\text{$\\lambda $1Norm}',
                     lhablock = 'NP',
                     lhacode = [ 1 ])

lam2Norm = Parameter(name = 'lam2Norm',
                     nature = 'external',
                     type = 'real',
                     value = 0.1,
                     texname = '\\text{$\\lambda $2Norm}',
                     lhablock = 'NP',
                     lhacode = [ 2 ])

lam2Left = Parameter(name = 'lam2Left',
                     nature = 'external',
                     type = 'real',
                     value = 0.1,
                     texname = '\\text{$\\lambda $2Left}',
                     lhablock = 'NP',
                     lhacode = [ 3 ])

lam1R111 = Parameter(name = 'lam1R111',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\lambda $1R111}',
                     lhablock = 'NP',
                     lhacode = [ 4 ])

lam1R112 = Parameter(name = 'lam1R112',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{$\\lambda $1R112}',
                     lhablock = 'NP',
                     lhacode = [ 5 ])

lam1R113 = Parameter(name = 'lam1R113',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{$\\lambda $1R113}',
                     lhablock = 'NP',
                     lhacode = [ 6 ])

lam1R121 = Parameter(name = 'lam1R121',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\lambda $1R121}',
                     lhablock = 'NP',
                     lhacode = [ 7 ])

lam1R122 = Parameter(name = 'lam1R122',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\lambda $1R122}',
                     lhablock = 'NP',
                     lhacode = [ 8 ])

lam1R123 = Parameter(name = 'lam1R123',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{$\\lambda $1R123}',
                     lhablock = 'NP',
                     lhacode = [ 9 ])

lam1R131 = Parameter(name = 'lam1R131',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\lambda $1R131}',
                     lhablock = 'NP',
                     lhacode = [ 10 ])

lam1R132 = Parameter(name = 'lam1R132',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\lambda $1R132}',
                     lhablock = 'NP',
                     lhacode = [ 11 ])

lam1R133 = Parameter(name = 'lam1R133',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\lambda $1R133}',
                     lhablock = 'NP',
                     lhacode = [ 12 ])

lam1R211 = Parameter(name = 'lam1R211',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\lambda $1R211}',
                     lhablock = 'NP',
                     lhacode = [ 13 ])

lam1R212 = Parameter(name = 'lam1R212',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{$\\lambda $1R212}',
                     lhablock = 'NP',
                     lhacode = [ 14 ])

lam1R213 = Parameter(name = 'lam1R213',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{$\\lambda $1R213}',
                     lhablock = 'NP',
                     lhacode = [ 15 ])

lam1R221 = Parameter(name = 'lam1R221',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\lambda $1R221}',
                     lhablock = 'NP',
                     lhacode = [ 16 ])

lam1R222 = Parameter(name = 'lam1R222',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\lambda $1R222}',
                     lhablock = 'NP',
                     lhacode = [ 17 ])

lam1R223 = Parameter(name = 'lam1R223',
                     nature = 'external',
                     type = 'real',
                     value = 1,
                     texname = '\\text{$\\lambda $1R223}',
                     lhablock = 'NP',
                     lhacode = [ 18 ])

lam1R231 = Parameter(name = 'lam1R231',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\lambda $1R231}',
                     lhablock = 'NP',
                     lhacode = [ 19 ])

lam1R232 = Parameter(name = 'lam1R232',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\lambda $1R232}',
                     lhablock = 'NP',
                     lhacode = [ 20 ])

lam1R233 = Parameter(name = 'lam1R233',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\lambda $1R233}',
                     lhablock = 'NP',
                     lhacode = [ 21 ])

lam1I111 = Parameter(name = 'lam1I111',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\lambda $1I111}',
                     lhablock = 'NP',
                     lhacode = [ 22 ])

lam1I112 = Parameter(name = 'lam1I112',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\lambda $1I112}',
                     lhablock = 'NP',
                     lhacode = [ 23 ])

lam1I113 = Parameter(name = 'lam1I113',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\lambda $1I113}',
                     lhablock = 'NP',
                     lhacode = [ 24 ])

lam1I121 = Parameter(name = 'lam1I121',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\lambda $1I121}',
                     lhablock = 'NP',
                     lhacode = [ 25 ])

lam1I122 = Parameter(name = 'lam1I122',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\lambda $1I122}',
                     lhablock = 'NP',
                     lhacode = [ 26 ])

lam1I123 = Parameter(name = 'lam1I123',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\lambda $1I123}',
                     lhablock = 'NP',
                     lhacode = [ 27 ])

lam1I131 = Parameter(name = 'lam1I131',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\lambda $1I131}',
                     lhablock = 'NP',
                     lhacode = [ 28 ])

lam1I132 = Parameter(name = 'lam1I132',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\lambda $1I132}',
                     lhablock = 'NP',
                     lhacode = [ 29 ])

lam1I133 = Parameter(name = 'lam1I133',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\lambda $1I133}',
                     lhablock = 'NP',
                     lhacode = [ 30 ])

lam1I211 = Parameter(name = 'lam1I211',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\lambda $1I211}',
                     lhablock = 'NP',
                     lhacode = [ 31 ])

lam1I212 = Parameter(name = 'lam1I212',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\lambda $1I212}',
                     lhablock = 'NP',
                     lhacode = [ 32 ])

lam1I213 = Parameter(name = 'lam1I213',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\lambda $1I213}',
                     lhablock = 'NP',
                     lhacode = [ 33 ])

lam1I221 = Parameter(name = 'lam1I221',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\lambda $1I221}',
                     lhablock = 'NP',
                     lhacode = [ 34 ])

lam1I222 = Parameter(name = 'lam1I222',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\lambda $1I222}',
                     lhablock = 'NP',
                     lhacode = [ 35 ])

lam1I223 = Parameter(name = 'lam1I223',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\lambda $1I223}',
                     lhablock = 'NP',
                     lhacode = [ 36 ])

lam1I231 = Parameter(name = 'lam1I231',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\lambda $1I231}',
                     lhablock = 'NP',
                     lhacode = [ 37 ])

lam1I232 = Parameter(name = 'lam1I232',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\lambda $1I232}',
                     lhablock = 'NP',
                     lhacode = [ 38 ])

lam1I233 = Parameter(name = 'lam1I233',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\lambda $1I233}',
                     lhablock = 'NP',
                     lhacode = [ 39 ])

lam2R11 = Parameter(name = 'lam2R11',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{$\\lambda $2R11}',
                    lhablock = 'NP',
                    lhacode = [ 40 ])

lam2R12 = Parameter(name = 'lam2R12',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{$\\lambda $2R12}',
                    lhablock = 'NP',
                    lhacode = [ 41 ])

lam2R13 = Parameter(name = 'lam2R13',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{$\\lambda $2R13}',
                    lhablock = 'NP',
                    lhacode = [ 42 ])

lam2R21 = Parameter(name = 'lam2R21',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{$\\lambda $2R21}',
                    lhablock = 'NP',
                    lhacode = [ 43 ])

lam2R22 = Parameter(name = 'lam2R22',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{$\\lambda $2R22}',
                    lhablock = 'NP',
                    lhacode = [ 44 ])

lam2R23 = Parameter(name = 'lam2R23',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{$\\lambda $2R23}',
                    lhablock = 'NP',
                    lhacode = [ 45 ])

lam2I11 = Parameter(name = 'lam2I11',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{$\\lambda $2I11}',
                    lhablock = 'NP',
                    lhacode = [ 46 ])

lam2I12 = Parameter(name = 'lam2I12',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{$\\lambda $2I12}',
                    lhablock = 'NP',
                    lhacode = [ 47 ])

lam2I13 = Parameter(name = 'lam2I13',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{$\\lambda $2I13}',
                    lhablock = 'NP',
                    lhacode = [ 48 ])

lam2I21 = Parameter(name = 'lam2I21',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{$\\lambda $2I21}',
                    lhablock = 'NP',
                    lhacode = [ 49 ])

lam2I22 = Parameter(name = 'lam2I22',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{$\\lambda $2I22}',
                    lhablock = 'NP',
                    lhacode = [ 50 ])

lam2I23 = Parameter(name = 'lam2I23',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{$\\lambda $2I23}',
                    lhablock = 'NP',
                    lhacode = [ 51 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

Mn = Parameter(name = 'Mn',
               nature = 'external',
               type = 'real',
               value = 1,
               texname = '\\text{Mn}',
               lhablock = 'MASS',
               lhacode = [ 5000001 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 120,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MX1 = Parameter(name = 'MX1',
                nature = 'external',
                type = 'real',
                value = 1000,
                texname = '\\text{MX1}',
                lhablock = 'MASS',
                lhacode = [ 6000001 ])

MX2 = Parameter(name = 'MX2',
                nature = 'external',
                type = 'real',
                value = 2000,
                texname = '\\text{MX2}',
                lhablock = 'MASS',
                lhacode = [ 6000002 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00575308848,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WX1 = Parameter(name = 'WX1',
                nature = 'external',
                type = 'real',
                value = 5.,
                texname = '\\text{WX1}',
                lhablock = 'DECAY',
                lhacode = [ 6000001 ])

WX2 = Parameter(name = 'WX2',
                nature = 'external',
                type = 'real',
                value = 50,
                texname = '\\text{WX2}',
                lhablock = 'DECAY',
                lhacode = [ 6000002 ])

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.sin(cabi)',
                   texname = '\\text{CKM1x2}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-cmath.sin(cabi)',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM2x2}')

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

Lam11x1x1 = Parameter(name = 'Lam11x1x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'complex(0,1)*lam1I111 + lam1R111',
                      texname = '\\text{Lam11x1x1}')

Lam11x1x2 = Parameter(name = 'Lam11x1x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'complex(0,1)*lam1I112 + lam1R112',
                      texname = '\\text{Lam11x1x2}')

Lam11x1x3 = Parameter(name = 'Lam11x1x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'complex(0,1)*lam1I113 + lam1R113',
                      texname = '\\text{Lam11x1x3}')

Lam11x2x1 = Parameter(name = 'Lam11x2x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'complex(0,1)*lam1I121 + lam1R121',
                      texname = '\\text{Lam11x2x1}')

Lam11x2x2 = Parameter(name = 'Lam11x2x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'complex(0,1)*lam1I122 + lam1R122',
                      texname = '\\text{Lam11x2x2}')

Lam11x2x3 = Parameter(name = 'Lam11x2x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'complex(0,1)*lam1I123 + lam1R123',
                      texname = '\\text{Lam11x2x3}')

Lam11x3x1 = Parameter(name = 'Lam11x3x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'complex(0,1)*lam1I131 + lam1R131',
                      texname = '\\text{Lam11x3x1}')

Lam11x3x2 = Parameter(name = 'Lam11x3x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'complex(0,1)*lam1I132 + lam1R132',
                      texname = '\\text{Lam11x3x2}')

Lam11x3x3 = Parameter(name = 'Lam11x3x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'complex(0,1)*lam1I133 + lam1R133',
                      texname = '\\text{Lam11x3x3}')

Lam12x1x1 = Parameter(name = 'Lam12x1x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'complex(0,1)*lam1I211 + lam1R211',
                      texname = '\\text{Lam12x1x1}')

Lam12x1x2 = Parameter(name = 'Lam12x1x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'complex(0,1)*lam1I212 + lam1R212',
                      texname = '\\text{Lam12x1x2}')

Lam12x1x3 = Parameter(name = 'Lam12x1x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'complex(0,1)*lam1I213 + lam1R213',
                      texname = '\\text{Lam12x1x3}')

Lam12x2x1 = Parameter(name = 'Lam12x2x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'complex(0,1)*lam1I221 + lam1R221',
                      texname = '\\text{Lam12x2x1}')

Lam12x2x2 = Parameter(name = 'Lam12x2x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'complex(0,1)*lam1I222 + lam1R222',
                      texname = '\\text{Lam12x2x2}')

Lam12x2x3 = Parameter(name = 'Lam12x2x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'complex(0,1)*lam1I223 + lam1R223',
                      texname = '\\text{Lam12x2x3}')

Lam12x3x1 = Parameter(name = 'Lam12x3x1',
                      nature = 'internal',
                      type = 'complex',
                      value = 'complex(0,1)*lam1I231 + lam1R231',
                      texname = '\\text{Lam12x3x1}')

Lam12x3x2 = Parameter(name = 'Lam12x3x2',
                      nature = 'internal',
                      type = 'complex',
                      value = 'complex(0,1)*lam1I232 + lam1R232',
                      texname = '\\text{Lam12x3x2}')

Lam12x3x3 = Parameter(name = 'Lam12x3x3',
                      nature = 'internal',
                      type = 'complex',
                      value = 'complex(0,1)*lam1I233 + lam1R233',
                      texname = '\\text{Lam12x3x3}')

Lam21x1 = Parameter(name = 'Lam21x1',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complex(0,1)*lam2I11 + lam2R11',
                    texname = '\\text{Lam21x1}')

Lam21x2 = Parameter(name = 'Lam21x2',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complex(0,1)*lam2I12 + lam2R12',
                    texname = '\\text{Lam21x2}')

Lam21x3 = Parameter(name = 'Lam21x3',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complex(0,1)*lam2I13 + lam2R13',
                    texname = '\\text{Lam21x3}')

Lam22x1 = Parameter(name = 'Lam22x1',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complex(0,1)*lam2I21 + lam2R21',
                    texname = '\\text{Lam22x1}')

Lam22x2 = Parameter(name = 'Lam22x2',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complex(0,1)*lam2I22 + lam2R22',
                    texname = '\\text{Lam22x2}')

Lam22x3 = Parameter(name = 'Lam22x3',
                    nature = 'internal',
                    type = 'complex',
                    value = 'complex(0,1)*lam2I23 + lam2R23',
                    texname = '\\text{Lam22x3}')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

