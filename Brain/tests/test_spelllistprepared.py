import unittest

from spelllistprepared import SpellListPrepared
from const.spellbookmaster import SpellBookMaster


class TestSpellTrigger(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.spell = SpellBookMaster.Fireball

    def test_constructor(self):
        st = SpellListPrepared(name='MyList', spell_map={ self.spell.getName() : self.spell })

    def test_getName(self):
        st = SpellListPrepared('MyList', spell_map={ self.spell.getName() : self.spell })
        self.assertEqual('MyList', st.getName())


if __name__ == '__main__':
    unittest.main()
