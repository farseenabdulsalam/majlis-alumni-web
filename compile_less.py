from glob import glob
from subprocess import call

less_files = glob('./less/*.less')
for less_file in less_files:
    #replace ./less/file.less with ./css/file.css
    css_file = './css/'+less_file[7:-4]+'css'
    call(['lessc',less_file,css_file])

