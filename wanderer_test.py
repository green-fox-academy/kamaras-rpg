import unittest, mainloop, model_character, model_hero, model_monster

class TestStatuses(unittest.TestCase):
    def test_hero_hp(self):
        self.assertEqual(mainloop.my_hero.hp, 0)
    
    def test_monster_hp(self):
        self.assertEqual(mainloop.skeleton1.hp, 0)

    def test_boss_hp(self):
        self.assertEqual(mainloop.boss.hp, 0)

if __name__ == '__main__':
    unittest.main()