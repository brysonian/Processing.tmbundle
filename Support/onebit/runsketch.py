import sys
import onebit
import os
import commands
import subprocess

bundle_dir = os.environ['TM_BUNDLE_SUPPORT']

if os.environ.has_key('TM_PROJECT_DIRECTORY'):
	proj_dir = os.environ['TM_PROJECT_DIRECTORY']
else:
	proj_dir = os.environ['TM_DIRECTORY']
	
scratch_dir = proj_dir+'/compiled'
os.chdir(proj_dir)
dir_name = os.path.basename(os.getcwd())

template = onebit.env.get_template("runsketch.html")

print template.render(
    bundle_dir = bundle_dir,
    proj_dir = proj_dir,
    scratch_dir = scratch_dir,
    dir_name = dir_name,
    title=dir_name, 
	fullscreen=sys.argv[1],
)

