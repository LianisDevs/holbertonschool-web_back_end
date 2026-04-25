export default class Pricing {
  constructor(amount, currency) {
    this.amount = amount;
    this.currency = currency;
  }

  get amount() {
    return this._amount;
  }

  set amount(value) {
    if (Number.isInteger(value) !== true) throw new TypeError('Amount must be a number');
    this._amount = value;
  }

  get currency() {
    return this._currency;
  }

  set currency(value) {
    this._currency = value;
  }

  displayFullPrice() {
    return `${this.amount} ${this.currency.name} (${this.currency.code})`;
  }

  static convertPrice(amount, conversionRate) {
    if (Number.isInteger(amount) !== true) throw new TypeError('Amount must be a number');

    if (Number.isInteger(conversionRate) !== true) throw new TypeError('Conversion rate must be a number');
    return amount * conversionRate;
  }
}
