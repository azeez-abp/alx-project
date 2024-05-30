'use client'
/*import Image from "next/image";*/
import Button from "@/components/Button";
import { useState } from "react";
import Link from 'next/link'
import {makeRequest} from '../request'
import { useRouter } from 'next/navigation'


const spinner_style = {
  position: 'absolute',
  right: '7em',
  top: '5px'
}


export default function Home(): any {
  const router = useRouter()
     const [loginState, setLoginState]  = useState({
      showLoader:false,
      error:false, 
      info:"", 
      inputData:{},
      suc:false})
     
     const disble_button = {
      pointerEvent: loginState.showLoader?'none':'all',
      opacity:loginState.showLoader?'0.4':'1',
      cursor:loginState.showLoader?'none':'pointer'
    }
/**
 * sigIn - function for signing user
 * @returns boolean
 */

interface ResponseDataErr{  
response:{data:{error:string}};

}

interface ResponseDataSuc{  
  data:string;
  
  }
 const signIn = (e) :boolean => {
    e.preventDefault()
    setLoginState({...loginState,showLoader:true,error:false})
    try {
      makeRequest("users/login", loginState.inputData, (err:ResponseDataErr, data:ResponseDataSuc)=>{
        console.log(data, err)
        if (err)
          {
             
            setTimeout(()=>{
              setLoginState({...loginState,showLoader:false,error:true,info:err.response.data.error})
            },3000)
            return
          }

          setTimeout(()=>{
            setLoginState({...loginState,showLoader:false,error:false,info:"Login successful",suc:true})
          },3000)

          localStorage.setItem("alx_token", data.data)
          setTimeout(()=>{
            console.log("redirect")
            router.push('/dashboard')
          },2000)
      })
    } catch (error) {
        console.log(error, "ERROR")
    }
   

  return true
 }

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
            Sign in to your account
          </h2>

         

         {(loginState.error|| loginState.suc)  && <div role="alert" className={loginState.error?'alert alert-error':'alert alert-success'}>
          <svg onClick={()=>setLoginState({...loginState, error:false,suc:false})} xmlns="http://www.w3.org/2000/svg" className="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
          <span>{loginState.info}</span>
        </div>}
       
                                                                                                                
        </div>

        <div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
          <form className="space-y-6" action="#" method="POST">
            <div>
              <label htmlFor="email" className="block text-sm font-medium leading-6 text-whute">
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
                  className="block w-full rounded-md border-0 py-1.5 text-white shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                />
              </div>
            </div>

            <div>
              <div className="flex items-center justify-between">
                <label htmlFor="password" className="block text-sm font-medium leading-6 text-white">
                  Password
                </label>
                <div className="text-sm">
                <Link href="/forget-password" className="font-semibold text-indigo-600 hover:text-indigo-500">Forgot password?</Link>
                </div>
              </div>
              <div className="mt-2">
                <input
                  id="password"
                  name="password"
                  type="password"
                  onInput={(e)=>getInput(e)}
                  autoComplete="current-password"
                  required
                  className="block w-full rounded-md border-0 py-1.5 text-white shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                />
              </div>
            </div>
             
            <div>
            <Button name="Sign in"  onclick={signIn} styles_button={{background: "rgb(79 70 229/.4)",
              height:"28px", fontWeight: 500, position: 'relative', ...disble_button, minWidth:"100%"} } >
                <span className="loading loading-spinner loading-sm"  style={{...spinner_style, display: loginState.showLoader?'block':'none'}}></span>
              </Button> 
            </div>
          </form>
          <p className="mt-10 text-center text-sm text-gray-500">
            Not a member?{' '}
            <Link href="/register" className="font-semibold leading-6 text-indigo-600 hover:text-indigo-500">
              Join as worker in the the farm
            </Link>
          </p>
        
        </div>
      </div>
      
      
    </main>
  );
}
