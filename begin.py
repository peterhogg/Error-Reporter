import subprocess;
import sys;
command = '';
for cmd in sys.argv[1:]:
	command=command+' '+cmd;
p = subprocess.Popen(command,shell=True,
		stderr=subprocess.PIPE);
out, err = p.communicate()
print err;
