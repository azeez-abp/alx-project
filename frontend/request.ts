

import axios from 'axios'
  export const backend_path  = "http://127.0.0.1:5000"
  export  const  makeRequest: (url: string, data: any, cb: (error?: object | null | any , response?: object | null | any) => void, mtd?: string, headers_opt?: any) => Promise<void> = async (url, data, cb, mtd, headers_opt) =>{
  let   header_setting  = headers_opt !==null ?headers_opt: { 
    //  'Content-Type': 'application/x-www-form-urlencoded',
      'Content-Type': 'application/json',
      'authorization': 'Bearer '+localStorage.getItem("alx_token")?localStorage.getItem("alx_token"):"",
     }
     console.log(data, "DATA",mtd, headers_opt)
        const options = {
            method: mtd? mtd: 'POST',
            headers:header_setting,
            
            // body:  {userID:inp},
             data:  data,
            url:"http://127.0.0.1:5000/api/v1/"+ url,
          };
          try {
         //   console.log(app_domain_proxy+ url)
             let d  =  await axios(options)
             let out  = d.data
                 console.log(typeof out.error, out.error, "TRY OUT")
              if(out.error){

                  console.log(out, "Try Error")
                return cb(out.error, null)
               }
                
 
               return cb(null,out)  
    
    
          } catch (error:any) {
            
             if (
             error &&
             error.hasOwnProperty('response') && 
             error.response.hasOwnProperty('data') && 
             error.response.data.hasOwnProperty('error')) 
             {
               return cb({error: error.response.data.error},null)// Property exists, safe to use error.response.dat
            }
            
            return cb({error: error.message},null)
           
          }
    
    
        }
            