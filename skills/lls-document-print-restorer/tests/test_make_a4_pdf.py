import json, subprocess, sys, tempfile, unittest
from pathlib import Path
from PIL import Image, ImageDraw

ROOT=Path(__file__).resolve().parents[1]
class TestA4(unittest.TestCase):
    def test_builds_pdf_preview_and_report(self):
        with tempfile.TemporaryDirectory() as d:
            d=Path(d); src=d/'source.png'; out=d/'out.pdf'; preview=d/'preview.png'; report=d/'report.json'
            im=Image.new('RGB',(800,1200),'#dddddd'); ImageDraw.Draw(im).text((80,100),'SYNTHETIC 123',fill='black'); im.save(src)
            subprocess.run([sys.executable,str(ROOT/'scripts/make_a4_pdf.py'),str(src),str(out),'--preview',str(preview),'--report',str(report)],check=True,capture_output=True,text=True)
            self.assertTrue(out.stat().st_size>1000)
            with Image.open(preview) as rendered:
                self.assertEqual(rendered.size,(2480,3508))
            data=json.loads(report.read_text()); self.assertEqual(data['original_pixels'],[800,1200]); self.assertIn('未恢复',data['warning'])
    def test_refuses_overwrite_without_force(self):
        with tempfile.TemporaryDirectory() as d:
            d=Path(d); src=d/'source.png'; out=d/'out.pdf'; Image.new('RGB',(10,20),'white').save(src); out.write_text('old')
            r=subprocess.run([sys.executable,str(ROOT/'scripts/make_a4_pdf.py'),str(src),str(out)],capture_output=True,text=True)
            self.assertNotEqual(r.returncode,0); self.assertEqual(out.read_text(),'old')
if __name__=='__main__': unittest.main()
