import json,subprocess,sys,tempfile,unittest
from pathlib import Path
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[1]
class TestRedact(unittest.TestCase):
 def test_solid_redaction_and_report(self):
  with tempfile.TemporaryDirectory() as d:
   d=Path(d); src=d/'in.png'; out=d/'out.png'; rep=d/'report.json'
   im=Image.new('RGB',(200,120),'white'); ImageDraw.Draw(im).text((50,40),'TOKEN-123',fill='black'); im.save(src)
   subprocess.run([sys.executable,str(ROOT/'scripts/redact_image.py'),str(src),str(out),'--box','45,30,100,35','--padding','0','--report',str(rep)],check=True,capture_output=True,text=True)
   got=Image.open(out); self.assertEqual(got.getpixel((50,40)),(17,17,17)); self.assertNotEqual(src.read_bytes(),out.read_bytes())
   data=json.loads(rep.read_text()); self.assertTrue(data['review_required']); self.assertEqual(len(data['boxes']),1)
 def test_refuses_in_place(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'in.png'; Image.new('RGB',(20,20),'white').save(p)
   r=subprocess.run([sys.executable,str(ROOT/'scripts/redact_image.py'),str(p),str(p),'--box','1,1,5,5'],capture_output=True,text=True)
   self.assertNotEqual(r.returncode,0)
if __name__=='__main__': unittest.main()
