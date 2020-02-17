const isValid = require('date-fns/isValid');
const Profession = require('../models/Profession');
const calculatePayment = require('../utils/calculatePayment');

module.exports = {
  async search(req, res) {
    const { start_date, days_available } = req.body;
    const { profession } = req.query;

    const professionExist = await Profession.findOne({
      profession,
    });

    if (!professionExist) {
      return res
        .status(400)
        .json({ error: `profession ${profession} do not exist` });
    }

    const { value } = professionExist;

    const isDateValid = isValid(new Date(start_date));

    if (isDateValid === false) {
      return res.status(400).json({
        error: 'invalid date type',
        correct: 'yyyy-mm-dd or mm-dd-yyyy',
      });
    }

    const initialDate = new Date(start_date);

    if (days_available < 0) {
      return res.status(400).json({ error: 'invalid day' });
    }

    const calculate = calculatePayment(initialDate, days_available, value);

    return res.json({
      profession,
      value,
      payment: calculate,
    });
  },
};
