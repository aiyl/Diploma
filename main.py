import os
import subprocess

ERR_OK = 0
ERR_WA = 1
ERR_PE = 2
ERR_UH = 3

path = os.path.dirname(os.path.abspath(__file__))

bPath = r"D:\Program Files\Blender Foundation\Blender\blender.exe"
blend = os.path.join(path, "scene.blend")
bscript = os.path.join(path, "scene.py")
render = os.path.join(path, "output_#")

try:
	subprocess.run([bPath, "-b", blend, "--python", bscript, "-o", render, "-f", "1"])
except Exception as e:
	print("Couldn't run subprocess {} \n".format(bPath))
	print(str(e))
	exit(-1)

print(str(ERR_OK) + '\n')


# with sqlite3.connect("test.db") as con, open("test.log", "w") as log:
# 	try:
# 		with open("solve.sql", 'r') as fid: sql = fid.read()

# 	except:
# 		log.write(str(ERR_PE) + '\n')
# 		log.write('File with query couldn\'t be read!')
# 		exit(0)
#
# 	try:
# 		cur = con.cursor()
# 		cur.execute('pragma foreign_keys = on')
# 		cur.execute('pragma query_only = on')
# 		cur.execute(sql)
# 	except (sqlite3.Warning, sqlite3.Error) as e:
# 		if type(e) in (sqlite3.ProgrammingError,
# 		               sqlite3.OperationalError,
# 		               sqlite3.Warning):
# 			log.write(str(ERR_PE) + '\n')
# 			log.write(str(e))
# 			exit(0)
#
# 		print(e, file = sys.stderr)
# 		exit(-1)
#
# 	log.write(str(ERR_OK) + '\n')
# 	ans = dumps(cur.fetchall())
# 	log.write(ans)
