import axios from "axios"

export const api = axios.create({
  baseURL: "http://aiedu.tplinkdns.com:6101",
  withCredentials: true,
  headers: {
    "Content-Type": "application/json",
  },
})
