import r2pipe

r = r2pipe.open()
r.cmd('aaa')
r.cmd('s main')
r.cmd('V')
r.cmd('p')
