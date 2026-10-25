import zipfile, os, shutil, glob
if os.path.isdir('out'): shutil.rmtree('out')
with zipfile.ZipFile('exparc-site.zip') as z: z.extractall('out')
site = 'out/exparc-site'
# social media slides: hosted at /social/post-NN/slide-N.jpg for the GoHighLevel scheduler, hidden from search engines
social = os.path.join(site, 'social'); os.makedirs(social, exist_ok=True)
for zp in sorted(glob.glob('social-*.zip')):
    with zipfile.ZipFile(zp) as z: z.extractall(social)
with open(os.path.join(site, '_headers'), 'a') as h:
    h.write('\n/social/*\n  X-Robots-Tag: noindex\n  Cache-Control: public, max-age=31536000\n')
print('site extracted:', len(os.listdir(site)), 'top-level entries; social slides:', len(glob.glob(social + '/post-*/*.jpg')))
