import json,subprocess,sys,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class T(unittest.TestCase):
 def test_dry_run_and_apply(self):
  with tempfile.TemporaryDirectory() as d:
   d=Path(d); (d/'IMG_1234.png').write_bytes(b'x'); m=d/'map.json'; m.write_text(json.dumps([{'file':'IMG_1234.png','description':'GitHub 发布页'}]))
   r=subprocess.run([sys.executable,str(ROOT/'scripts/plan_rename.py'),'--root',str(d),'--mapping',str(m)],capture_output=True,text=True,check=True); self.assertTrue((d/'IMG_1234.png').exists()); self.assertIn('GitHub-发布页__IMG_1234.png',r.stdout)
   subprocess.run([sys.executable,str(ROOT/'scripts/plan_rename.py'),'--root',str(d),'--mapping',str(m),'--apply'],check=True,capture_output=True,text=True); self.assertTrue((d/'GitHub-发布页__IMG_1234.png').exists())
 def test_collision_stops(self):
  with tempfile.TemporaryDirectory() as d:
   d=Path(d); (d/'a.png').write_bytes(b'a'); (d/'测试__a.png').write_bytes(b'b')
   r=subprocess.run([sys.executable,str(ROOT/'scripts/plan_rename.py'),str(d/'a.png'),'--description','测试','--root',str(d)],capture_output=True,text=True); self.assertNotEqual(r.returncode,0); self.assertTrue((d/'a.png').exists())
if __name__=='__main__':unittest.main()
