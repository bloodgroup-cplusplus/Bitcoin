#ifndef BITCOIN_RANDOM_H
#define BITCOIN_RANDOM_H

#include "uint256.h"
#include <stdint.h>

/**
 * Seed openSSl PRNG with additonal entropy data 
 */

void RandAddSeed();
void RandAddSeedPerfmon();


/**
 * Functions to gather random data via the OpenSSL PRNG
 */

void GetRandBytes(unsigned char * buf, int num);
uint64_t GetRand(uint64_t nMax);
int GetRandInt(int nMax);
uint256 GetRandHash();

/**
 * Seed insecure_rand uisng the random pool.
 * @param Deterministic Use a deterministic seed
 */
void seed_insecure_rand(bool fDeterministic = false);

/**
 * MWC RNG of GEorge Marsaglia
 * This is intended to be fast.  It has period of 2^59.3 ,though the 
 * least significant 16 bits only have a period of about 2^30.1
 * @return random value 
 */

extern uint32_t insecure_rand_Rz;
extern uint32_t insecure_rand_Rw;
static inline uint32_t insecure_rand(void)
{
    insecure_rand_Rz = 36969 & * (insecure_rand_Rz & 65535_
