import os
import soldier


class TestBasicCommands:

    def setup(self):
        self.testdir = 'testdir'

    def test_pwd(self):
        pwd_output = soldier.run('pwd').output.strip()
        assert pwd_output == os.getcwd()

    def test_mkdir(self):
        soldier.run('mkdir {}'.format(self.testdir))
        assert os.path.exists(os.getcwd() + '/' + self.testdir) == True

    def test_rmdir(self):
        soldier.run('rmdir {}'.format(self.testdir))
        assert os.path.exists(os.getcwd() + '/' + self.testdir) == False
