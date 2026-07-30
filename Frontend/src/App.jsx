import { useEffect, useState } from 'react';
import { createStudent, getStudents } from './services/api';
import './styles.css';

const initialForm = {
  name: '',
  email: '',
  phone: '',
  age: '',
  course: '',
  address: '',
};

export default function App() {
  const [formData, setFormData] = useState(initialForm);
  const [students, setStudents] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [isSaving, setIsSaving] = useState(false);
  const [message, setMessage] = useState('');

  useEffect(() => {
    const loadStudents = async () => {
      try {
        const savedStudents = await getStudents();
        setStudents(savedStudents);
        setMessage('');
      } catch {
        setMessage('Start the backend server to load saved student records.');
      } finally {
        setIsLoading(false);
      }
    };

    loadStudents();
  }, []);

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData((current) => ({
      ...current,
      [name]: value,
    }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setIsSaving(true);
    setMessage('');

    try {
      const savedStudent = await createStudent(formData);
      setStudents((current) => [...current, savedStudent]);
      setFormData(initialForm);
      setMessage('Student saved successfully.');
    } catch {
      setMessage('Unable to save student. Please check that the backend is running.');
    } finally {
      setIsSaving(false);
    }
  };

  const clearForm = () => {
    setFormData(initialForm);
  };

  return (
    <main className="app-shell">
      <section className="student-panel">
        <div className="panel-header">
          <p className="eyebrow">Student Management</p>
          <h1>Student Details</h1>
        </div>

        <form className="student-form" onSubmit={handleSubmit}>

          <label>
            Student Name
            <input
              name="name"
              type="text"
              value={formData.name}
              onChange={handleChange}
              placeholder="Enter student name"
              required
            />
          </label>

          <label>
            Mail
            <input
              name="email"
              type="email"
              value={formData.email}
              onChange={handleChange}
              placeholder="student@gmail.com"
              required
            />
          </label>

          <label>
            Phone No
            <input
              name="phone"
              type="tel"
              value={formData.phone}
              onChange={handleChange}
              placeholder="Enter phone number"
              required
            />
          </label>

          <label>
            Age
            <input
              name="age"
              type="number"
              value={formData.age}
              onChange={handleChange}
              placeholder="Enter age"
              required
            />
          </label>

          <label>
            Course
            <input
              name="course"
              type="text"
              value={formData.course}
              onChange={handleChange}
              placeholder="Enter course"
              required
            />
          </label>

          <label className="full-width">
            Address
            <textarea
              name="address"
              value={formData.address}
              onChange={handleChange}
              placeholder="Enter address"
              rows="4"
              required
            />
          </label>

          <div className="form-actions">
            <button type="submit" disabled={isSaving}>
              {isSaving ? 'Saving...' : 'Save Student'}
            </button>

            <button
              type="button"
              className="secondary-button"
              onClick={clearForm}
            >
              Clear
            </button>
          </div>
        </form>

        {message && <p className="status-message">{message}</p>}
      </section>

      <section className="records-panel">
        <div className="panel-header">
          <p className="eyebrow">{students.length} records</p>
          <h2>Submitted Students</h2>
        </div>

        {isLoading ? (
          <p>Loading student records...</p>
        ) : students.length === 0 ? (
          <p>No student details submitted yet.</p>
        ) : (
          <div className="table-wrap">
            <table>
              <thead>
                <tr>
                  <th>Name</th>
                  <th>Mail</th>
                  <th>Phone</th>
                  <th>Age</th>
                  <th>Course</th>
                  <th>Address</th>
                </tr>
              </thead>

              <tbody>
                {students.map((student) => (
                  <tr key={student.id}>
                    <td>{student.name}</td>
                    <td>{student.email}</td>
                    <td>{student.phone}</td>
                    <td>{student.age}</td>
                    <td>{student.course}</td>
                    <td>{student.address}</td>
                  </tr>
                ))}
              </tbody>

            </table>
          </div>
        )}
      </section>
    </main>
  );
}