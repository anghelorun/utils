#!/bin/bash
TOTAL=$1
SIZE=$2
for i in $(jot $TOTAL)
do 
  CHAVE=$(./genpasswd.sh $SIZE)
  echo "$CHAVE MD5: $(echo $CHAVE|md5)"
  echo "$CHAVE SHA1: $(echo $CHAVE|shasum)"
  echo "$CHAVE SHA1-256: $(echo $CHAVE|shasum -a 256)"
  echo "$CHAVE SHA1-512: $(echo $CHAVE|shasum -a 512)"
done

