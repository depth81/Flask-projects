import React from 'react';
import {toast} from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

class App extends React.Component{
  
  constructor(props){
    super(props);
    this.state={
      _id:'',
      name:'',
      price:'',
      books:[], //Arreglo para recoger los recursos de libros.
    };
    this.handleChange = this.handleChange.bind(this);
    this.addBook = this.addBook.bind(this);
  };

  handleChange(e){
    const { name, value} = e.target;
    this.setState({
      [name]: value
    });
  };

  refreshBooks(){
    const apiUrl = `http://localhost:5600/books`
    fetch(apiUrl).then((response) => response.json())
    .then((data) => {
      this.setState({books:data});
      console.log(this.state.books);
    })
  };

  //Metodo que se ejecuta al cargar el componente
  componentDidMount(){
    this.refreshBooks();
  };

  addBook(e){
    e.preventDefault();
    if (this.state._id){
      fetch(`http://localhost:5600/books/${this.state._id.$oid}`,{
        method:'PUT',
        body: JSON.stringify({
          name: this.state.name,
          price: this.state.price,
        }),
        headers:{
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        }
      })
      .then(res => res.json())
      .then(data => {
        this.setState({_id:'',name:'', price:''});
        toast.success("Updated/Saved",{
          position: toast.POSITION.BOTTOM_RIGHT,
          autoClose:1000
        })
        this.refreshBooks();
      });
      
    }
    else{
      fetch(`http://localhost:5600/books`,{
        method:'POST',
        body:JSON.stringify(this.state),
        headers:{
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        }
      })
      .then(res => res.json())
      .then(data => {
        this.setState({name:'',price:''});
        toast.success("Updated/Saved",{
          position: toast.POSITION.BOTTOM_RIGHT,
          autoClose:1000
        })
        this.refreshBooks();
      });
    }
  }

  deleteBook(_id){
    if(window.confirm('Are you sure to delete the book?')){
      fetch(`http://localhost:5600/books/${_id}`,{
        method:'DELETE',
        headers:{
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        }
      })
      .then(res=>res.json())
      .then(data =>{
        toast.success("The book has been deleted",{
          position: toast.POSITION.TOP_LEFT,
          autoClose:2000
        })
        this.refreshBooks();
      });
    }
  }

  editBook(_id){
    fetch(`http://localhost:5600/books/${_id}`)
    .then(res => res.json())
    .then(data =>{
      this.setState({
        name:data.name,
        price:data.price,
        _id:data._id
      });
    });
  };
  
  render(){
    return(
      <div className='container'>
        <h1 style={{color:'green'}}>LIBRARY</h1>
        <div className="container">
        <h1 style={{color:'green'}}>Update books</h1>
          {/* Formulario*/}
          <form onSubmit={this.addBook}>
            <div className="mb-3">
              <label htmlFor="name">Name</label>
              <input type="text" name="name" className="form-control" 
              onChange={this.handleChange} value={this.state.name}
              placeholder="Name" autoFocus></input>
            </div>
            <div className="mb-3">
              <label htmlFor="price">Price</label>
              <input type="number" name="price" className="form-control" 
              onChange={this.handleChange} value={this.state.price}
              placeholder="Price($)"></input>
            </div>
            <button type="submit" className="btn btn-primary">Save</button>
          </form>
          {/* Fin formulario*/}
          <table className='table table-hover'>
            <thead>
              <tr>
                <th>Id</th>
                <th>Name</th>
                <th>Price</th>
              </tr>
            </thead>
            <tbody>
              {
                this.state.books.map(book =>{
                  return(
                    <tr key={JSON.stringify(book._id.$oid)}>
                      <td>{JSON.stringify(book._id.$oid)}</td>
                      <td>{book.name}</td>
                      <td>{book.price}</td>
                      <td>
                        <button onClick={()=>this.editBook(book._id.$oid)} className="btn btn-primary" style={{margin: '4px'}}>
                        Edit
                        </button>
                        <button onClick={()=>this.deleteBook(book._id.$oid)} className="btn btn-danger" style={{margin: '4px'}}>
                        Delete
                        </button>
                      </td>
                    </tr>
                  )
                })
              }
            </tbody>
          </table>
        </div>
    </div>
    );
  }
}

export default App;