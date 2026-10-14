// Publish only generated static files, preserving the existing Pages history.
// Uses existing Git authentication; no tokens are stored in files or remote URLs.
import {execFileSync} from 'node:child_process';
import {mkdtemp,rm,access} from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import {fileURLToPath} from 'node:url';
const app=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const run=(args,opts={})=>execFileSync('git',args,{cwd:app,encoding:'utf8',...opts}).trim();
const gitDir=run(['rev-parse','--absolute-git-dir']);
await access(path.join(app,'dist/index.html'));
const remote=run(['ls-remote','--heads','origin','refs/heads/gh-pages']);
let parent='';
if(remote){run(['fetch','--no-tags','origin','refs/heads/gh-pages']);parent=run(['rev-parse','FETCH_HEAD']);}
const temp=await mkdtemp(path.join(os.tmpdir(),'as-gamyba-pages-'));
try{
 const env={...process.env,GIT_INDEX_FILE:path.join(temp,'index')};
 const git=['--git-dir',gitDir,'--work-tree',path.join(app,'dist')];
 run([...git,'read-tree','--empty'],{env});run([...git,'add','--all','.'],{cwd:path.join(app,'dist'),env});
 const tree=run([...git,'write-tree'],{env});
 if(parent&&run(['rev-parse',parent+'^{tree}'])===tree){console.log('Pages content already matches; no push needed.');}
 else{
  const args=['-c','user.name=AS gamyba preview automation','-c','user.email=as-gamyba-preview@users.noreply.github.com','commit-tree',tree];
  if(parent)args.push('-p',parent);
  const sha=run(args,{input:'Publish AS gamyba design preview\n'});
  run(['push','origin',`${sha}:refs/heads/gh-pages`],{stdio:['pipe','pipe','pipe']});
  console.log(`Published static site to gh-pages: ${sha}`);
 }
}finally{await rm(temp,{recursive:true,force:true});}
