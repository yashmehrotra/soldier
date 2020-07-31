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

    def test_stdout_override(self):
        new_file = open(self.testdir + '/my_file', 'w')
        soldier.run('echo hello', std_out=new_file.fileno())
        new_file.close()

        with open(self.testdir + '/my_file', 'r') as f:
            assert f.read().strip() == 'hello'

    def test_rmdir(self):
        soldier.run('rm -rf {}'.format(self.testdir))
        assert not os.path.exists(os.getcwd() + '/' + self.testdir)
