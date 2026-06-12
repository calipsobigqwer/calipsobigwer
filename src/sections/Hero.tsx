import styles from './Hero.module.css'

const Hero = () => {
  return (
    <section className={styles.hero}>
      <div className="container">
        <div className={styles.content}>
          <h1 className={styles.title}>
            Building Modern <br />
            <span>Digital Experiences</span>
          </h1>
          <p className={styles.subtitle}>
            I'm a Frontend Developer specializing in React and TypeScript.
            I create clean, performant, and user-friendly websites.
          </p>
          <div className={styles.actions}>
            <a href="#projects" className={styles.primaryBtn}>View Work</a>
            <a href="#contact" className={styles.secondaryBtn}>Contact Me</a>
          </div>
        </div>
      </div>
    </section>
  )
}

export default Hero
