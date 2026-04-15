import axios from "axios"

export const api = axios.create({
  baseURL: "http://aiedu.tplinkdns.com:6100",
  withCredentials: true,
  headers: {
    "Content-Type": "application/json",
  },
})
