---
author: Mindusting
corrected: false
headerFile: false
tags:
  - Programming
  - Java
  - ORM
title: Hibernate ORM en Java
---

# HIBERNATE ORM EN JAVA

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Explicar como descargar el `.jar` para poder usar la librería:
> >     - [MVN REPOSITORY](https://mvnrepository.com/artifact/org.hibernate.orm/hibernate-core)
> >     - [`7.1.10`](https://mvnrepository.com/artifact/org.hibernate.orm/hibernate-core/7.1.10.Final)
> > - [ ] Explicar que dependiendo de la versión de Java no funcionará, por lo que hay que usar una versión reciente.

%%
`@Entity`
`@Table(name="[tableName]")`
`@Id`
`@OneToOne`
`@OneToMany`
`@ManyToOne`
`@ManyToMany`
%%

**pom.xml**

```xml
<dependency>
    <groupId>org.hibernate.orm</groupId>
    <artifactId>hibernate-core</artifactId>
    <version>6.5.2.Final</version>
</dependency>
```

**src/main/resources/hibernate.cfg.xml**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<hibernate-configuration>
    <session-factory>
        <property name="hibernate.connection.driver_class">
            com.mysql.cj.jdbc.Driver
        </property>
        <property name="hibernate.connection.url">
jdbc:mysql://localhost:3306/hibernateExample?createDatabaseIfNotExist=true
        </property>
        <property name="hibernate.connection.username">root</property>
        <property name="hibernate.connection.password"></property>
        
        <property name="hibernate.dialect">
            org.hibernate.dialect.MySQLDialect
        </property>
        
        <property name="show_sql">true</property>
        <property name="format_sql">true</property>
        
        <property name="hibernate.hbm2ddl.auto">update</property>
        
        <mapping class="Hibernate.entity.User"/>
    </session-factory>
</hibernate-configuration>
```

**Entities**

```java
@Entity
@Table(name = "users")
public class UserDB implements Serializable {
    @Serial
    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;
    @ManyToOne
    @JoinColumn(name = "userTypeId")
    private UserTypeDB userType;
}
```

****

```java
public class UserRepository {

    @Override
    public List<UserDB> selectAll() {
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            return session.createQuery("FROM users", UserDB.class).list();
        }
    }

    @Override
    public UserDB selectById(long id) {
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            return session.get(UserDB.class, id);
        }
    }

    @Override
    public void insert(UserDB t) throws DBException {
        Transaction tx = null;
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            tx = session.beginTransaction();
            session.persist(t);
            tx.commit();
        } catch (Exception ex) {
            if (tx != null) tx.rollback();
            throw new DBException("No se ha podido introducir el UserDB.");
        }
    }

    @Override
    public void update(UserDB t) throws DBException {
        Transaction tx = null;
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            tx = session.beginTransaction();
            session.merge(t);
            tx.commit();
        } catch (Exception ex) {
            if (tx != null) tx.rollback();
            throw new DBException("No se ha podido actualizar el UserDB.");
        }
    }

    @Override
    public void delete(UserDB t) throws DBException {
        Transaction tx = null;
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            tx = session.beginTransaction();
            session.remove(t);
            tx.commit();
        } catch (Exception ex) {
            if (tx != null) tx.rollback();
            throw new DBException("No se ha podido borrar el UserDB.");
        }
    }
    
    public UserDB selectByLoginAndPasswordHash(UserDB user) {
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            String sql = "FROM users WHERE login = :login AND passwordHash = :passwordHash;";
            Query<UserDB> query = session.createQuery(sql, UserDB.class);
            query.setParameter("login", user.getLogin());
            query.setParameter("passwordHash", user.getPasswordHash());
            return query.getSingleResultOrNull();
        }
    }
}
```
