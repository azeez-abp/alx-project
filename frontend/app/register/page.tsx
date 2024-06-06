'use client'
/*import Image from "next/image";*/
import Button from "@/components/Button";
import { useState } from "react";
import Link from 'next/link'
import {makeRequest} from '../../request'
import { useRouter } from 'next/navigation'


const spinner_style = {
  position: 'absolute',
  left: '17em',
  top: '-18px'
}

const Register = () => {

  const router = useRouter()
  const [loginState, setLoginState]  = useState({
   showLoader:false,
   error:false, 
   info:"", 
   inputData:{
    "email": "",
    "password": "",
    "first_name": "",
    "middle_name": "",
    "last_name": "",
    "date_of_birth": "",
    "state": "",
    "city": "",
    "street": "",
    "profile_pix": "",
    "gender": "",
    "zip_code": "2000525"
},
   suc:false})
  
  const disble_button = {
    pointerEvents: loginState.showLoader ? 'none' : 'all',
   opacity:loginState.showLoader ? '0.4' : '1',
   cursor:loginState.showLoader? 'none' : 'pointer'
 }

  /* @returns boolean
  */
 
 interface ResponseDataErr{  
 response:{data:{error:string}};
 
 }
 
 interface ResponseDataSuc{  
   data:string;
   error:string;
   success:string;
   
   }
 
 



  const signIn = (e: any) :boolean => {
     e.preventDefault()
     setLoginState({...loginState,showLoader:true,error:false})

   
     if (
       loginState.inputData['email'] === undefined
        || 
       loginState.inputData['password']  === undefined
     )
       {
         setLoginState({
           ...loginState,
           error:true,
           info: "Email and password are required",
           showLoader:false
         })
         return false
       }
   
     try {
         
 
 
       makeRequest("users/register", loginState.inputData, (err:ResponseDataErr, data:ResponseDataSuc)=>{
             console.log(err, data.error)
         if (err)
           {
              
             setTimeout(()=>{
               setLoginState({...loginState,showLoader:false,error:true,info:err.response.data.error})
             },3000)
             return
           }

           if (data['error'] !== "" )
            {
               
              setTimeout(()=>{
                setLoginState({...loginState,showLoader:false,error:true,info:data.error})
              },3000)
              return
            }


 
           setTimeout(()=>{
             setLoginState({...loginState,showLoader:false,error:false,info:"Registration successful",suc:true})
           },3000)
 
          
       })
     } catch (error:any) {
          
         setLoginState({...loginState,showLoader:true,error:true, info: error.message})
     }
    
 
   return true
  }
 

  const handleFileChange = (e:any) => {
    const file = e.target.files[0];
    const reader = new FileReader();
    reader.onloadend = () => {
      let data = {...loginState, inputData:{...loginState.inputData, 
    
        [e.target.name]: reader.result, 
        [e.target.id]: e.target.value,
       }}
       console.log(reader.result)
     setLoginState(data)
    };
    reader.readAsDataURL(file);
  };


 const getInput = (e:any)=>{
   e.preventDefault()
  let data:any = {}
     data = {...loginState, inputData:{...loginState.inputData, [e.target.name]: e.target.value }}
     setLoginState(data)
 }

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24 text-white">

    <div className="flex min-h-full flex-1 w-full flex-col justify-center px-6 py-0 lg:px-8">
      <div className="sm:mx-auto sm:w-full sm:max-w-sm relative">
        <img
          className="mx-auto h-20 w-20"
          src="./images/logo.png"
          alt="Your Company"
        />
        
        

        <h2 className="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-white">
          Register
        </h2>

       

       {(loginState.error|| loginState.suc)  && <div role="alert" className={loginState.error?'alert alert-error':'alert alert-success'}>
        <svg onClick={()=>setLoginState({...loginState, error:false,suc:false})} xmlns="http://www.w3.org/2000/svg" className="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
        <span>{loginState.info}</span>
      </div>}
     
                                                                                                              
      </div>

      <div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
        <form className="space-y-6" action="#" method="POST">
        <div>
            <label htmlFor="email" className="block text-sm font-medium leading-6 text-white">
              First name
            </label>
            <div className="mt-2">
              <input
                id="fname"
                name="first_name"
                type="text"
                autoComplete="none"
                onInput={(e)=>getInput(e)}
                required
                className="block w-full rounded-md border-0  py-1.5 px-2 text-white shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
              />
            </div>
          </div>

          <div>
            <label htmlFor="email" className="block text-sm font-medium leading-6 text-white">
              Middle name
            </label>
            <div className="mt-2">
              <input
                id="mname"
                name="middle_name"
                type="text"
                autoComplete="none"
                onInput={(e)=>getInput(e)}
                required
                className="block w-full rounded-md border-0 py-1.5 px-2 text-white shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
              />
            </div>
          </div>

          <div>
            <label htmlFor="email" className="block text-sm font-medium leading-6 text-white">
              Last name
            </label>
            <div className="mt-2">
              <input
                id="lname"
                name="last_name"
                type="text"
                autoComplete="email"
                onInput={(e)=>getInput(e)}
                required
                className="block w-full rounded-md border-0 py-1.5 px-2 text-white shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
              />
            </div>
          </div>

          

          

          <div>
            <label htmlFor="email" className="block text-sm font-medium leading-6 text-white">
              Email address
            </label>
            <div className="mt-2">
              <input
                id="email"
                name="email"
                type="email"
                autoComplete="email"
                onInput={(e)=>getInput(e)}
                required
                className="block w-full rounded-md border-0 py-1.5 px-2 text-white shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
              />
            </div>
          </div>


          <div>
            <label htmlFor="email" className="block text-sm font-medium leading-6 text-white">
             Date of birth
            </label>
            <div className="mt-2">
              <input
                id="dob"
                name="date_of_birth"
                type="date"
                autoComplete="date"
                onInput={(e)=>getInput(e)}
                required
                className="block w-full rounded-md border-0 py-1.5 px-2 text-white shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
              />
            </div>
          </div>


          <div>
            <label htmlFor="email" className="block text-sm font-medium leading-6 text-white">
             State
            </label>
            <div className="mt-2">
              <input
                id="state"
                name="state"
                type="text"
                autoComplete="on"
                onInput={(e)=>getInput(e)}
                required
                className="block w-full rounded-md border-0 py-1.5 px-2 text-white shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
              />
            </div>
          </div>


          <div>
            <label htmlFor="email" className="block text-sm font-medium leading-6 text-white">
             City
            </label>
            <div className="mt-2">
              <input
                id="city"
                name="city"
                type="text"
                autoComplete="on"
                onInput={(e)=>getInput(e)}
                required
                className="block w-full rounded-md border-0 py-1.5 px-2 text-white shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
              />
            </div>
          </div>

          <div>
            <label htmlFor="email" className="block text-sm font-medium leading-6 text-white">
             Street
            </label>
            <div className="mt-2">
              <input
                id="street"
                name="street"
                type="text"
                autoComplete="on"
                onInput={(e)=>getInput(e)}
                required
                className="block w-full rounded-md border-0 py-1.5 px-2 text-white shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
              />
            </div>
          </div>




         
          <div>
            <div className="flex items-center justify-between">
              <label htmlFor="password" className="block text-sm font-medium leading-6 text-white">
                Password
              </label>
            
            </div>
            <div className="mt-2">
              <input
                id="password"
                name="password"
                type="password"
                onInput={(e)=>getInput(e)}
                autoComplete="current-password"
                required
                className="block w-full rounded-md border-0 py-1.5 px-2 text-white shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
              />
            </div>
          </div>
           
          <div>
            <label htmlFor="email" className="block text-sm font-medium leading-6 text-white">
              Last name
            </label>
            <div className="mt-2">
            <select defaultValue={"Male"} name="gender" onInput={(e)=>getInput(e)}
             className="select select-primary w-full max-w-xs">
              <option disabled defaultValue={"Gender"}>Gender</option>
              <option>Male</option>
              <option>Female</option>
            </select>
            </div>
          </div> 
        
        <label className="form-control w-full max-w-xs">
        <div className="label">
          {/* <span className="label-text">Pick a file</span>
          <span className="label-text-alt">Alt label</span> */}
        </div>
        <input type="file" id="profile_pix_name" onInput={handleFileChange} name="profile_pix" className="file-input file-input-bordered w-full max-w-xs" />
        <div className="label">
        
        </div>
      </label>
           
          <div>
          <Button name="Sign in"  onclick={signIn} styles_button={{background: "rgb(79 70 229/.4)",
            height:"28px", fontWeight: 500, position: 'relative', ...disble_button, minWidth:"100%"} } >
              <span className="loading loading-spinner loading-sm"  style = {{...spinner_style, position: "relative", display: loginState.showLoader?"block":"none"}}></span>
            </Button> 
          </div>
        </form>
        <p className="mt-10 text-center text-sm text-gray-500">
          Not a member?{' '}
          <Link href="/login" className="font-semibold leading-6 text-indigo-600 hover:text-indigo-500">
           Login
          </Link>
        </p>
      
      </div>
    </div>
    
    
  </main>
  )
}

export default Register