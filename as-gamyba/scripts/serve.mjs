import http from 'node:http';
import {readFile,stat} from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../dist');
const basePath=(process.env.BASE_PATH||'').replace(/\/$/,'');
const port=Number(process.env.PORT||4173);
const types={'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.js':'text/javascript; charset=utf-8','.svg':'image/svg+xml','.json':'application/json','.txt':'text/plain; charset=utf-8','.xml':'application/xml','.png':'image/png','.jpg':'image/jpeg','.webp':'image/webp'};
http.createServer(async(req,res)=>{try{const url=new URL(req.url,'http://localhost');let name=decodeURIComponent(url.pathname);if(basePath){if(name==='/'||name===basePath){res.writeHead(302,{Location:basePath+'/'});return res.end();}if(!name.startsWith(basePath+'/'))throw new Error('Outside base path');name=name.slice(basePath.length);}let target=path.resolve(root,'.'+name);if(target!==root&&!target.startsWith(root+path.sep)){res.writeHead(403);return res.end('Forbidden');}const info=await stat(target);if(info.isDirectory()){if(!name.endsWith('/')){res.writeHead(301,{Location:url.pathname+'/'+url.search});return res.end();}target=path.join(target,'index.html');}res.writeHead(200,{'Content-Type':types[path.extname(target)]||'application/octet-stream','X-Content-Type-Options':'nosniff'});res.end(await readFile(target));}catch{res.writeHead(404,{'Content-Type':'text/html; charset=utf-8'});res.end(await readFile(path.join(root,'404.html')));}}).listen(port,'0.0.0.0',()=>console.log(`AS gamyba preview listening on port ${port}`));
