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
        assert os.path.exists(os.getcwd() + '/' + self.testdir)

    def test_pipe(self):
        ls_output = soldier.run('ls | grep {}'.format(self.testdir)).\
                        output.strip()
        assert ls_output == self.testdir

    def test_cwd(self):
        output = soldier.run('ls | grep {}'.format(self.testdir), cwd=self.testdir).\
                output.strip()

        assert output == ''

    def test_cwd(self):
        output = soldier.run('printenv', env={'TEST_VAR': 'VALUE'}).\
                output.strip()

        assert output == 'TEST_VAR=VALUE'

    def test_rmdir(self):
        soldier.run('rmdir {}'.format(self.testdir))
        assert not os.path.exists(os.getcwd() + '/' + self.testdir)
