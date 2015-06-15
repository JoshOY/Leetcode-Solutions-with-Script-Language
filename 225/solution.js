/**
 * @constructor
 */
var Stack = function() {
    this.data = [];
};

/**
 * @param {number} x
 * @returns {void}
 */
Stack.prototype.push = function(x) {
    this.data = this.data.concat(x);
};

/**
 * @returns {void}
 */
Stack.prototype.pop = function() {
    this.data.pop();
};

/**
 * @returns {number}
 */
Stack.prototype.top = function() {
    return this.data[this.data.length - 1];
};

/**
 * @returns {boolean}
 */
Stack.prototype.empty = function() {
    return this.data.length === 0;
};