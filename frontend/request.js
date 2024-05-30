

import axios from 'axios'

  export  const makeRequest = async (url,data,cb,mtd=null,headers_opt=null)=>{
  let   header_setting  = headers_opt !==null ?headers_opt: { 
    //  'Content-Type': 'application/x-www-form-urlencoded',
      'Content-Type': 'application/json',
      'authorization': 'Bearer '+localStorage.getItem("alx_token")?localStorage.getItem("alx_token"):"",
     }
        const options = {
            method: mtd?mtd:'POST',
            headers:header_setting,
            
            // body:  {userID:inp},
             data:  data,
            url:"http://127.0.0.1:5000/api/v1/"+ url,
          };
          try {
         //   console.log(app_domain_proxy+ url)
              let d  =  await axios(options)
             let out  = d.data
            
               if(out.err){
                return cb({message:out.err,isArr:typeof out.err=='object'?true:false},null)
               }
                 cb(null,out)  
    
    
          } catch (error) {
            cb(error,null)
           
          }
    
    
        }
            