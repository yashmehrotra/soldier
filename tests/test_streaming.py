try:
    # Python2
    from StringIO import StringIO
except ImportError:
    # Python3
    from io import StringIO
import sys

import soldier

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stdout = self._stdout

class TestStreamingCommand:
    def test_stream(self):
        with Capturing() as stream_output:
            soldier.run('ls', stream=True)

        s = soldier.run('ls')
        command_output = s.output.strip().split('\n')

        assert stream_output == command_output

    def test_stream_exit_code(self):
        s = soldier.run('echo hello > /dev/null', stream=True)
        assert s.exit_code == 0
