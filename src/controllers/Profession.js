const Profession = require('../models/Profession');

module.exports = {
  async store(req, res) {
    const { profession_name, value } = req.body;

    const professionExist = await Profession.findOne({
      profession: profession_name,
    });

    if (professionExist) {
      return res
        .status(400)
        .json({ error: `profession ${profession_name} already exist` });
    }

    const professions = await Profession.create({
      profession: profession_name,
      value,
    });

    return res.json(professions);
  },
};
