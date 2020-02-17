const { Schema, model } = require('mongoose');

const ProfessionSchema = new Schema({
  profession: {
    type: String,
    required: true,
  },
  value: {
    type: Number,
    required: true,
  },
});

module.exports = model('Profession', ProfessionSchema);
