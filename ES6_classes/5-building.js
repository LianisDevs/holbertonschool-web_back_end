export default class Building {
  constructor(sqft) {
    if (this.constructor !== Building
      && this.evacuationWarningMessage === Building.prototype.evacuationWarningMessage) {
      Building.evacuationWarningMessage();
    }
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(value) {
    if (Number.isInteger(value) !== true) throw new TypeError('Sqft must be a number');
    this._sqft = value;
  }

  static evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}
