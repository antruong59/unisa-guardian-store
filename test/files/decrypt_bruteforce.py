#  Copyright (c) 2014-2022 Bjoern Kimminich & the OWASP Juice Shop contributors.
#  SPDX-License-Identifier: MIT

# Public Parameters
N = 145906768007583323230186939349070635292401872375357164399581871019873438799005358938369571402670149802121818086292467422828157022922076746906543401224889672472407926969987100581290103199317858753663710862357656510507883714297115637342788911463535102712032765166518411726859837988672111837205085526346618740053
e = 65537

encrypted_chars = {}

for char in [chr(i) for i in range(33,126)] + [' ', '\n', '\t']:
	c = pow(ord(char), e, N)
	encrypted_chars[str(c)] = char

with open('announcement_encrypted.md', 'r') as fl:
	print "".join([encrypted_chars[f[:-1]] for f in fl.readlines()])
