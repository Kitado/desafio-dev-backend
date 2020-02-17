const differenceInBusinessDays = require('date-fns/differenceInBusinessDays');

module.exports = function calculatePayment(startDate, days, value) {
  Date.prototype.addDays = function(days) {
    const date = new Date(this.valueOf());
    date.setDate(date.getDate() + days);
    return date;
  };

  const endDate = startDate.addDays(days);

  const calculateBusinessDays = differenceInBusinessDays(startDate, endDate);

  const result = calculateBusinessDays * value;

  return Math.abs(result);
};
