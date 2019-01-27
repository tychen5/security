contract solved {

    
    //Challenge4
    uint eopXD_blockNumber=3245076;
    bytes32 eopXD_blockhash=0xb388f89fb847890e2d96c9a37c9d25beadef55fb84c2b1b2cf41dc7703bd08f5;
    uint eopXD_timestamp=1526464861;
    function Challenge4_sol () public view returns (uint16) {
        //return (eopXD_blockNumber,blockhash(eopXD_blockNumber));
        return uint16(keccak256(eopXD_blockhash, eopXD_timestamp));
    }
    
    address addr  = 0x9b56a7c72d9782503fa1684ae0fca835c0973638;
    //Challenge5
    function Challenge5_sol() public payable {
        CaptureTheEther guessit = CaptureTheEther(addr);
        uint16 myanswer = uint16(keccak256(block.blockhash(block.number - 1), now));
        guessit.guessRuntimeRandomNumber("r06725035",myanswer);
    }
    
}