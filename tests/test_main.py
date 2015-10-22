import os
import soldier


class TestBasicCommands:

    def test_pwd(self):
        pwd_output = soldier.run('pwd').output.strip()
        assert pwd_output == os.getcwd()
