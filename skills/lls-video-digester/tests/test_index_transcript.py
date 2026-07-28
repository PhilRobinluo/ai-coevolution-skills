import json,subprocess,sys,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class T(unittest.TestCase):
 def test_srt(self):
  with tempfile.TemporaryDirectory() as d:
   d=Path(d); src=d/'a.srt'; out=d/'o.json'; src.write_text('1\n00:00:01,000 --> 00:00:03,000\n第一句\n\n2\n00:02:10,000 --> 00:02:12,000\n第二句\n')
   subprocess.run([sys.executable,str(ROOT/'scripts/index_transcript.py'),str(src),str(out),'--chunk-seconds','60'],check=True,capture_output=True,text=True); x=json.loads(out.read_text()); self.assertEqual(x['segments'],2); self.assertEqual(len(x['chunks']),2); self.assertEqual(x['chunks'][0]['start'],'00:00:01')
if __name__=='__main__':unittest.main()
