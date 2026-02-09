import { useState, useEffect } from 'react'
import { api } from '@utils/network.js'
import { useNavigate } from "react-router";
import { useAuth } from '@hooks/AuthProvider.jsx'
import { useCookies } from 'react-cookie'
import { productArr } from "../data/data";


const Bag = () => {
    const nav = useNavigate()
    const { checkAuth } = useAuth()
    const [cookies, setCookie, removeCookie] = useCookies(['jangbaguni']);
    

    const del_cookie = () => {
        removeCookie(name = "jangbaguni", { path: '/' })
        alert('삭제되었습니다.')
    }
    

    return (
        <div className="container mt-3">
            <h1 className="display-1 text-center">JangBaguni</h1>
            <div className="d-flex justify-content-between align-items-center mt-4">
                <div className="btn-group">
                    <button type='button' className="btn btn-primary" onClick={del_cookie}>장바구니 비우기</button>
                </div>
            </div>
            <table className="table table-hover mt-3 text-center">
                <thead className="table-dark">
                    <tr>
                        <th>no</th>
                        <th>Product</th>
                        <th>Price</th>
                    </tr>
                </thead>
                <tbody>
                    {
                        bags?.map((v, i) => {
                            return (
                                <tr className="cursor-pointer" key={i}>
                                    <td>{v.no}</td>
                                    <td>{v.title}</td>
                                    <td>{v.price}</td>
                                </tr>
                            )
                        })
                    }
                </tbody>
            </table>
        </div>
    )
}


export default Bag