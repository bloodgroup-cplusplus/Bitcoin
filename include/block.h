#ifndef BITCOIN_PRIMITIVES_BLOCK_H
#define BITCOIN_PRIMITIVES_BLOCK_H


#include "primitives/transaction.h"
#include "serialize.h"
#include "uint256.h"


/** Nodes collect new transactions into a block, has them into a hash tree, 
 * and scan through nonce values to make the blocks' hash satisfy proof-of-work requirements. 
 * Whey they solve the proof-of-work, they broadcast the block to every one and the block is added to the block chain . 
 * The first transaction in the block is  a special one that creates a new coin owned by the createor fo th block 
 */

class CBlockHeader
{
    public : 
        //header 
        static const int32_t CURRENT_VERSION = 3; 
        int32_t nVersion ; 
        uint256 hashPrevBlock ; 
        uint256 hashMerkleRoot;
        uint32_t nTime;
        uint32_t nBits;
        uint32_t nNonce;

    CBlockHeader()
    {
        SetNull();
    }

    ADD_SERIALIZE_METHODS;

    template<typename Stream, typename Operation >

    inline void SerializationOp(Stream & os, Operation ser_action, int nType, int nVersion )
    {
        READWRITE(this->nversion);
        nVersoin = (this->nVersion);
        READWRITE(hashPrevBlock);
        READWRITE(hashMerkleRoot);
        READWRITE(nTime);
        READWRITE(nBits);
        READWRITE(nNonce);
    }


    void SetNull()
    {
        nVersion = CBlockHeader::CURRENT_VERSION ;




