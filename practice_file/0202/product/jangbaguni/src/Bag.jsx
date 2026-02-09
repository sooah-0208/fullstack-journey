import { useState, useEffect } from 'react'
import { api } from '@utils/network.js'
import { useNavigate } from "react-router";
import { useAuth } from '@hooks/AuthProvider.jsx'
import { useCookies } from 'react-cookie'


const Bag = () => {
    const [list, setList] = useState([])
    const [page, setPage] = useState(1)
    const [total, setTotal] = useState(0)
    const [search, setSearch] = useState("")
    const navigate = useNavigate()
    const { checkAuth } = useAuth()
    const [cookies, setCookie, removeCookie] = useCookies(['ck']);
    const searchEvent = e => {
        e.preventDefault()
        //getData(1, search)
        setPage(1)
        setSearch("")}

        useEffect(() => {
            //getData(page, search)
            const arr1 = [
                { "no": 1, "title": "iPhone", "price": "1,700,000" },
            ]
            setList(arr1)
        }, [])
        return (
            <div className="container mt-3">
                <h1 className="display-1 text-center">JangBaguni</h1>
                <div className="d-flex justify-content-between align-items-center mt-4">
                    <div className="btn-group">
                        <button type='button' className="btn btn-primary">게시글 작성</button>
                    </div>
                    <form className="d-flex" style={{ "maxWidth": "300px" }} onSubmit={searchEvent}>
                        <input className="form-control me-2" type="search" value={search} onChange={e => setSearch(e.target.value)} placeholder="검색어를 입력하세요" />
                        <button className="btn btn-outline-dark" type="submit">Search</button>
                    </form>
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
                            list?.map((v, i) => {
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