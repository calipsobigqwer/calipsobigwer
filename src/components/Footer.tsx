const Footer = () => {
  return (
    <footer style={{ padding: '2rem 0', borderTop: '1px solid #e2e8f0', textAlign: 'center' }}>
      <div className="container">
        <p>&copy; {new Date().getFullYear()} Calipso. All rights reserved.</p>
      </div>
    </footer>
  )
}

export default Footer
