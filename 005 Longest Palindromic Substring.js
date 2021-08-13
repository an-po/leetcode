/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    var IsP = function(s2) {
        var k1 = 0;
        var k2 = s2.length-1;
        while ((k1<k2)&&(s2[k1]==s2[k2])) {
            k1++;
            k2--;
        }
        if (k1<k2) {
            return false;
        } else {
            return true;
        }
    }
    for (var i = s.length; i>1; i--) {
        for (var j = 0; j<=s.length-i; j++) {
            if (IsP(s.slice(j,j+i))) {
                return s.slice(j,j+i);
            }    
        }
        
    }
    if (s.length>0) {
        return s[0]
    } else {
        return "";
    }
    
};