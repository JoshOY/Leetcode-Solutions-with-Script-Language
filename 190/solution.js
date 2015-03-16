/*
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).
*/

var reverseBits = function(n) {
	var zeros = [];
	for (var i = 0; i < 32 - n.toString(2).length; i++) {
		zeros = zeros.concat([0]);
	}
	return parseInt(n.toString(2).split("").reverse().concat(zeros).join(""), 2);
}

console.log(reverseBits(43261596));