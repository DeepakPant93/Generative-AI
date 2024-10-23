"use strict";(self.webpackChunkmy_website=self.webpackChunkmy_website||[]).push([[507],{2002:(e,r,s)=>{s.r(r),s.d(r,{assets:()=>c,contentTitle:()=>i,default:()=>h,frontMatter:()=>t,metadata:()=>a,toc:()=>d});var n=s(4848),o=s(8453);const t={},i="Chroma DB Python Application",a={id:"comaDB/intro",title:"Chroma DB Python Application",description:"This is a Python-based application that demonstrates how to insert data into Chroma DB (a vector database) and perform search queries. The project utilizes Docker Compose to deploy Chroma DB locally for easy setup and usage. It showcases how Chroma DB can efficiently store and search vector embeddings.",source:"@site/docs/comaDB/intro.md",sourceDirName:"comaDB",slug:"/comaDB/intro",permalink:"/https://github.com/DeepakPant93/Generative-AI/docs/docs/comaDB/intro",draft:!1,unlisted:!1,editUrl:"https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/docs/comaDB/intro.md",tags:[],version:"current",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Croma Database",permalink:"/https://github.com/DeepakPant93/Generative-AI/docs/docs/category/croma-database"},next:{title:"Image Generator",permalink:"/https://github.com/DeepakPant93/Generative-AI/docs/docs/category/image-generator"}},c={},d=[{value:"Features:",id:"features",level:3},{value:"Prerequisites:",id:"prerequisites",level:3},{value:"Setup Instructions:",id:"setup-instructions",level:3},{value:"Folder Structure:",id:"folder-structure",level:3},{value:"Docker Compose Setup:",id:"docker-compose-setup",level:3},{value:"Additional Resources:",id:"additional-resources",level:3}];function l(e){const r={a:"a",code:"code",h1:"h1",h3:"h3",header:"header",li:"li",ol:"ol",p:"p",pre:"pre",strong:"strong",ul:"ul",...(0,o.R)(),...e.components};return(0,n.jsxs)(n.Fragment,{children:[(0,n.jsx)(r.header,{children:(0,n.jsx)(r.h1,{id:"chroma-db-python-application",children:"Chroma DB Python Application"})}),"\n",(0,n.jsx)(r.p,{children:"This is a Python-based application that demonstrates how to insert data into Chroma DB (a vector database) and perform search queries. The project utilizes Docker Compose to deploy Chroma DB locally for easy setup and usage. It showcases how Chroma DB can efficiently store and search vector embeddings."}),"\n",(0,n.jsx)(r.h3,{id:"features",children:"Features:"}),"\n",(0,n.jsxs)(r.ol,{children:["\n",(0,n.jsxs)(r.li,{children:[(0,n.jsx)(r.strong,{children:"Data Insertion:"})," Insert vectorized data into Chroma DB."]}),"\n",(0,n.jsxs)(r.li,{children:[(0,n.jsx)(r.strong,{children:"Vector Search:"})," Perform searches based on vector similarities."]}),"\n",(0,n.jsxs)(r.li,{children:[(0,n.jsx)(r.strong,{children:"Docker Deployment:"})," Easily run Chroma DB using Docker Compose."]}),"\n"]}),"\n",(0,n.jsx)(r.h3,{id:"prerequisites",children:"Prerequisites:"}),"\n",(0,n.jsxs)(r.ol,{children:["\n",(0,n.jsxs)(r.li,{children:[(0,n.jsx)(r.strong,{children:"Docker & Docker Compose:"})," Install Docker and Docker Compose on your machine."]}),"\n",(0,n.jsxs)(r.li,{children:[(0,n.jsx)(r.strong,{children:"Python 3.10+"}),": Ensure Python is installed."]}),"\n",(0,n.jsxs)(r.li,{children:[(0,n.jsx)(r.strong,{children:"pip"}),": For Python package management."]}),"\n"]}),"\n",(0,n.jsx)(r.h3,{id:"setup-instructions",children:"Setup Instructions:"}),"\n",(0,n.jsxs)(r.ol,{children:["\n",(0,n.jsxs)(r.li,{children:["\n",(0,n.jsx)(r.p,{children:(0,n.jsx)(r.strong,{children:"Install the required Python libraries:"})}),"\n",(0,n.jsxs)(r.p,{children:["Install dependencies using ",(0,n.jsx)(r.code,{children:"pip"}),":"]}),"\n",(0,n.jsx)(r.pre,{children:(0,n.jsx)(r.code,{className:"language-bash",children:"pip install -r requirements.txt\n"})}),"\n"]}),"\n",(0,n.jsxs)(r.li,{children:["\n",(0,n.jsx)(r.p,{children:(0,n.jsx)(r.strong,{children:"Start Chroma DB with Docker:"})}),"\n",(0,n.jsx)(r.p,{children:"Use Docker Compose to set up Chroma DB locally:"}),"\n",(0,n.jsx)(r.pre,{children:(0,n.jsx)(r.code,{className:"language-bash",children:"docker compose up -d\n"})}),"\n",(0,n.jsx)(r.p,{children:"This will pull the Chroma DB image and run the service locally."}),"\n"]}),"\n",(0,n.jsxs)(r.li,{children:["\n",(0,n.jsx)(r.p,{children:(0,n.jsx)(r.strong,{children:"Run the Application:"})}),"\n",(0,n.jsxs)(r.p,{children:["Execute the ",(0,n.jsx)(r.code,{children:"app.py"})," script to insert data and perform a search:"]}),"\n",(0,n.jsx)(r.pre,{children:(0,n.jsx)(r.code,{className:"language-bash",children:"python app.py\n"})}),"\n"]}),"\n"]}),"\n",(0,n.jsx)(r.h3,{id:"folder-structure",children:"Folder Structure:"}),"\n",(0,n.jsx)(r.pre,{children:(0,n.jsx)(r.code,{className:"language-bash",children:".\n\u251c\u2500\u2500 docker-compose.yml    # Docker Compose file for Chroma DB setup\n\u251c\u2500\u2500 app.py                # Python script for inserting data and performing search queries\n\u251c\u2500\u2500 requirements.txt      # Python dependencies\n\u2514\u2500\u2500 README.md             # Project documentation\n"})}),"\n",(0,n.jsx)(r.h3,{id:"docker-compose-setup",children:"Docker Compose Setup:"}),"\n",(0,n.jsxs)(r.p,{children:["A ",(0,n.jsx)(r.code,{children:"docker-compose.yml"})," file is used to run the Chroma DB service. You can start the service by running ",(0,n.jsx)(r.code,{children:"docker-compose up"})," from the terminal in the project directory. For further guidance on Docker deployment, refer to the official documentation."]}),"\n",(0,n.jsxs)(r.ul,{children:["\n",(0,n.jsxs)(r.li,{children:[(0,n.jsx)(r.strong,{children:"Docker Deployment Documentation"}),": ",(0,n.jsx)(r.a,{href:"https://docs.trychroma.com/deployment/docker",children:"https://docs.trychroma.com/deployment/docker"})]}),"\n"]}),"\n",(0,n.jsx)(r.h3,{id:"additional-resources",children:"Additional Resources:"}),"\n",(0,n.jsxs)(r.ul,{children:["\n",(0,n.jsxs)(r.li,{children:[(0,n.jsx)(r.strong,{children:"Chroma DB Documentation"}),": Learn more about Chroma DB and its features: ",(0,n.jsx)(r.a,{href:"https://docs.trychroma.com/",children:"https://docs.trychroma.com/"})]}),"\n",(0,n.jsxs)(r.li,{children:[(0,n.jsx)(r.strong,{children:"Reference Video"}),": Watch this video to get an overview of Chroma DB deployment: ",(0,n.jsx)(r.a,{href:"https://www.youtube.com/watch?v=QSW2L8dkaZk",children:"https://www.youtube.com/watch?v=QSW2L8dkaZk"})]}),"\n"]})]})}function h(e={}){const{wrapper:r}={...(0,o.R)(),...e.components};return r?(0,n.jsx)(r,{...e,children:(0,n.jsx)(l,{...e})}):l(e)}}}]);