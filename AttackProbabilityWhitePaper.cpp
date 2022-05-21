// we consider the scenario of an attacker trying to generate an alternate chain faster than the honest chain. 
// Evern if this is accomplished, it does not throw the system open to arbitrary chages, such as creating value of of thin air or taking money that never belonged to the attacker. 
// Nodes are not going to accept an invalid transaction as payment, and honest nodes will never accept a block containing them . 
// An attacker can only try to change one of his own transactions to take back 
// Money he recently spent. 
// The race between the honest chain and an attacker chain can be characterized as a 
// Binomial Random Walks. The success event is the honest chain being extended by one block, 
// Increasing its lead by +1 and the failure event is the attacker's chain being extended by one block, 
// reducing the gap by -1 
// The probability of an attacker catching up from a given deficit is analogous to a Gambler's Ruin problem. 
// Suppose a gambler with unlimited credit starts at a deficit and plays potentially an 
// infinite number of trails to try to reack breakeven . We can calculate the probability he ever
// reaches breakeven, or that an attacker ever catches up with the honest chain, as follows 
// p = probability an honest node finds the net block 
// q= probability the attacker finds the next block 
// qz = probability the attacker will ever catch up from z blocks behind 
//
// qz = { 1 if p<=q (q/p) exp (z) if p> q} 
// Given our assumptoin that p> q the probability drops exponentially as the number of blocks the attacker has to catch up with increases. 
// With the odds against him, if he doesn't make a lucky lunge forward early on , his chances becomes vanishingly small as he falls further behing. 
// We now conisder how long the recipient of a new transaction needs to wait before bieng sufficiently 
// certain the sender can't change the transaction. we assume the sender is an attacker 
// who wants to make the recipient believe he paid him for a while, then switch it to pay back to 
// himself after some time has passed. 
// The reciever will be alerted when that happens, but the 
// sender hopes it will be too late. 
// lambda = = z qp
//To get the probability the attacker could still catch up now, we multiply the Poisson density for
//each amount of progress he could have made by the probability he could catch up from that point:
//∞ ke−{q/pz−k ifk≤z} ∑k=0 k!⋅ 1 ifkz
//j
//Rearranging to avoid summing the infinite tail of the distribution...
//z ke− z−k 1−∑k=0 k! 1−q/p 

#include<iostream>
#include<math>
double AttackerSuccessProbability ( double q, int z ) 
{
    double p = 1.0 -q;
    double lambda = z*(q/p);
    double sum = 1.0;
    int i,k;
    for(k = 0; k< = z; ++k)
    {
        double poisson = exp (-lambda);
        for (i = 1; i< = k ; i++)
        {
            poisson * = lambda / i;
    
        sum - = poission * (1 - pow (q/p , z-k))}
    }
    return sum ; 
}
int main ()
{
    double q; int z; 
    std::cin >> q >> z; 
    std::cout <<AttackerSuccessProbability( q, z);
    return 0;
}

