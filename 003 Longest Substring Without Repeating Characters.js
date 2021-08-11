/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    var i = 1;
    var j = 1;
    var m = 0;
    while (j <= s.length) {
      if (j-i+1 > m) {
          m = j-i+1
      }
      if (s.slice(i-1,j).includes(s[j])) {
          i++;
      } else {j++}
    }
    return m;
};